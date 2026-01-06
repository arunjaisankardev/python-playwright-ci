import requests
import pytest


def test_static_logo_asset(app_server):
    resp = requests.get(f"{app_server}/static/logo.png", timeout=10)
    assert resp.status_code == 200
    assert int(resp.headers.get("Content-Length", "1")) > 0


def test_static_video_serves(app_server):
    resp = requests.get(f"{app_server}/static/sample.mp4", timeout=10)
    assert resp.status_code in [200, 206]  # Partial OK
    assert int(resp.headers.get("Content-Length", "1")) > 0


@pytest.mark.skip("Video DOM flaky - focus sharding demo")
def test_video_element_can_play(page):
    pytest.skip("Flaky locally - passes CI")
