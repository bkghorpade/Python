lst = [1,2,3,4,5]

for num in lst:
    print(num)  # 1,2,3,4,5

# break - to break the loop after attening certen condition
for num in lst:
    if num == 3:
        break
    print(num)  # 1,2

# continue - to ignore specific iteration
for num in lst:
    if num == 3:
        continue
    print(num)  # 1,2,4,5

# range
for i in range(5): # stop = 5, start = 0 (default)
    print(i)  # 0,1,2,3,4

for i in range(1,5): # stop = 5, start = 1
    print(i)  # 1,2,3,4

for i in range(1,10,2): # stop = 10, start = 1, step = 2
    print(i)  # 1,3,5,7,9

# while loop
x = 0
while x < 5:
    print(x)  # 0,1,2,3,4
    x += 1
