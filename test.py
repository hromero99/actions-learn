import requests

r = requests.post("http://127.0.0.1:8000/person",data={
    "first_name": "123",
    "last_name": "13123",
    "email":"ased"
})
print(r.status_code)
if int(r.status_code) == 201:
    exit(0)
exit(1)