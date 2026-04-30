'''
리스트 자료형: 순서O, 중복O, 삭제O, 수정O

'''

# 선언
a = []
print(type(a))

b = list()
print(type(b))
print()

c = [70, 75, 80, 85]
d = [21.42, 'jmyoo', 'sean', -9, False]
e = [10, 100, ['python', 'study', 'basic']]

# 인덱싱
print(d)
print(d[0], d[1])
print(d[4])
print(e[-1][1])
print(list(e[-1][1]))
print(e[-2])
print()

# 슬라이싱
print(c[0:3])
print(c[2:])
print(e[2][1:3])
print(d[4:])
print(d[4])
print()

# 리스트 연산
print(c+d)
print(c*3)
print('test'+ str(c[1]))
print()

f = [1, -1, 3, 0, 5, -4]
print(f)
f.append(6)
print(f)
f.sort()
print(f)
f.reverse()
print(f)
f.insert(2, 7)
print(f)
print()

c[0] = 4
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[1]
print('c - ', c)
print()


a = [1, 2, 3, 4, 5]

while a:
    p = a.pop()
    print(p)

