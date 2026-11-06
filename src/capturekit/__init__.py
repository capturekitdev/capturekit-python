"""Official Python SDK for the CaptureKit API."""

from ._endpoints import ENDPOINTS
from ._version import __version__
from .client import (
    DEFAULT_BASE_URL,
    DEFAULT_CONCURRENCY,
    DEFAULT_RETRY_DELAY,
    DEFAULT_TIMEOUT,
    MAX_RETRIES,
    RETRY_BACKOFF_FACTOR,
    AsyncCaptureKitClient,
    CaptureKitClient,
)
from .errors import (
    CaptureKitAPIError,
    CaptureKitConfigurationError,
    CaptureKitError,
    CaptureKitJobTimeoutError,
    CaptureKitResponseDecodingError,
    CaptureKitSerializationError,
    CaptureKitTransportError,
)
from .models import (
    APIResponse,
    BatchResult,
    BinaryResponse,
    EndpointDefinition,
    HTTPMethod,
    JsonResponse,
    RawResponse,
    RequestOptions,
)

__all__ = [
    "APIResponse",
    "AsyncCaptureKitClient",
    "BatchResult",
    "BinaryResponse",
    "DEFAULT_BASE_URL",
    "DEFAULT_CONCURRENCY",
    "DEFAULT_RETRY_DELAY",
    "DEFAULT_TIMEOUT",
    "MAX_RETRIES",
    "RETRY_BACKOFF_FACTOR",
    "ENDPOINTS",
    "EndpointDefinition",
    "HTTPMethod",
    "JsonResponse",
    "RawResponse",
    "RequestOptions",
    "CaptureKitAPIError",
    "CaptureKitClient",
    "CaptureKitConfigurationError",
    "CaptureKitError",
    "CaptureKitJobTimeoutError",
    "CaptureKitResponseDecodingError",
    "CaptureKitSerializationError",
    "CaptureKitTransportError",
    "__version__",
]
