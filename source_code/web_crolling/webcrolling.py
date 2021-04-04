import requests
from bs4 import BeautifulSoup

url = "https://saywoo.github.io/saywoo/"
ret = requests.get(url)
soup = BeautifulSoup(ret.text, 'html.parser')
print(soup.head.title.text)
h2 = soup.find('h2')
print(h2.get_text())