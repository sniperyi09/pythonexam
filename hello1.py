from copy import copy
a = [1,2,3]

b = copy(a)
a[1] = 4
print(id(a))
print(b)
print( a is b)

c, d = ('python', 'life')
print(c)
print(d)

e = 3
f = 5
e,f = f,e
print(e)
print(f)
