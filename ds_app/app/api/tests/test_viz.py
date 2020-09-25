from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success for valid 2 character location for the airbnb optimal price rates."""
    response = client.get('/viz/IL')
    assert response.status_code == 200
    assert 'Illinois Airbnb Optimal Price Rates' in response.text


def test_invalid_input():
    """Return 404 if the endpoint isn't valid locations."""
    response = client.get('/viz/ZZ')
    body = response.json()
    assert response.status_code == 404
    assert body['detail'] == 'Location ZZ not found'
