import requests

BASE = "http://127.0.0.1:5000/"

response = requests.delete(BASE + "video/3")
print(response)

input()

response = requests.get(BASE + "video/3")
print(response.json())