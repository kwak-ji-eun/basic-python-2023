# 주소록앱
# 2023-02-06
# KJE
# 15-1 파일 없을 때 나는 예외
# 15-2 입력시 / 개수가 다를 때 예외
# 15-2 메뉴번호 입력 숫자외 예외


import os # 운영체제 모듈

class Contact:
    # 생성자 - 이름, 전번, 이멜, 주소
    def __init__(self,name, phone_num, email, addr) -> None:
        self.__name = name 
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}') 
        return str_res        

    # 10. 객체 존재여부 확인 클래스 함수
    def isNameExist(self, name):
        if self.__name == name: 
            return True
        else:
            return False

    # 12. 각 멤버번수 접근하는 함수
    # getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name

    def getPhoneNum(self) -> str:
        return self.__phone_num
    
    def getEmail(self) -> str:
        return self.__email

    def getAddr(self) -> str:
        return self.__addr

      
# 5. 사용자입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름/전번/이메일/주소 )').split('/')
    # print(name, phone_num, email, addr)
    # 7. Contact 객체 만들기 
    contact = Contact(name, phone_num, email, addr)
    return contact

# 9. 주소록출력
def get_contacts(list):
    for item in list:
        print(item)
        print('====================')
    
# 10. 주소록 삭제
def del_content(list, name):
    count = 0
    for i, item in enumerate(list): # 리스트 인덱스 추가생성 기능(enumerate(list) 사용하면 0, 1, ...번호가 한번더 나옴) 
       if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제
    if count > 0: # 11. 메시지 출력
        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 
def save_contacts(list):
    file = open('C:/Source/studyPython2023/Project/contacts.txt', 'w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')
    
    file.close() # 파일 닫아줘야 함!!

# 14. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/studyPython2023/Project/contacts.txt', 'r', encoding='utf-8')
    except Exception as e:
        f = open('C:/Source/studyPython2023/Project/contacts.txt', 'r', encoding='utf-8')
        f.close() # 파일이 없어서 생기는 예외는 파일생성하고 함수아웃
        return 


    while True:
        line = file.readline().replace('\n','') # 15. 문장끝 \n 제거
        if not line: break
        
        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)
    
    file.close

    
# 추가. 화면클리어
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'): # Window 운영체제라면                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        command = 'cls' # 윈도우 화면 클리어 명령어


# 6. 메뉴표시
def get_menu():
    str_menu = ('주소록앱 v0.5\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱종료')
    print(str_menu)
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        menu = 0 # 영문자, 특수문자넣으면 전부 0으로
        
    return menu

# 3. 전체실행
def run():
    contacts = list() # 주소를 담기위한 빈리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    # temp = Contact('곽지은', '010-8258-5440', 'snstkfkawldm@naver.com', '부산시 사상구...')
    # set_contact()


    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            try:
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공')
            except Exception as e:
                print('이름/전번/이메일/주소순으로 똑바로 입력하세요')
                input
            finally:
                clear_console()
        elif sel_menu == 2: # 9. 연락처 출력
            get_contacts(contacts)
            input('주소록 출력 완료') # 입력 기다리다가
            clear_console() # 화면 전환함
        elif sel_menu == 3: # 10. 연락처 삭제
            name = input('삭제할 이름 입력 : ')
            del_content(contacts, name)
            input()
            clear_console()
        elif sel_menu == 4: # 13. 종료시 주소록 파일 저장
            save_contacts(contacts)
            break
        else:
            clear_console()
    

# 1. 메인실행 영역
if __name__ == '__main__':
    print('주소록앱 시작합니다')
    run()
