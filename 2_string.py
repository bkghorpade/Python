message = 'Hello World1'

# when to use single and double quotes
message_one = "Bobby's World"
# use Double quotes if single quote used inside string. and vise versa...
# use three quotes ("""  """) for multiple line string

# number of characters in string
len(message)  # 11

# accessing characters of string
print(message[0])  # H
print(message[0:5])  # Hello -- 5th index character excluded
print(message[:5])  # Hello

# string methods (method is a function which belongs to object)

lowercase = message.lower()  # make all characters lowercase
uppercase = message.upper()  # make all characters uppercase
capatilize = message.capitalize()  # make the first character of each word upper case and the rest lowercase
count = message.count('l')  # counting occurance of specific character or set of characters in given string

find = message.find('l')  # returns index position of start of first occurance of given character or of set of characters
#  it will return -1 if given character not available in string

replace = message.replace('World', 'Universe')
# methods can't change original string. we have to store updated string in one variable.

center = message.center(25, '*')  # *******Hello World*******
# center the message within 25 characters. fill character is *

index = message.index('o')  # Return the lowest index in message where substring 'o' is found

is_alpha_numeric = message.isalnum()  # Return True if the string is an alphanumeric string, False otherwise

text1 = "hello"
text2 = "hello123"
text3 = "Hello, World!"
print(text1.isalpha())  # True
print(text2.isalpha())  # False - containes numbers
print(text3.isalpha())  # False - contains speces and puncuations
# Output of isalpha() is True if all characters are alphabetic without any spaces, numbers, puncuations or special characters
text1 = "hello123"
text2 = "hello world"
text3 = "12345"
text4 = "!@#$"

print(text1.isalnum())  # Output: True
print(text2.isalnum())  # Output: False (contains space)
print(text3.isalnum())  # Output: True
print(text4.isalnum())  # Output: False (contains special characters)
# Output of isalnum() is True if all characters are either all alphabetic or all numeric or mix of alphabets and numbers
# without any spaces, puncuations or special characters

# Concatnation of strings
msg1 = 'Hello'
msg2 = 'Dear'
message = '{}, {}. Welcome!'.format(msg1, msg2)  # formated string
f_message = f'{msg1}, {msg2}. Welcome!'  # f string

print(dir(str))  # list of all method applicable to string
help(str)  # information about all methods
help(str.isalpha)  # information about specific method

