# 파이썬 3가지 print format

x=50
y=100
text = 30845434
n='Yoo'

# 출력1
ex1 = 'n= %s, s= %s, sum= %d' % (n, text, x+y)
print(ex1)


#출력2
ex2 = 'n= {n}, s= {s}, sum= {sum}' .format(n=n, s=text, sum=x+y)
print(ex2)


#출력3
ex3 = f'n= {n}, s= {text}, sum = {x+y}'
print(ex3)

#구분기호
m= 100000000

print(f'm: {m:,}')


#정렬
# ^ 가운데 정렬
# < 왼쪽,   > 오른쪽

t = 20
print(f"t : {t:10}")
print(f"t : {t:^10}")
print(f"t : {t:<10}")
print(f"t : {t:>10}")

print(f"{t:-^10}")
print(f"{20.2:#<54}")