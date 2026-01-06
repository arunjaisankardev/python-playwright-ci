import os
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright

from playwright_config import PLAYWRIGHT_SETTINGS  # from playwright.config.py


@pytest.fixture(scope="session", autouse=True)
def app_server():
    """Start the Flask app once for all tests."""
    port = int(os.environ.get("PORT", 8000)) + int(os.getpid()) % 100
    env = os.environ.copy()
    env["PORT"] = str(port)

    proc = subprocess.Popen(
        ["python", "-m", "app.main"],
        env=env,
    )

    # wait for server to start
    time.sleep(3)

    yield f"http://127.0.0.1:{port}"

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = getattr(
        playwright_instance, PLAYWRIGHT_SETTINGS["browser_name"]
    ).launch(
        headless=PLAYWRIGHT_SETTINGS["headless"],
        slow_mo=PLAYWRIGHT_SETTINGS["slowmo"],
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser, app_server):
    context = browser.new_context(base_url=app_server)
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Screenshot + video on failure."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        context = item.funcargs.get("context")
        if context:
            context.screenshot(path=f"test-results/screenshots/{item.name}.png")
            # Videos saved automatically by browser fixture


@pytest.fixture(scope="function")
def context(browser):
    """Fresh context per test with video."""
    context = browser.new_context(
        record_video_dir="test-results/videos/",
        record_har_path=f"test-results/traces/{pytest.current_test}.har",
    )
    yield context
    context.close()
