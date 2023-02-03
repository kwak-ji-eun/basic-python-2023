# 다중입력 - 코테할 때 이거 사용

# x, y = input('두 영단어를 입력하세요>').split() # 공백으로 잘라서 각각 만든다(split)

# print(x)
# print(y)

# 완전 다중입력(개수가 몇개든지 상관없음)
# 중요!!!
inputs = list(map(int, input('정수를 입력하세요 > ').split())) # str은 문자 가능/ int는 숫자

print(inputs)