"""Generated from the CaptureKit OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal, cast

from .models import APIResponse, JsonResponse, RequestOptions


class _SyncOperations:
    """Generated CaptureKit endpoint methods."""

    __slots__ = ()

    def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    def analyze(
        self,
        *,
        url: str,
        custom_response: str | None = None,
        custom_prompt: str | None = None,
        proxy: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Analyze (AI). AI Content API analyzes any webpage and returns AI insights summary, value proposition, features, categories, use cases, and optional contact signals. Credit cost: 1 credit per call.

        ``GET / POST /v1/analyze``

        Args:
            url: The URL of the webpage to capture.
            custom_response: Pass custom response fields to be included in the AI response.
            custom_prompt: Add your own instructions to guide the AI’s analysis.
            proxy: Specify a proxy server to route your request through.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "analyze",
                {
                    "url": url,
                    "custom_response": custom_response,
                    "custom_prompt": custom_prompt,
                    "proxy": proxy,
                    "cache": cache,
                    "cache_ttl": cache_ttl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def capture(
        self,
        *,
        url: str,
        format: Literal["jpeg", "jpg", "pdf", "png", "webp"] | str | None = None,
        device: Literal[
            "galaxy_fold4",
            "galaxy_s23",
            "galaxy_s23_ultra",
            "galaxy_s8",
            "huawei_mate_50_pro",
            "huawei_p60_pro",
            "ipad",
            "iphone_12",
            "iphone_13_mini",
            "iphone_13_pro_max",
            "iphone_14_pro",
            "iphone_14_pro_max",
            "iphone_x",
            "pixel_5",
            "pixel_6a",
            "pixel_7_pro",
            "redmi_note_11",
            "redmi_note_12_pro",
        ]
        | str
        | None = None,
        full_page: bool | None = None,
        full_page_scroll: bool | None = None,
        full_page_scroll_duration: int | float | None = None,
        viewport_width: int | float | None = None,
        viewport_height: int | float | None = None,
        scale_factor: int | float | None = None,
        image_quality: str | None = None,
        selector: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        s3_secret_key: str | None = None,
        s3_access_key_id: str | None = None,
        s3_bucket: str | None = None,
        s3_object_key: str | None = None,
        s3_region: str | None = None,
        storage_endpoint: str | None = None,
        s3_url: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Capture (Screenshot). Browser-like Screenshot API that captures webpages as PNG/JPEG/WebP or PDF for previews, QA, reporting, monitoring, and archiving no headless setup. Credit cost: 1 credit per call.

        ``GET / POST /v1/capture``

        Args:
            url: The URL of the webpage to capture. Examples:  https://www.amazon.com/s?k=pokemon
            format: The output format of the screenshot.
            device: The device type to emulate for the screenshot.
            full_page: Capture the entire page instead of just the visible viewport.
            full_page_scroll: Scroll the page to fully load lazy-loaded elements before capturing a full-page screenshot.
            full_page_scroll_duration: Time in milliseconds for scrolling before capturing the full page.
            viewport_width: The width of the browser viewport in pixels.
            viewport_height: The height of the browser viewport in pixels.
            scale_factor: The scale factor for high-resolution screenshots.
            image_quality: Generate images with custom quality settings.
            selector: Capture a specific element on the page instead of the full viewport.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            remove_selectors: A comma-separated list of elements to hide before capturing (e.g., ads, popups).
            remove_cookie_banners: Automatically remove cookie banners before capturing.
            remove_ads: Automatically remove ads before capturing.
            block_resources: Comma-separated list of resource types to block (e.g., “image,stylesheet,font”).
            block_urls: Comma-separated list of URL patterns to block (e.g., “analytics,tracking,advertisement”).
            delay: Delay in seconds before capturing the screenshot.
            wait_until: Define when to capture.
            wait_for_selector: Wait for a specific element to appear before taking the screenshot.
            proxy: Specify a proxy server to route your request through.
            s3_secret_key: AWS S3 secret access key.
            s3_access_key_id: AWS S3 access key ID.
            s3_bucket: The S3 bucket name where the screenshot will be uploaded.
            s3_object_key: The filename for the S3 object (auto-generated if not provided).
            s3_region: AWS S3 region for storage.
            storage_endpoint: Leave this field empty for AWS S3. Only specify a value if required. S3-compatible storage services are supported, for example, use https://<accountId>.r2.cloudflarestorage.com for Cloudflare R2.
            s3_url: Use S3 storage for screenshots. The S3 URL will be returned in the response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "capture",
            {
                "url": url,
                "format": format,
                "device": device,
                "full_page": full_page,
                "full_page_scroll": full_page_scroll,
                "full_page_scroll_duration": full_page_scroll_duration,
                "viewport_width": viewport_width,
                "viewport_height": viewport_height,
                "scale_factor": scale_factor,
                "image_quality": image_quality,
                "selector": selector,
                "cache": cache,
                "cache_ttl": cache_ttl,
                "remove_selectors": remove_selectors,
                "remove_cookie_banners": remove_cookie_banners,
                "remove_ads": remove_ads,
                "block_resources": block_resources,
                "block_urls": block_urls,
                "delay": delay,
                "wait_until": wait_until,
                "wait_for_selector": wait_for_selector,
                "proxy": proxy,
                "s3_secret_key": s3_secret_key,
                "s3_access_key_id": s3_access_key_id,
                "s3_bucket": s3_bucket,
                "s3_object_key": s3_object_key,
                "s3_region": s3_region,
                "storage_endpoint": storage_endpoint,
                "s3_url": s3_url,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def content(
        self,
        *,
        url: str,
        include_html: bool | None = None,
        include_markdown: bool | None = None,
        include_sitemap: bool | None = None,
        use_defuddle: bool | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Content. CaptureKit Content API extracts structured webpage data, metadata, links, HTML/Markdown: in one request for SEO, monitoring, indexing and automation. Credit cost: 1 credit per call.

        ``GET / POST /v1/content``

        Args:
            url: The URL of the webpage to capture.
            include_html: Include the raw HTML of the webpage in the response.
            include_markdown: Include the Markdown of the webpage in the response.
            include_sitemap: Include the sitemap of the website in the response.
            use_defuddle: Use Defuddle to clean and extract the main content from web pages. This popular library removes unnecessary elements like comments, sidebars, headers, footers, and other non-essential elements, leavi…
            remove_selectors: A comma-separated list of elements to hide before capturing (e.g., ads, popups).
            remove_cookie_banners: Automatically remove cookie banners before capturing.
            remove_ads: Automatically remove ads before capturing.
            block_resources: Comma-separated list of resource types to block (e.g., “image,stylesheet,font”).
            block_urls: Comma-separated list of URL patterns to block (e.g., “analytics,tracking,advertisement”).
            delay: Delay in seconds before capturing the screenshot.
            wait_until: Define when to capture.
            wait_for_selector: Wait for a specific element to appear before taking the screenshot.
            proxy: Specify a proxy server to route your request through.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "content",
                {
                    "url": url,
                    "include_html": include_html,
                    "include_markdown": include_markdown,
                    "include_sitemap": include_sitemap,
                    "use_defuddle": use_defuddle,
                    "remove_selectors": remove_selectors,
                    "remove_cookie_banners": remove_cookie_banners,
                    "remove_ads": remove_ads,
                    "block_resources": block_resources,
                    "block_urls": block_urls,
                    "delay": delay,
                    "wait_until": wait_until,
                    "wait_for_selector": wait_for_selector,
                    "proxy": proxy,
                    "cache": cache,
                    "cache_ttl": cache_ttl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, self._call("jobs", {"id": id}, request_options))

    def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example capture. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/capture. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse, self._call("stats", {"engine": engine, "path": path}, request_options)
        )

    def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your CaptureKit account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, self._call("usage", {}, request_options))

    def website_crawler(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Website Crawler. Website Crawler API fetches raw HTML from any webpage in request mode (no rendering) for fast scraping, audits, monitoring, and link/metadata extraction. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/crawler``

        Args:
            query: A website URL with either the http or https protocol.
            allow_redirects: If set to false, do not follow redirects.
            return_page_source: If set to true, the response will be the HTML source of the page.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "website_crawler",
            {
                "query": query,
                "allow_redirects": allow_redirects,
                "return_page_source": return_page_source,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )


class _AsyncOperations:
    """Generated CaptureKit endpoint methods."""

    __slots__ = ()

    async def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    async def analyze(
        self,
        *,
        url: str,
        custom_response: str | None = None,
        custom_prompt: str | None = None,
        proxy: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Analyze (AI). AI Content API analyzes any webpage and returns AI insights summary, value proposition, features, categories, use cases, and optional contact signals. Credit cost: 1 credit per call.

        ``GET / POST /v1/analyze``

        Args:
            url: The URL of the webpage to capture.
            custom_response: Pass custom response fields to be included in the AI response.
            custom_prompt: Add your own instructions to guide the AI’s analysis.
            proxy: Specify a proxy server to route your request through.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "analyze",
                {
                    "url": url,
                    "custom_response": custom_response,
                    "custom_prompt": custom_prompt,
                    "proxy": proxy,
                    "cache": cache,
                    "cache_ttl": cache_ttl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def capture(
        self,
        *,
        url: str,
        format: Literal["jpeg", "jpg", "pdf", "png", "webp"] | str | None = None,
        device: Literal[
            "galaxy_fold4",
            "galaxy_s23",
            "galaxy_s23_ultra",
            "galaxy_s8",
            "huawei_mate_50_pro",
            "huawei_p60_pro",
            "ipad",
            "iphone_12",
            "iphone_13_mini",
            "iphone_13_pro_max",
            "iphone_14_pro",
            "iphone_14_pro_max",
            "iphone_x",
            "pixel_5",
            "pixel_6a",
            "pixel_7_pro",
            "redmi_note_11",
            "redmi_note_12_pro",
        ]
        | str
        | None = None,
        full_page: bool | None = None,
        full_page_scroll: bool | None = None,
        full_page_scroll_duration: int | float | None = None,
        viewport_width: int | float | None = None,
        viewport_height: int | float | None = None,
        scale_factor: int | float | None = None,
        image_quality: str | None = None,
        selector: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        s3_secret_key: str | None = None,
        s3_access_key_id: str | None = None,
        s3_bucket: str | None = None,
        s3_object_key: str | None = None,
        s3_region: str | None = None,
        storage_endpoint: str | None = None,
        s3_url: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Capture (Screenshot). Browser-like Screenshot API that captures webpages as PNG/JPEG/WebP or PDF for previews, QA, reporting, monitoring, and archiving no headless setup. Credit cost: 1 credit per call.

        ``GET / POST /v1/capture``

        Args:
            url: The URL of the webpage to capture. Examples:  https://www.amazon.com/s?k=pokemon
            format: The output format of the screenshot.
            device: The device type to emulate for the screenshot.
            full_page: Capture the entire page instead of just the visible viewport.
            full_page_scroll: Scroll the page to fully load lazy-loaded elements before capturing a full-page screenshot.
            full_page_scroll_duration: Time in milliseconds for scrolling before capturing the full page.
            viewport_width: The width of the browser viewport in pixels.
            viewport_height: The height of the browser viewport in pixels.
            scale_factor: The scale factor for high-resolution screenshots.
            image_quality: Generate images with custom quality settings.
            selector: Capture a specific element on the page instead of the full viewport.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            remove_selectors: A comma-separated list of elements to hide before capturing (e.g., ads, popups).
            remove_cookie_banners: Automatically remove cookie banners before capturing.
            remove_ads: Automatically remove ads before capturing.
            block_resources: Comma-separated list of resource types to block (e.g., “image,stylesheet,font”).
            block_urls: Comma-separated list of URL patterns to block (e.g., “analytics,tracking,advertisement”).
            delay: Delay in seconds before capturing the screenshot.
            wait_until: Define when to capture.
            wait_for_selector: Wait for a specific element to appear before taking the screenshot.
            proxy: Specify a proxy server to route your request through.
            s3_secret_key: AWS S3 secret access key.
            s3_access_key_id: AWS S3 access key ID.
            s3_bucket: The S3 bucket name where the screenshot will be uploaded.
            s3_object_key: The filename for the S3 object (auto-generated if not provided).
            s3_region: AWS S3 region for storage.
            storage_endpoint: Leave this field empty for AWS S3. Only specify a value if required. S3-compatible storage services are supported, for example, use https://<accountId>.r2.cloudflarestorage.com for Cloudflare R2.
            s3_url: Use S3 storage for screenshots. The S3 URL will be returned in the response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "capture",
            {
                "url": url,
                "format": format,
                "device": device,
                "full_page": full_page,
                "full_page_scroll": full_page_scroll,
                "full_page_scroll_duration": full_page_scroll_duration,
                "viewport_width": viewport_width,
                "viewport_height": viewport_height,
                "scale_factor": scale_factor,
                "image_quality": image_quality,
                "selector": selector,
                "cache": cache,
                "cache_ttl": cache_ttl,
                "remove_selectors": remove_selectors,
                "remove_cookie_banners": remove_cookie_banners,
                "remove_ads": remove_ads,
                "block_resources": block_resources,
                "block_urls": block_urls,
                "delay": delay,
                "wait_until": wait_until,
                "wait_for_selector": wait_for_selector,
                "proxy": proxy,
                "s3_secret_key": s3_secret_key,
                "s3_access_key_id": s3_access_key_id,
                "s3_bucket": s3_bucket,
                "s3_object_key": s3_object_key,
                "s3_region": s3_region,
                "storage_endpoint": storage_endpoint,
                "s3_url": s3_url,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def content(
        self,
        *,
        url: str,
        include_html: bool | None = None,
        include_markdown: bool | None = None,
        include_sitemap: bool | None = None,
        use_defuddle: bool | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Content. CaptureKit Content API extracts structured webpage data, metadata, links, HTML/Markdown: in one request for SEO, monitoring, indexing and automation. Credit cost: 1 credit per call.

        ``GET / POST /v1/content``

        Args:
            url: The URL of the webpage to capture.
            include_html: Include the raw HTML of the webpage in the response.
            include_markdown: Include the Markdown of the webpage in the response.
            include_sitemap: Include the sitemap of the website in the response.
            use_defuddle: Use Defuddle to clean and extract the main content from web pages. This popular library removes unnecessary elements like comments, sidebars, headers, footers, and other non-essential elements, leavi…
            remove_selectors: A comma-separated list of elements to hide before capturing (e.g., ads, popups).
            remove_cookie_banners: Automatically remove cookie banners before capturing.
            remove_ads: Automatically remove ads before capturing.
            block_resources: Comma-separated list of resource types to block (e.g., “image,stylesheet,font”).
            block_urls: Comma-separated list of URL patterns to block (e.g., “analytics,tracking,advertisement”).
            delay: Delay in seconds before capturing the screenshot.
            wait_until: Define when to capture.
            wait_for_selector: Wait for a specific element to appear before taking the screenshot.
            proxy: Specify a proxy server to route your request through.
            cache: Cache the response.
            cache_ttl: Cache the response for a custom TTL (in seconds).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "content",
                {
                    "url": url,
                    "include_html": include_html,
                    "include_markdown": include_markdown,
                    "include_sitemap": include_sitemap,
                    "use_defuddle": use_defuddle,
                    "remove_selectors": remove_selectors,
                    "remove_cookie_banners": remove_cookie_banners,
                    "remove_ads": remove_ads,
                    "block_resources": block_resources,
                    "block_urls": block_urls,
                    "delay": delay,
                    "wait_until": wait_until,
                    "wait_for_selector": wait_for_selector,
                    "proxy": proxy,
                    "cache": cache,
                    "cache_ttl": cache_ttl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, await self._call("jobs", {"id": id}, request_options))

    async def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example capture. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/capture. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse,
            await self._call("stats", {"engine": engine, "path": path}, request_options),
        )

    async def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your CaptureKit account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, await self._call("usage", {}, request_options))

    async def website_crawler(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Website Crawler. Website Crawler API fetches raw HTML from any webpage in request mode (no rendering) for fast scraping, audits, monitoring, and link/metadata extraction. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/crawler``

        Args:
            query: A website URL with either the http or https protocol.
            allow_redirects: If set to false, do not follow redirects.
            return_page_source: If set to true, the response will be the HTML source of the page.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "website_crawler",
            {
                "query": query,
                "allow_redirects": allow_redirects,
                "return_page_source": return_page_source,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )
