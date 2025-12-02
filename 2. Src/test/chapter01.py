# Print 사용법


# 기본 출력
print('Python Start!')
print(" Python S t a r t!")
print('''Python Start! ''')
print("""Python Start!""")


# 개행
print()


# seperator 옵션
print('P', 'y', 't', 'h', 'o', 'n', sep='')
print('P', 'y', 't', 'h', 'o', 'n', sep='* ')
print('010', '4344', '7047', sep='-')
print('jaeminyoo', 'naver.com', sep='@')

print()


# end 옵션
print('Welcom to', end=' ')
print('IT News', end='   ')
print('Web Site')


# file 옵션
import sys
print('Learn Python', file=sys.stdout)

print()


#format 사용 (d : 3, s : 'python', f : 3.14)

print('====== format 사용 ======')
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('====== %s 사용 ======')
print('%10s' %('nice'))
print('{:>10}'.format('nice'))
print('%-10s' %('nice'))
print('{:10}'.format('nice'))
print('{:_>10}'.format('nice'))
print('{:_^10}'.format('nice'))  # ^ 가운데 정렬

print('%.5s' %('python study'))   # 절삭
print('{:10.5}'.format('pythonstudy'))


# %d
print('====== %d 사용 ======')
print('%d %d' %(1,2))
print('{} {}'.format(1, 2))
print('%4d' % (42))
print('{:>4d}'.format(42))

# %f
print('====== %f 사용 ======')
print('%2.2f %f' % (3.14, 3.32))
print('{:2.2f}' .format(4.098))
print('%06.2f' % (3.141592))
print('{:06.2f}' .format(3.141592))