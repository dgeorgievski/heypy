from conftest import client
from heyapp import create_app

def test_config():
    assert not create_app().testing
    assert create_app('testing').testing

def test_request_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to HeyApp!" in response.data

def test_request_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert b"OK" in response.data
