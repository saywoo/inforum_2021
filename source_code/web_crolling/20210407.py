import requests
from bs4 import BeautifulSoup
# 아까전에 다운받았던거 import해주기

word = input()
# 단어 하나 입력받기

url = "https://dic.daum.net/search.do?q=" + word
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

print(soup)