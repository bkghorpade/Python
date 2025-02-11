from module_test import addition, subtraction, test
# Module Imported successfully
print(test)  # test string
a = 10
b = 2

add = addition(a, b)
print(add)  # 12

sub = subtraction(a,b)
print(sub)  # 8

import sys
print(sys.path) # paths on system where python will look for module to import
# if any script we are trying to import is not available in current directorywe can add path
sys.path.append('<script path>')
