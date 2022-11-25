import requests

r = requests.post("http://127.0.0.1:8000/person",data={
    "first_name": "123",
    "last_name": "13123",
    "email":"ased"
})
if r.status_code != 201:
    exit(r.status_code)