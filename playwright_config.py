import os

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8000")

PLAYWRIGHT_SETTINGS = {
    "base_url": BASE_URL,
    "browser_name": "chromium",
    "headless": True,
    "slowmo": 0,
}
