def func_multiply(x):
    y1 = x *10
    y2 = x *20
    y3 = x *30
    return {'val1': y1, 'val2': y2, 'val3': y3}

a = func_multiply(1)
print(a)

print(a.get('val2'), a.items(), a.keys())
print()


'''
get: value 반환, items: 목록, keys: 키 반환
'''

# 매개변수 *arg, **arg 사용법! 
def func_args(*b): # a 에 넘어온 인자를 튜플로 묶는다, 인자 여러개 가능
    print(b)
    print(type(b))
    
func_args(10+1, 4)
print()

def func_args2(**arg): # 넘어온 인자를 딕셔너리로 묶는
    print(arg)
    print(type(arg))

func_args2(ir=4, r395=9.2)    
print()

# "{}".format f"{}"
call = f"{func_multiply(1)}"
print(call)
print("{}".format(func_multiply(1)))
print()

def tot_length(word: str, num: int)-> int:
    return(len(word)*num)
print(tot_length('Yoo jaemin', 10))
print('->', tot_length("i love you", 10))
print()


# lambda func 사용법 -> 
data = [(1, 3), (4, 1), (-1, 3), (9, 0)]
res = sorted(data, key=lambda x:x[1])
print(res)


    
    



    
 