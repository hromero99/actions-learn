import requests

status_code = 1
r = requests.post("http://127.0.0.1:8000/person",data={
    
})
print(r.status_code)
if int(r.status_code) == 200 or int(r.status_code) == 201:
    status_code = 0
exit(status_code)