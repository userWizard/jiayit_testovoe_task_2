import pytest
from fastapi.testclient import TestClient
from httpx import HTTPStatusError
from src.application.api.users import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_get_user_success(mocker):
    mock_response = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    mocker.patch('httpx.AsyncClient.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    response = client.post("/user", json={"user_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_get_user_not_found(mocker):
    mocker.patch('httpx.AsyncClient.get', side_effect=HTTPStatusError("Not Found", request=None, response=mocker.Mock(status_code=404)))

    response = client.post("/user", json={"user_id": 9999})
    assert response.status_code == 404
    assert response.json() == {"error": "Not Found"}
