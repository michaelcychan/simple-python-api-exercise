import requests

response = requests.get('http://www.boredapi.com/api/activity/')
print(response.status_code)
print(response.text)
data = response.json()
print(data['activity'])