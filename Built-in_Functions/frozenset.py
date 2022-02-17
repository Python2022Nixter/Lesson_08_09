import os


os.system('clear')


# list() function
t1 = (1, 2, 3, 4, 5)
l1 = list(t1)
print(l1)


s1 = {1, 2, 3, 4, 5}
l1 = list(s1)
print(l1)

# tuple(ITERABLE)
# set()
# frozenset() - immutable set

s2 = frozenset(l1)
print(s1, type(s2))

# dict()
d1 = dict(({1, 2}, [3, 4], (5, 6)))
print(d1)