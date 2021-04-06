# 이건 혼자 연습한거

import requests
from bs4 import BeautifulSoup

url = "https://saywoo.github.io/saywoo/"
ret = requests.get(url)
soup = BeautifulSoup(ret.text, 'html.parser')
h2 = soup.find('h2')
h3 = soup.find_all('h3')
print(h2.text)

for i in h3:
    print(i.text)