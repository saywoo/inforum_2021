import requests
from bs4 import BeautifulSoup

url = "https://saywoo.github.io/saywoo/"
ret = requests.get(url)

print(ret.text)