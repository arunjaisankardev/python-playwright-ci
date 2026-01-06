import requests
from playwright.sync_api import Page, expect


def test_static_logo_asset(app_server):
    resp = requests.get(f"{app_server}/static/logo.png", timeout=5)
    assert resp.status_code == 200
    assert int(resp.headers.get("Content-Length", "1")) > 0


def test_static_video_asset(app_server):
    resp = requests.get(f"{app_server}/static/sample.mp4", timeout=5)
    assert resp.status_code == 200
    assert int(resp.headers.get("Content-Length", "1")) > 0


def test_video_element_can_play(page: Page):
    page.goto("/")
    video = page.locator("#demo-video")
    expect(video).to_be_visible()
    ready_state = page.evaluate(
        "() => document.getElementById('demo-video').readyState"
    )
    assert ready_state >= 1
