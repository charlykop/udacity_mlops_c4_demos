import requests
import json

data = {"value": 5}
r = requests.post("http://127.0.0.1:8000/3?query=3", data=json.dumps(data))

print(r.json())