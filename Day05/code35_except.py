# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
#원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지 마세요')
#     exit()

print('계산 테스트')

# try:
#     print(div(x, y)) # 예외 시 pass가 되어 오류 발생 x
# except:
#     print('나누기실패 : 0으로 나누려고 했습니다.')

try:
    print(div(x, y)) 
#except ZeroDivisionError as e: # except 여러개 사용하지 않아도 된다
#    print('0으로 나누면 안되요!')
except Exception as e:
    print(e)

print(add(x, y))
print(mul(x, y))