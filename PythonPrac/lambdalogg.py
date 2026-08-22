"""
Anonymous functions, simple function, single line function, functional programming
"""

def double(x):
    return x * 2

k = lambda x: x * 2

print(double(3))
print(k(3))

print((lambda y,z: y + z)(4,5))


l1 = [1,2,3,4,5,6,7,8,9]

f = filter(lambda x: x % 2 == 0, l1)

l2 = list(f)

print(l2)

l3 = [1,2,3,4,5]

l4 = list(map(lambda x: -x, l3))

print(l4)

l5 = [1,2,3,4,5,6,7,8,9]

k = lambda x: x if x % 2 == 0 else -x

l6 = list(map(k,l5))

print(l6)

l7 = [[4,2,"six"],[1,4,"five"],[2,2,'four']]
 
l8 = sorted(l7 , key = lambda x: x[0] + x[1] )

print(l8)