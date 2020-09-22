from fastapi.testclient import testclient 

from app.main import app

client = TestClient(app)

def test_docs():
    responses = client.get('/')
    assert response.status_code = 200
    assert response.headers['content-type'].startswith('text/html')