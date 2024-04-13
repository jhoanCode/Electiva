# test_app.py
from app import app

import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data
