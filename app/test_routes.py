import pytest
from routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Flask Application!" in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Page" in response.data