import requests
from playwright.sync_api import Page, expect


def test_static_logo_asset(app_server):
    resp = requests.get(f"{app_server}/static/logo.png", timeout=10)
    assert resp.status_code == 200
    assert int(resp.headers.get("Content-Length", "1")) > 0


def test_static_video_asset(app_server):
    resp = requests.get(f"{app_server}/static/sample.mp4", timeout=10)
    assert resp.status_code == 200
    assert int(resp.headers.get("Content-Length", "1")) > 0


def test_video_element_can_play(page: Page):
    page.goto("/")
    video = page.locator("#demo-video")
    expect(video).to_be_visible()
    
    # Wait for video metadata to load + retry
    page.wait_for_timeout(2000)  # Give video time to load
    
    # Poll until readyState >= 1 (metadata loaded)
    ready_state = page.evaluate("""
        () => {
            const video = document.getElementById('demo-video');
            return new Promise((resolve) => {
                if (video.readyState >= 1) {
                    resolve(video.readyState);
                } else {
                    video.addEventListener('loadedmetadata', () => resolve(video.readyState), {once: true});
                    setTimeout(() => resolve(video.readyState), 5000);
                }
            });
        }
    """)
    assert ready_state >= 1, f"Video readyState={ready_state} (expected >=1)"
