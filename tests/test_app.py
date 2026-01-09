"""Unit tests for Flask application."""
import pytest
from app import app

@pytest.fixture
def client():
    """Create test client for Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home endpoint returns correct response."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello from Flask in Docker!' in response.data

def test_health_endpoint(client):
    """Test health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_health_returns_json(client):
    """Test health endpoint returns JSON content type."""
    response = client.get('/health')
    assert response.content_type == 'application/json'

def test_nonexistent_endpoint(client):
    """Test 404 error for non-existent endpoint."""
    response = client.get('/doesnotexist')
    assert response.status_code == 404

