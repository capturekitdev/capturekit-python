"""Save a binary response to a file."""

import os

from capturekit import BinaryResponse, CaptureKitClient

with CaptureKitClient(os.environ["CAPTUREKIT_API_KEY"]) as client:
    response = client.capture(url="https://example.com", format="png")
    if isinstance(response, BinaryResponse):
        with open("screenshot.png", "wb") as file:
            file.write(response.bytes)
        print(f"Saved screenshot.png ({response.content_type}, {len(response.bytes)} bytes)")
    else:
        print(response.data)
