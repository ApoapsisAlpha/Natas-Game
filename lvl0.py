import requests
import re

username = 'natas0'
password = 'natas0'

url = f'http://{username}.natas.labs.overthewire.org/'

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall('<!--The password for natas1 is (.*) -->', content)[0])