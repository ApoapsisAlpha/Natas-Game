import requests
import re

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = f'http://{username}.natas.labs.overthewire.org'

cookies = { 'data' : 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK' }

response = requests.post(url, auth = (username, password), cookies = cookies)
content = response.text

print(re.findall('The password for natas12 is (.*)<br>', content)[0])