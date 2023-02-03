# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)
print(res.status) # 200은 잘 수신했다는 뜻 / 404는 제대로 못받음

