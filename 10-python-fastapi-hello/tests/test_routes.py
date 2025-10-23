from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_hello_default():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json()["message"].startswith("Hello,")

def test_hello_name():
    r = client.get("/hello", params={"name": "Valentin"})
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, Valentin"}

def test_metrics():
    client.get("/hello")
    m = client.get("/metrics")
    assert m.status_code == 200
    assert "http_requests_total" in m.text
