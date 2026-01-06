import requests


def test_health_api(app_server):
    resp = requests.get(f"{app_server}/api/health", timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


def test_video_metadata_api(app_server):
    resp = requests.get(f"{app_server}/api/video-metadata", timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "sample.mp4"
    assert "duration" in data
