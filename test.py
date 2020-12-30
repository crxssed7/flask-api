import requests

BASE = "http://127.0.0.1:5000/"

# Make a record
response = requests.put(BASE + "video/1", {"name":"video name", "views":100, "likes": 10})
print(response.json())

input()

# Show that record
response = requests.get(BASE + "video/1")
print(response.json())

input()

# Delete that record
response = requests.delete(BASE + "video/1")
print(response)

input()

## Show that 
response = requests.get(BASE + "video/1")
print(response.json())