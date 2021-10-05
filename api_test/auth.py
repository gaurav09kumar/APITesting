import requests

resp = requests.get("http://the-internet.herokuapp.com/basic_auth", auth=('admin', 'admin'))

print(resp.status_code)

resp2 = requests.get("http://the-internet.herokuapp.com/basic_auth", auth=('admin', 'xyz'))

print(resp2.status_code)
