import requests

api_url = 'http://localhost:5000/api'

response = requests.get(api_url)
print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)
print(response.json())


api_url = 'http://localhost:5000/api'
todo = {"userId":1,"title":"buy milk","complete":False}
response = requests.post(api_url, json=todo)
print(response.status_code)
print(response.text)

