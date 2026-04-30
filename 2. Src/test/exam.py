'''
import string

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

result = {}
for x, y, z in zip(a, b, c):
    result[x] = y*z
print(result)

print({ x:y*z for x, y, z in zip(a, b, c) })
print()
print()

def alphabet(filepath):
    with open(filepath, 'w', encoding="UTF-8") as f:
        for letter in string.ascii_uppercase:
            f.write(letter)


alphabet("alphabet.txt")
'''


'''
x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N -> 3
출력 결과 : [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R'],['S','T','U'],['V','W','X'],['Y','Z']]
    
N -> 5
출력 결과 : [['A','B','C','D','E'],['F','G','H','I','J'],['K','L','M','N','O'],['P','Q','R','S','T'],['U','V','W','X','Y'],['Z']]
'''


x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def alphabet_output(size=3):
    for idx in range(0, len(x), size):
        print(idx)

alphabet_output(3)        
