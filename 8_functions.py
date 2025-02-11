import subprocess
import optparse
def hello_func():
    print('Hello Function')


print(hello_func)  # it will give us memory location (<function hello_func at 0x000001EDE516D5A0>)
print(hello_func())  # it will print return value of function

# *args, **kwargs
# args - positional arguments
# kwargs - keyword arguments

def student_info(*args, **kwargs):
    print(args)  # ('Math', 'Science') - tuple
    print(kwargs)  # {'name': 'Bapu', 'age': 34} - dict

student_info('Math', 'Science', name='Bapu', age=34)

# order should be 1. Positional arguments, 2. Keyword arguments
# * & ** to unpack the values
# not necessary to use args and kwargs words exactly. we can use any string after * and **


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    # check if year divisible by 4
    # check if .year not divisible by 100 OR should be divisible by 400

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""


    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2020, 2))

