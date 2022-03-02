import requests

resp= requests.post("http://127.0.0.1:8000/home_cbv/")
print(resp.content)


