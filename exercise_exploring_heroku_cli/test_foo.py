from fastapi.testclient import TestClient

from foo import app

client = TestClient(app)

# Test status code
def test_response():
    r = client.get("/items/5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 5"}


# Test status code with query parameter
def test_response_with_query_parameter():
    r = client.get("/items/5?count=2")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 2 of 5"}


# Test wrong URL 
def test_wrong_url():
    r = client.get("/falsch")
    assert r.status_code != 200