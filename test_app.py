
import pytest
import requests

def test_home():
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, World!"
