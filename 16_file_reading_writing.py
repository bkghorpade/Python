f = open('test.txt', mode='r')
'''
r - read file
w - write file
a  - append file
r+ - read and write
'''
print(f.name)  # test.txt

f.close()
# read
with open('test.txt', 'r') as f:
    f_read = f.read(100)
    # type str. it reads all data at once which can cause memmory issue
    # to avoid this, we can pass size argument. which will indicate number of characters to read at one time
    # but at the end of file, it will return empty string
with open('test.txt', 'r') as f:
    size_to_read = 100
    f_read = f.read(size_to_read)
    while len(f_read) > 0:
        print(f_read, end='')  # end argument - string appended after last value. if we pass * , there will be * after each 10 characters
        f_read = f.read(size_to_read)

# seek

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_read = f.read(size_to_read)
    print(f_read, end='')
    f.seek(0)
    f_read = f.read(size_to_read)
    print(f_read)

# write

with open('test.txt', 'rb', ) as rf:
    with open ('test_copy.txt', 'wb') as wf:
        for line in rf:
            wf.write(line)

# while working on files, sonme time, we got unicode decode error.
# to avoid that, we can pass 'encoding' argument OR 'rb' instead of 'r', and 'wb' instead of 'w'

