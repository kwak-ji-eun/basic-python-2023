# 자동차 클래스
class Car:
    __number = '54라 9538'

    def get_number(self) -> str:
        return self.__number

    #클래스 외부에선 변경 x, 
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '54라 9538') -> None:
        print('__init__')
        self.__number = number

    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # 부모클래스(상속)
    
    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999'
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555') # 내부함수 사용하여 바꼈다.
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는요 아이오닉이고, 번호가 {mycar.get_number()}')

mycar.__number = '132거 8874'
print(mycar.__number)
print(mycar)
