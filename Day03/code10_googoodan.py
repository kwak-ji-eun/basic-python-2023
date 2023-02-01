# 구구단 프로그램
for x in range(2, 10): # 이중 for문 사용하여 구구단 
    for y in range(1, 10):
        print(f'{x} X {y} = {x*y}') 
        # print(x, 'x', y, '=', x*y)

for x in range(2, 10): # 이중 for문 사용하여 구구단 
    for y in range(1, 10):
        print(f'{x} X {y} = {x*y}', end=' ') # 한줄로 간단하게 표현 end=' '
    
    print() # 깔끔하게 출력

for x in range(2, 10): # 이중 for문 사용하여 구구단
    print(f'{x}단 시작 ======')
    for y in range(1, 10):
        print(f'{x} X {y} = {x*y:>2}', end=' ') # {x*y:>2} 깔끔한 배열로 출력
    
    print() # 깔끔하게 출력