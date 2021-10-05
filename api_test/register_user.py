import requests

#POST
data_payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

print(type(data_payload))

resp = requests.post("https://reqres.in/api/register", data=data_payload)
print(resp)

print(resp.json())

print(resp.json()['token'])

