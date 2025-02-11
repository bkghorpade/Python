my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# +index   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# -index -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# access single element
print(my_list[2])  # it will print 2
print(my_list[-4])  # it will print 6

# accessing multiple elements
# list[start:end] - end index element is excluded from output
print(my_list[0:5])  # [0, 1, 2, 3, 4]
print(my_list[-4:-1])  # [6, 7, 8]
print(my_list[1:-2])  # [1, 2, 3, 4, 5, 6, 7]
# accessing multiple elements with step
# list[start:end:step]
print(my_list[1:6:2])  # [1, 3, 5]
print(my_list[1:7:2])  # [1, 3, 5] # end index element 7 is excluded from output
print(my_list[-1:2])  # empty
print(my_list[-1:2:-1])  # [9, 8, 7, 6, 5, 4, 3]

print(my_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] reversing list
