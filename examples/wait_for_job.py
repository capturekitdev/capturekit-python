"""Start an async job and wait for its result."""

from capturekit import CaptureKitClient

with CaptureKitClient() as client:  # reads CAPTUREKIT_API_KEY
    submitted = client.content(url="https://example.com", is_async=True)
    job = client.wait_for_job(
        submitted.data["job_id"],
        on_progress=lambda j: print(j["status"], j.get("progress")),
    )
    print(job.data)
