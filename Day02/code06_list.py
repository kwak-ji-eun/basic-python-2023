# 복합형

# 리스트
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10 # 변수 10개 만든 상황

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# 리스트
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1, 2, 3]
arr2 = [1.1, 2.2, 3.3]
arr3 = ['Hello', 13, 'World!', True]
print(arr3)
print(type(arr3))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,5,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)

# 튜플은 만들면 추가 및 삭제 안된다(변화 x) <-> 리스트는 가능
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

#tuple1.append(4)
print(tuple1)
print(type(tuple1))

# 딕셔너리
spiderman = { 'name' : 'Peter Parker ',
               'age' : 18,
            'weapon' : 'Web Shooter',
            'desert' : '탈영병'}

print(spiderman)
print(spiderman['weapon'])
print(spiderman['desert'])
print(type(spiderman))

# 집합
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")
print(set1)