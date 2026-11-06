"""Call the featured endpoint and print the JSON result."""

import json
import os

from capturekit import CaptureKitClient

with CaptureKitClient(os.environ["CAPTUREKIT_API_KEY"]) as client:
    response = client.content(url="https://example.com")
    print(json.dumps(response.data, indent=2))
