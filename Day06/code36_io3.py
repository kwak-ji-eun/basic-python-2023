# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)
print('1. Hello.\r\nWorld') 
print('2. Hello.\nWorld') # \r, \n 같기 때문에 \n만쓰자 (권장)

print('3. Hello.\n\tWorld') # t:탭
print('4. Hello.\n\t\bWorld') # b:백스페이스

print('5. Hello.\n\'World\'') # '\' 문자열내 홑따옴표
print('6. Hello. "World"')
print('7. Hello. \"World\"')

print('8. Hello. \\ World') # \를 문자열에 표현
print('9.Hello\0')

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작
me = '저'
name = '곽지은'
age = 24
print('%s는 %s입니다. %d입니다.' % (me, name, age))

print(f'{254.112233:.2f}') # 최신식

print('%4.4f' %(254.1142233)) # 구식 전체자리수.소수점


