# LIST
courses = ['mech', 'civil', 'comp', 'it']
#  indexing
print(courses[0])  # mech
print(courses[0:2])  # ['mech', 'civil']
print(courses[-1])  # it

# list method
courses.index('mech')  # 0
courses.append('electrical')  # Append element to the end of the list
courses.insert(0, 'AI')  # Insert element at specific index
courses_1 = ['art', 'sci']
courses.extend(courses_1)  # Extend list by appending elements from another list
courses.pop()  # by default, it will remove list element of list
courses.pop(0)  # remove element of specific index
courses.remove('art')  # remove specific element from list
courses.reverse()  # reverse order of elements of list
courses.sort()  # sort alphabetically or in ascending order
courses.sort(reverse=True)  # after sorting, reverse the order
sorted_courses = sorted(courses)  # it will create new list with sorted elements

# min max sum
num = [1, 3, 5, 2, 4]
min(num)  # 1
max(num)  # 5
sum(num)  # 15

# enumerate method
for index, course in enumerate(courses, start=0):
    print(index, course)

# join method
courses_str = ', '.join(courses)  # mech, it, electrical, comp, civil

# split method
new_list = courses_str.split(',')  # ['mech', ' it', ' electrical', ' comp', ' civil']

# TUPLE
tuple1 = ('mech', 'civil', 'comp', 'it')
# tuple1[0] = 'AI' # Tuples don't support item assignment due to it's inmutability

# SET
# order is not important in set
# it get rid of duplicate element by its own
set_1 = {'mech', 'civil', 'comp', 'it'}
set_2 = {'mech', 'civil', 'art', 'sci'}
print(set_1.intersection(set_2))  # {'mech', 'civil'} # comman elements
print(set_1.difference(set_2))  # {'it', 'comp'} different set1 element than set2
print(set_2.difference(set_1))  # {'sci', 'art'} different set2 element than set2
print(set_1.union(set_2))  # {'it', 'comp', 'art', 'sci', 'mech', 'civil'}

# empty list, set and tuple

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # it is dictonary
empty_set = set()
