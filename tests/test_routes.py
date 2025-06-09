import pytest
from app.server import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["REDIS_URL"] = "redis://localhost:6379/1"
    return app.test_client()

def test_set_and_get_cache(client):
    resp = client.post("/cache/test", json={"value": "abc"})
    assert resp.status_code == 201
    resp2 = client.get("/cache/test")
    assert resp2.json == {"value": "abc"}
