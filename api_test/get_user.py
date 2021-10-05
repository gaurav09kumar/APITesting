import requests

resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)

print(type(resp))
print(dir(resp))

code = resp.status_code

assert code == 200, "Code doesnt match"

print(resp.text)  # returns data in unicode
print(resp.content)  # returns code in bytes format
print(resp.json())  # returns data in JSON encoded form. Serialized JSON

print(resp.headers)  #Get all the headers

print(resp.cookies)

print(resp.encoding)

print(resp.url)


json_response = resp.json()

print(json_response['total'])
#Validate
assert json_response['total'] == 12, "Total doesnt match"

print(json_response['total_pages'])
#Validate
assert json_response['total_pages'] == 2, "Total pages count doesnt match"

print(json_response['data'][0]['email'])
#Validate
assert (json_response['data'][0]['email']).endswith("reqres.in"), "Email doesnt match"

print(json_response['data'][2]['last_name'])
#Validate
assert (json_response['data'][2]['last_name']) != None, "Email doesnt match"

p = {'pages': 2}

resp2 = requests.get("https://reqres.in/api/users", params=p)

print(resp2.status_code)
print(resp2.url)

json_resp = resp2.json()
print(json_resp["support"]["url"])





