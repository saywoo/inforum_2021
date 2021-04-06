# 단어 하나를 입력하면 다음 사전을 크롤링해서 단어 뜻을 출력해주는 프로그램

# 라이브러리 import
import requests
from bs4 import BeautifulSoup

# 단어 하나를 입력받기
word = input()

# 다음 사전 url을 가져와서 파싱하기
url = "https://dic.daum.net/search.do?q=" + word
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# html 소스코드를 보고 단어의 뜻이 들어가있는 태그와 클래스를 찾아서 find 함수를 이용해 가져오기
mean_list = soup.find('div', class_='cleanword_type kuek_type')

# 만약 여기서 비어있으면 뜻이 없다는 뜻이므로 사전에 없는 단어라고 출력함
if not mean_list:
    print("사전에 없는 단어입니다")
# 아니면 계속 파싱하기
else:
    mean_list = mean_list.find_all('span', class_='txt_search')
    
    # 순서대로 출력하기
    for i in mean_list:
        print(i.text)