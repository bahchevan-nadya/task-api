from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_create_task():
    responce = client.post(
        '/tasks',
        json={
            "title": "Test 1",
            "description": "Test description"
        })
    assert responce.status_code == 201
    data = responce.json()
    assert data["title"] == "Test 1"
    assert data["description"] == "Test description"
    assert data["status"] == "new"