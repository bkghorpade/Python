a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # it will return True as a and b has same value.
print(a is b)  # it will return False as id(a) not equal to id(b)

c = [4, 5, 6]
d = c
print(id(a), id(b), id(c), id(d))
print(c is d)  # It will return True as c and d pointing to same object. id(c) will be equal to id(d)
print(id(c) == id(d))  # True

# False Values :
    #  False
    #  None
    # Zero of any numeric type
    # Any empty sequence. for example '', (), [].
    # Any Empty mapping. For example, {}

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')