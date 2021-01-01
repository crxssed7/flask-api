import requests

BASE = "http://192.168.0.48:5000/"

response = requests.get(BASE + "video/1")
print(response.json())