import os

print('***** file_in_out example *****')
print()

print(os.getcwd())
print(os.__file__)
print()

'''
f = open('.\\114.txt', 'r', encoding= 'UTF-8')
print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
print(f.read())
f.close()
print()
'''

with open('114.txt', 'rt',encoding='UTF-8') as f:
   # print(f.read(3))
   #print(f.read())
   #f.seek(0,0)
   #print(f.read())
   print(f.readline())
   print(f.readline())
   print(f.readline())
print()

with open('contents1.txt', 'w') as wf:
    wf.write('I love python!')




