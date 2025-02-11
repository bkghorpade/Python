student = {'name': 'Bapusaheb', 'age': 33, 'courses': ['science', 'math']}
# name_of_dictonary = {key1 : value1, key2 : value2}
# kay and values are of any mutable data type

# accessing specific key value
print(student['name'])  # Bapusaheb

# Key error if try to access key which does not exist
# print(student['email'])
# to avoid such error....
print(student.get('email'))  # None (as default is None)
# instead of 'None' we can set some default value
print(student.get('email', __default='email@email.com'))  # email@email.com

# adding new key value pair to dict
student['Phone'] = 8850876334
print(student.get('Phone'))  # 8850876334

# updating key's existing value
student['Phone'] = 9594006636
print(student.get('Phone'))  # 9594006636

# update multiple key value pair at once
student.update({'name': 'Bapu', 'age': 32, 'courses': ['science', 'math', 'engineering']})
print(student)

# deleting specific key value pair
# del method
del student['courses']
print(student)
# pop method.it will remove but also return removed value
phone = student.pop('Phone')
print(student)

# length of dict
print(len(student))

print(student.keys())  # dict_keys(['name', 'age'])
print(student.values())  # dict_values(['Bapu', 32])
print(student.items())  # dict_items([('name', 'Bapu'), ('age', 32)])

# way to iterate through dictonary
for key, value in student.items():
    print(key, value)
