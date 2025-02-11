# sort vs sorted
    # sort method only for list. sorted is for all datatypes
    # sort returns None. sorted returns list irrespective of datatype
st = 'qwertyuiopasdfghjklzxcvbnm'
sts = sorted(st)
print(sts)
li = [9,2,4,3,5,1,7,6,8,0]
s_li = sorted(li) # creating new list with sorted element. reverse=False(default)
print('Sorted list :\t', s_li)
li.sort()  # sorting original list
print('Sorted list :\t', li)

# tuple
tup = (9,2,4,3,5,1,7,6,8,0)
# tup.sort() attribute error
s_tup = sorted(tup) # returns list
print('Sorted tuple :\t', s_tup)

# dict
dic = {'name': 'bapusaheb', 'age': 33, 'profession': 'Engineer', 'place': 'Ahmednagar'}
s_dic = sorted(dic)  # ['age', 'name', 'place', 'profession']

# sorting based on absolute values
lst = [-6,-5,-4,1,2,3]
s_lst = sorted(lst, key=abs)  # [1, 2, 3, -4, -5, -6]
