# 파일 읽어오기
file = open('./Day05/sample05.txt','r', encoding = 'utf-8')

while True:
    text = file.read()
    
    if not text: break
    
    print(text)

file.close() # file open 시 반드시 close해야한다.