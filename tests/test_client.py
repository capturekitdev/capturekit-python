from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qsl, urlsplit

import httpx
import pytest

from capturekit import (
    ENDPOINTS,
    AsyncCaptureKitClient,
    BinaryResponse,
    CaptureKitAPIError,
    CaptureKitClient,
    CaptureKitConfigurationError,
    CaptureKitResponseDecodingError,
    CaptureKitSerializationError,
    CaptureKitTransportError,
    JsonResponse,
    RequestOptions,
)

Responder = Callable[[httpx.Request], httpx.Response]


def _json(body: Any, status: int = 200) -> httpx.Response:
    return httpx.Response(status, json=body)


def _client(
    responder: Responder = lambda _r: _json({"ok": True}), **kwargs: Any
) -> tuple[CaptureKitClient, list[httpx.Request]]:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return responder(request)

    http_client = httpx.Client(transport=httpx.MockTransport(handler))
    kwargs.setdefault("api_key", "test-key")
    return CaptureKitClient(http_client=http_client, **kwargs), requests


def test_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CAPTUREKIT_API_KEY", raising=False)
    with pytest.raises(CaptureKitConfigurationError, match="CAPTUREKIT_API_KEY"):
        CaptureKitClient()
    with pytest.raises(CaptureKitConfigurationError):
        CaptureKitClient("   ")


def test_reads_api_key_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CAPTUREKIT_API_KEY", "env-key")
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return _json({})

    with CaptureKitClient(
        http_client=httpx.Client(transport=httpx.MockTransport(handler))
    ) as client:
        client.request("GET", "/v1/usage")
    assert requests[0].headers["x-api-key"] == "env-key"


def test_rejects_invalid_configuration() -> None:
    with pytest.raises(CaptureKitConfigurationError):
        CaptureKitClient("k", base_url="ftp://example.test")
    with pytest.raises(CaptureKitConfigurationError):
        CaptureKitClient("k", timeout=0)


def test_featured_operation_sends_get_with_api_key() -> None:
    client, requests = _client(lambda _r: _json({"hello": "world"}))
    response = client.content(url="https://example.com")
    assert isinstance(response, JsonResponse)
    assert response.data == {"hello": "world"}
    request = requests[0]
    assert request.method == "GET"
    assert str(request.url).split("?")[0] == "https://api.capturekit.dev/v1/content"
    assert request.headers["x-api-key"] == "test-key"
    assert request.headers["user-agent"].startswith("capturekit-python/")


def test_query_serialization() -> None:
    client, requests = _client(base_url="https://example.test/")
    client.request(
        "GET",
        "/v1/anything",
        {
            "text": "a b&c",
            "flag": False,
            "count": 0,
            "ratio": 1.5,
            "whole": 2.0,
            "list": ["x", "y"],
            "nothing": None,
        },
    )
    url = urlsplit(str(requests[0].url))
    assert url.netloc == "example.test"
    assert parse_qsl(url.query) == [
        ("text", "a b&c"),
        ("flag", "false"),
        ("count", "0"),
        ("ratio", "1.5"),
        ("whole", "2"),
        ("list", "x"),
        ("list", "y"),
    ]


def test_post_sends_json_body() -> None:
    client, requests = _client()
    client.request("POST", "/v1/anything", {"query": "x", "page": 2, "gone": None})
    request = requests[0]
    assert request.method == "POST"
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {"query": "x", "page": 2}
    assert request.url.query == b""


def test_post_keeps_global_parameters_in_query() -> None:
    client, requests = _client()
    client.request("POST", "/v1/anything", {"query": "x", "is_async": True, "fields": "a"})
    request = requests[0]
    assert json.loads(request.content) == {"query": "x"}
    assert request.url.query == b"fields=a&is_async=true"


def test_path_parameters() -> None:
    client, requests = _client()
    client.request("GET", "/v1/items/{id}", {"id": "a/b c", "other": 1})
    assert requests[0].url.raw_path == b"/v1/items/a%2Fb%20c?other=1"
    with pytest.raises(CaptureKitSerializationError):
        client.request("GET", "/v1/items/{id}", {})


def test_unsupported_method_is_rejected() -> None:
    client, requests = _client()
    with pytest.raises(CaptureKitConfigurationError):
        client.jobs(id="test", request_options=RequestOptions(method="POST"))
    assert requests == []


def test_dual_operation_can_use_post() -> None:
    client, requests = _client(lambda _r: _json({}))
    client.analyze(url="test", request_options=RequestOptions(method="POST"))
    assert requests[0].method == "POST"
    assert json.loads(requests[0].content) == {"url": "test"}


@pytest.mark.parametrize("name", sorted(ENDPOINTS))
def test_every_endpoint_method(name: str) -> None:
    client, requests = _client(lambda _r: _json({}))
    method = getattr(client, name + "_" if not hasattr(client, name) else name)
    kwargs: dict[str, Any] = REQUIRED.get(name, {})
    method(**kwargs)
    endpoint = ENDPOINTS[name]
    expected = endpoint.path.replace("{id}", "test")
    assert requests[0].url.path == expected
    assert requests[0].method == endpoint.methods[0]


def test_binary_response() -> None:
    client, _ = _client(
        lambda _r: httpx.Response(200, content=b"\x89PNG", headers={"content-type": "image/png"})
    )
    response = client.request("GET", "/v1/anything")
    assert isinstance(response, BinaryResponse)
    assert response.bytes == b"\x89PNG"
    assert response.content_type == "image/png"


def test_non_json_success_for_json_operation() -> None:
    client, _ = _client(
        lambda _r: httpx.Response(200, content=b"<html>", headers={"content-type": "text/html"})
    )
    with pytest.raises(CaptureKitResponseDecodingError):
        client.content(url="https://example.com")


def test_api_error() -> None:
    client, _ = _client(lambda _r: _json({"error": "Invalid API Key"}, 401))
    with pytest.raises(CaptureKitAPIError) as info:
        client.request("GET", "/v1/usage")
    assert info.value.status == 401
    assert str(info.value) == "Invalid API Key"
    assert info.value.response_body == {"error": "Invalid API Key"}


def test_non_json_error_body() -> None:
    client, _ = _client(lambda _r: httpx.Response(502, content=b"Bad gateway"), max_retries=0)
    with pytest.raises(CaptureKitAPIError) as info:
        client.request("GET", "/v1/usage")
    assert info.value.status == 502
    assert info.value.raw_response.body == b"Bad gateway"


def test_transport_error() -> None:
    def fail(_request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("down")

    client, _ = _client(fail, max_retries=0)
    with pytest.raises(CaptureKitTransportError):
        client.request("GET", "/v1/usage")


def test_closed_client() -> None:
    client, _ = _client()
    client.close()
    with pytest.raises(CaptureKitConfigurationError):
        client.request("GET", "/v1/usage")


@pytest.mark.asyncio
async def test_async_client() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return _json({"async": True})

    async with AsyncCaptureKitClient(
        "k", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
    ) as client:
        response = await client.content(url="https://example.com")
    assert isinstance(response, JsonResponse)
    assert response.data == {"async": True}
    assert requests[0].headers["x-api-key"] == "k"


def test_retries_then_succeeds() -> None:
    statuses = [503, 429, 200]
    client, requests = _client(lambda _r: _json({"ok": True}, statuses.pop(0)), retry_delay=0.001)
    response = client.request("GET", "/v1/usage")
    assert isinstance(response, JsonResponse)
    assert len(requests) == 3


def test_gives_up_after_max_retries() -> None:
    client, requests = _client(
        lambda _r: _json({"error": "busy"}, 503), retry_delay=0.001, max_retries=2
    )
    with pytest.raises(CaptureKitAPIError):
        client.request("GET", "/v1/usage")
    assert len(requests) == 3


def test_never_retries_client_errors() -> None:
    client, requests = _client(
        lambda _r: _json({"error": "Payment required"}, 402), retry_delay=0.001
    )
    with pytest.raises(CaptureKitAPIError):
        client.request("GET", "/v1/usage")
    assert len(requests) == 1


def test_retries_network_errors_and_retry_after() -> None:
    calls = {"n": 0}

    def flaky(_request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ConnectError("reset")
        if calls["n"] == 2:
            return httpx.Response(429, json={}, headers={"retry-after": "0"})
        return _json({"ok": True})

    client, _ = _client(flaky, retry_delay=0.001)
    client.request("GET", "/v1/usage")
    assert calls["n"] == 3


@pytest.mark.parametrize(
    ("message", "expected_calls"),
    [
        ("Rate limit exceeded: You've exceeded the rate limit on your subscription", 2),
        ("Rate limit exceeded for the API key: quota daily", 1),
        ("Invalid API Key", 1),
    ],
)
def test_401_rate_limits_are_retried_but_not_quotas(message: str, expected_calls: int) -> None:
    calls = {"n": 0}

    def respond(_request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return _json({"error": message}, 401) if calls["n"] == 1 else _json({"ok": True})

    client, requests = _client(respond, retry_delay=0.001)
    try:
        client.request("GET", "/v1/usage")
    except CaptureKitAPIError:
        pass
    assert len(requests) == expected_calls


def test_global_parameters() -> None:
    client, requests = _client(lambda _r: _json({"job_id": "j1"}))
    client.content(url="https://example.com", fields="a,b.c", is_async=True, soft_fail=False)
    query = dict(parse_qsl(urlsplit(str(requests[0].url)).query))
    assert query["fields"] == "a,b.c"
    assert query["is_async"] == "true"
    assert query["soft_fail"] == "false"


def test_request_level_retry_override() -> None:
    client, requests = _client(lambda _r: _json({}, 500), retry_delay=0.001)
    with pytest.raises(CaptureKitAPIError):
        client.request("GET", "/v1/usage", max_retries=0)
    assert len(requests) == 1


def test_batch_keeps_order_and_isolates_failures() -> None:
    client, requests = _client(lambda r: _json({"q": r.url.params["q"]}))

    def task(q: str) -> Any:
        if q == "bad":
            raise ValueError("boom")
        return client.request("GET", "/v1/usage", {"q": q})

    results = client.batch(["a", "bad", "c"], task, concurrency=2)
    assert [r.index for r in results] == [0, 1, 2]
    assert [r.ok for r in results] == [True, False, True]
    assert isinstance(results[1].error, ValueError)
    assert len(requests) == 2
    with pytest.raises(CaptureKitConfigurationError):
        client.batch([1], lambda x: x, concurrency=0)


@pytest.mark.asyncio
async def test_async_batch_caps_concurrency() -> None:
    import asyncio

    async with AsyncCaptureKitClient(
        "k", http_client=httpx.AsyncClient(transport=httpx.MockTransport(lambda r: _json({})))
    ) as client:
        running = peak = 0

        async def task(n: int) -> int:
            nonlocal running, peak
            running += 1
            peak = max(peak, running)
            await asyncio.sleep(0.005)
            running -= 1
            return n * 10

        results = await client.batch(range(6), task, concurrency=2)
    assert peak == 2
    assert [r.value for r in results] == [0, 10, 20, 30, 40, 50]


def test_wait_for_job() -> None:
    statuses = ["Queued", "Running", "CompletedJob"]
    client, requests = _client(lambda _r: _json({"status": statuses.pop(0), "progress": 50}))
    seen: list[Any] = []
    job = client.wait_for_job("abc", interval=0.001, on_progress=seen.append)
    assert job.data["status"] == "CompletedJob"
    assert len(requests) == 3
    assert requests[0].url.path == "/v1/jobs/abc"
    assert len(seen) == 3


def test_wait_for_job_times_out() -> None:
    from capturekit import CaptureKitJobTimeoutError

    client, _ = _client(lambda _r: _json({"status": "Running"}))
    with pytest.raises(CaptureKitJobTimeoutError):
        client.wait_for_job("abc", interval=0.01, timeout=0.001)


REQUIRED: dict[str, dict[str, Any]] = {
    "analyze": {"url": "test"},
    "capture": {"url": "https://www.amazon.com/s?k=pokemon"},
    "content": {"url": "test"},
    "jobs": {"id": "test"},
    "website_crawler": {"query": "test"},
}
