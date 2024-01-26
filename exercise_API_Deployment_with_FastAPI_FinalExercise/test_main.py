from fastapi.testclient import TestClient
import json

# Import app
from main import app

# Intantiate testing client
client = TestClient(app)

# Test success
def test_sucess():
    data = json.dumps({"feature_1": 3, "feature_2": "123"})
    r = client.post("/data/", data=data)
    assert r.status_code == 200

# Test execption feature_1
def test_exeption_feature_1():
    data = json.dumps({"feature_1": -3, "feature_2": "123"})
    r = client.post("/data/", data=data)
    assert r.status_code == 422