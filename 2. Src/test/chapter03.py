# 파이썬 변수
# 기본 선언


n = 700

print(n)
print(n*3.14)
print(type(n))

#동시선언

x=y=z= 123
print(x, y, z)

var = 'change value'
print(var)
print(type(var))


# ex1)
# object reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

print(300)
print(int(300))

# ex2)

n =777
print(n, type(n))

m=n
print(m, n)


#id (identity) 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m)==id(n))
print()

#같은 오브젝트 참조
m= 100
n =100
print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates -> 변수 선언  (가장 추천)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
_age = 6
_age_ = 6

# 1age =1 X


# 예약어  for, as, class