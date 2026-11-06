"""Use the asyncio client."""

import asyncio

from capturekit import AsyncCaptureKitClient


async def main() -> None:
    async with AsyncCaptureKitClient() as client:  # reads CAPTUREKIT_API_KEY
        response = await client.content(url="https://example.com")
        print(response.data)


asyncio.run(main())
