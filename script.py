
import os


os.system('clear')


print("type([])", type([]))
print("type(())", type(()))
print("type((1))", type((1)))
print("type((1,))", type((1,)))

print("type({})", type({}))
print("type({'a':1})", type({'a':1}))
print("type({1, 1})", type({1, 1}))

# is, is not

print((type(1)is not int))
print()
print("type ((1,)) is tuple - ", type((1,)) is tuple)

a = []
a.append(1)
print("a - ", a)

# b = ()
# b.append(1)
# print("b - ", b) # TypeError: 'tuple' object does not support item assignment

c = (
    {1: "test1"},
    { 2: "test2"}
    )
print("c - ", c)
c[0][1] = "test3"
print(type(c), type(c[0]))
print("c - ", c)

ee = ([1, 2], [3, 4])
encode_rfc2231 = ((1, 2), (3, 4))
ee[0][0] = 5
print(ee)

#
d = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1,2, 3, 4, 5}
print(len(d))

sysmbol = "*"

    # List comprehension
    
list1 = [[sysmbol  for i in range(3)] for j in range(3)]
for i in list1:
    print(*i)
    