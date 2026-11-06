"""Generated from the CaptureKit OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from .models import EndpointDefinition

ENDPOINTS: dict[str, EndpointDefinition] = {
    "analyze": EndpointDefinition(
        path="/v1/analyze",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("url",),
    ),
    "capture": EndpointDefinition(
        path="/v1/capture",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("url",),
    ),
    "content": EndpointDefinition(
        path="/v1/content",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("url",),
    ),
    "jobs": EndpointDefinition(
        path="/v1/jobs/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "stats": EndpointDefinition(
        path="/v1/stats",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "usage": EndpointDefinition(
        path="/v1/usage",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "website_crawler": EndpointDefinition(
        path="/v1/website/crawler",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("query",),
    ),
}
