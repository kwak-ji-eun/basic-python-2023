# 좀 더 복잡한 계산기
def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i
    elif option == 'mul':
        for i in args:
            result *= i
    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i

    return result       
#print(calc('add', 5, 7, 17)) #29
#print(calc('mul'512, 2, 2, 21))

 # 여러값을 리턴할 때
def new_calc(x, y):
    return (x*y)

