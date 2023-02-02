# 클래스 생성 # 객체는 함수와 변수의 집합!!
class Person: # 클래스를 정의할 때의 Person
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가 
    #def __init__(self):
    #    self.name = '홍길동'
    #   self.height = '170'
    #   self.gender = 'male'
    #   self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None: # 색이 연한 것 : 아직까지 한번도 사용하지 x / 밑에 self.name = name 써주면 색이 돌아옴
        self.name = name # 초기화 하는 것 
        self.height = height
        self.gender = gender 

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option): # 클래스 안에서의 함수는 self 필수
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')
    
    def stop():
        print('멈춥니다.')
    
    # 2. 생성자와 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 :  이름은 {self.name}, 성별은 {self.gender}'

jieun = Person('곽지은', 156, 'female') # 객채를 instance # 함수를 만들어라!(동사) Person
#jieun.name = '곽지은'
#jieun.height = '156'
#jieun.gender = 'female'
#jieun.blood_type = 'B'

print(f'{jieun.name}의 혈액형은 {jieun.blood_type}입니다.')

jieun.run('Fast')
print(jieun)

# 1. 초기화 후 객체생성
hong = Person('홍길동', 170, 'male')
hong.run('Slow')
print(jieun)


print('====================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
