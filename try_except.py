# try - except

try:
    f = open('testt.txt')
except FileNotFoundError as e:
    print(e)

# multiple except

try:
    f = open('test.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)


# try except and else

try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
else:
    print(f.read())
    f.close()