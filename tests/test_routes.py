"""Unit tests for Flask routes using pytest"""

import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client


def test_routes(client):
    """Test the /add/michael route greeting."""
    response = client.get('/add/michael')
    assert response.status_code == 200
    html = response.data.decode()
    assert "hello, michael!" in html.lower()
    assert "michael@kean.edu" in html.lower()
