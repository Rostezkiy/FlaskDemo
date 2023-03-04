import requests

res = requests.delete("http://127.0.0.1:5000/api/archive/7", json={"name": "Kitty", "photos": 77, "videos": 99})
print(res)
print(res.json())
