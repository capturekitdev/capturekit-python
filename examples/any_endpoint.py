"""Call any path with request() and handle API errors."""

from capturekit import CaptureKitAPIError, CaptureKitClient, JsonResponse

with CaptureKitClient() as client:  # reads CAPTUREKIT_API_KEY
    try:
        response = client.request("GET", "/v1/usage")
        if isinstance(response, JsonResponse):
            print(response.data)
    except CaptureKitAPIError as error:
        print(f"HTTP {error.status}: {error}")
