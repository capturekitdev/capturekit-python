# CaptureKit Python SDK

The official Python SDK for the [CaptureKit](https://www.capturekit.dev) screenshot API.

Capture websites as PNG, JPEG, WebP or PDF, extract their content, or analyse them with AI.

The SDK exposes **7 typed methods**, one per documented endpoint, with blocking and `asyncio` clients built on [HTTPX](https://www.python-httpx.org/), plus a generic `request()`.

## Requirements

- Python 3.11 or newer

## Installation

```sh
pip install capturekitdev
```

## Get your API key

[Sign up for CaptureKit](https://app.capturekit.dev/register) or sign in, then copy your API key from the [dashboard](https://app.capturekit.dev). The client reads the `CAPTUREKIT_API_KEY` environment variable when no key is passed.

## Quick start

```python
import os

from capturekit import CaptureKitClient

with CaptureKitClient(os.environ["CAPTUREKIT_API_KEY"]) as client:
    response = client.content(url="https://example.com")
    print(response.data)
```

Keyword arguments mirror the [API reference](https://app.capturekit.dev/openapi). Python keywords get a trailing underscore (`from_=`), and the wire name is used on the request.

## Binary responses

Endpoints that can return a file (image, PDF…) return a `JsonResponse` or a `BinaryResponse`:

```python
from capturekit import BinaryResponse

response = client.capture(url="https://example.com", format="png")
if isinstance(response, BinaryResponse):
    with open("screenshot.png", "wb") as file:
        file.write(response.bytes)
```

## Async jobs

Any call accepts `is_async: true` (useful past the 60-second server limit): the response is then a `job_id`. `wait_for_job()` polls `GET /v1/jobs/{id}` until the job reaches a terminal status (`CompletedJob`, `Error`, `NotFound`, `BadRequest`):

```python
submitted = client.content(url="https://example.com", is_async=True)
job = client.wait_for_job(
    submitted.data["job_id"],
    on_progress=lambda j: print(j["status"], j.get("progress")),
)
print(job.data)
```

## Async I/O

```python
import asyncio

from capturekit import AsyncCaptureKitClient


async def main() -> None:
    async with AsyncCaptureKitClient() as client:
        response = await client.content(url="https://example.com")
        print(response.data)


asyncio.run(main())
```

## GET or POST

Methods use GET when the endpoint supports it (parameters in the query string). POST sends the same parameters as a JSON body:

```python
from capturekit import RequestOptions

client.analyze(url="test", request_options=RequestOptions(method="POST"))
```

`None` values are omitted, `False` and `0` are sent, and sequences repeat the parameter name.

## Any endpoint

```python
response = client.request("GET", "/v1/usage")
```

## Errors

```python
from capturekit import CaptureKitAPIError

try:
    client.content(url="https://example.com")
except CaptureKitAPIError as error:
    print(error.status, error, error.response_body)
```

| Error | When |
| --- | --- |
| `CaptureKitConfigurationError` | Missing API key, invalid options, unsupported method, closed client. |
| `CaptureKitSerializationError` | A required parameter is missing or a value can't be sent. |
| `CaptureKitTransportError` | Network failure or timeout. |
| `CaptureKitAPIError` | Non-2xx status (`status`, `error_message`, `response_body`, `raw_response`). |
| `CaptureKitResponseDecodingError` | A success response could not be decoded. |

All of them extend `CaptureKitError`.

## Retries

Requests are retried up to 3 times after a network error, a `408`, `500`, `502`, `503` or `504`, or a rate limit — which the API returns as `401` (or `429`) with a `Rate limit exceeded` message. Per-key quota errors (`…: quota daily`) are not retried, nor are `400`, `402`, `404` or client-side timeouts. The delay starts at 1 second and grows 1.5× per retry (capped at 30 seconds); a `Retry-After` header wins.

```python
client = CaptureKitClient(max_retries=5, retry_delay=0.5)

# or for one request
client.content(url="https://example.com", request_options=RequestOptions(max_retries=0))
```

## Batch requests

`batch()` runs a function per item on 10 threads (`concurrency`) and returns one `BatchResult` per item, in input order. A failing item never stops the others. `AsyncCaptureKitClient.batch()` does the same with `asyncio`.

```python
inputs = ["https://example.com", "https://www.capturekit.dev", "https://github.com"]
results = client.batch(inputs, lambda url: client.content(url=url), concurrency=5)

for result in results:
    if result.ok:
        print(result.value.data)
    else:
        print(inputs[result.index], result.error)
```

| Constant | Default | Description |
| --- | --- | --- |
| `DEFAULT_CONCURRENCY` | `10` | Tasks run at the same time by batch |
| `DEFAULT_TIMEOUT` | `120.0` | Request timeout (seconds) |
| `MAX_RETRIES` | `3` | Retry attempts after a network error, a 408/5xx or a rate limit |
| `RETRY_BACKOFF_FACTOR` | `1.5` | Exponential backoff multiplier |
| `DEFAULT_RETRY_DELAY` | `1.0` | Delay before the first retry (seconds) |

## Timeouts and custom HTTPX clients

```python
import httpx

from capturekit import CaptureKitClient, RequestOptions

client = CaptureKitClient(timeout=60)  # seconds, default 120, None disables
client.content(url="https://example.com", request_options=RequestOptions(timeout=30))

# Bring your own HTTPX client (proxies, limits, event hooks…). You keep ownership of it.
http_client = httpx.Client(proxy="http://localhost:8080")
client = CaptureKitClient(http_client=http_client)
```

## Endpoints

7 methods, generated from the [OpenAPI document](https://app.capturekit.dev/openapi).

| Method | HTTP | Description |
| --- | --- | --- |
| `analyze()` | GET / POST `/v1/analyze` | AI Content API analyzes any webpage and returns AI insights summary, value proposition, features, categories, use cases, and optional conta… |
| `capture()` | GET / POST `/v1/capture` | Browser-like Screenshot API that captures webpages as PNG/JPEG/WebP or PDF for previews, QA, reporting, monitoring, and archiving no headle… |
| `content()` | GET / POST `/v1/content` | CaptureKit Content API extracts structured webpage data, metadata, links, HTML/Markdown: in one request for SEO, monitoring, indexing and a… |
| `jobs()` | GET `/v1/jobs/{id}` | Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: Completed… |
| `stats()` | GET `/v1/stats` | Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 mea… |
| `usage()` | GET `/v1/usage` | Retrieve real-time usage statistics and credit balance for your CaptureKit account. |
| `website_crawler()` | GET / POST `/v1/website/crawler` | Website Crawler API fetches raw HTML from any webpage in request mode (no rendering) for fast scraping, audits, monitoring, and link/metada… |

## License

MIT — see [LICENSE](LICENSE).
