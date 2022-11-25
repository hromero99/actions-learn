import requests

r = requests.post("http://127.0.0.1:8000/person",data={
    "first_name": "123",
    "last_name": "13123",
    "email":"ased"
})
print(r.status_code)
if int(r.status_code) != 201 or int(r.status_code) != 200:
    exit(1)
exit(0)