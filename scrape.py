import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup

url = 'http://www.google.com/search?q=nike+shoes'
fname = 'html_output.txt'

try:
    r = requests.get(url, timeout=0.075)
except Timeout:
    print('Request timeout!')
else:
    print('The request got executed.')
	
soup = BeautifulSoup(r.content, 'html.parser')

f = open(fname, 'w', encoding='utf-8')
f.write(soup)
f.close()
