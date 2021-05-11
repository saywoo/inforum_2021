#필요한 모듈 import 하기
import requests
import json

#이용할 api url을 변수에 저장해놓기
url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
#부여받은 api key값을 입력해서 변수에 저장해놓기
rest_api_key = 'bc4a2926795316221cc9c511c19e9a83'

#request를 할때 필요한 정보들을 headers 라는 변수에 저장해놓기(이거는 그냥 따라하면 됨)
headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

#음성을 인식하기 위한 wav 파일을 열기 
with open("heykakao.wav", 'rb') as fp:
    audio = fp.read()

#api를 호출해서 결과값을 res라는 변수에 저장해놓기
res = requests.post(url, headers=headers, data=audio)

#api의 호출 결과값을 출력하기 (json의 형태)
#print(res.text)

#json의 형태에서 결과값만 추출해서 출력하기
result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
result = json.loads(result_json_string)
print(result['value'])