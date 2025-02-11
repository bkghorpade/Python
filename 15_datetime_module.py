import datetime
import pytz

# Naive datetime - a datetime without any timezone

# DATE
d = datetime.date(2024, 9, 29)  # No leading zeros otherwise syntax error
# 2024-09-29
today = datetime.date.today()
print(today)  # 2024-10-29
print(today.year)  # 2024
print(today.weekday())  # 1
print(today.isoweekday())  # 2
# weekday() --> Monday 0 .... Sunday 6
# isoweekday() --> Monday 1 .... Sunday 7

tdelta = datetime.timedelta(days=7) # created time difference of 7 days
newdate = today + tdelta  # 2024-11-05

my_bday = datetime.date(2025,10,17)
till_bday = my_bday - today
print(till_bday)  # 353 days, 0:00:00

# TIME - mostly not used
t = datetime.time(9,30,45, 100000) # 09:30:45.100000
print(t)

# DATETIME
dt = datetime.datetime(2024, 10, 29, 10, 6, 45, 100000)
print(dt)  # 2024-10-29 10:06:45.100000

# TIMEZONE
dt_today = datetime.datetime.today()  # current local datetime with timezone of none
dt_now = datetime.datetime.now(tz=None)  # have option to passin timezone as argument
dt_utcnow = datetime.datetime.utcnow()  # gives current UTC time
print(dt_now)
print(dt_today)
print(dt_utcnow)

# recommended to use pytz library
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)  # 2024-10-30 05:25:10.457440+00:00 (+00:00 is UTC offset)
print(pytz.all_timezones)
dt_itc = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_itc)  # 2024-10-30 11:05:54.770278+05:30

# how to convert 'naive datetime' into 'timezone aware datetime'
dt_now = datetime.datetime.now()
dt_now_itc = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
# OR
dt_now_itc = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')) # passing tz argument to now()
print(dt_now)  # 2024-10-30 11:58:47.008178
print(dt_now_itc)  # 2024-10-30 11:58:47.008178+05:30
# OR
itc_tz = pytz.timezone('Asia/Kolkata')
dt_now_itc = itc_tz.localize(dt_now)  # 2024-10-30 12:02:53.352895+05:30

# convering datetime from one zone to another
dt_mtn = dt_now_itc.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)              # # 2024-10-30 00:50:40.971026-06:00
print(dt_mtn.isoformat())  # 2024-10-30T00:50:40.971026-06:00 (additional T in date and time)

# strftime
dt_now_itc = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt_now_itc.strftime('%B %d, %Y'))  # October 30, 2024 --- Recomended
print()
print('       Weekday : ', dt_now_itc.strftime('%a')) #  Sun, Mon, …, Sat
print('       Weekday : ',dt_now_itc.strftime('%A')) #  Sunday, Monday, …, Saturday
print('       Month   : ',dt_now_itc.strftime('%b')) #  Jan, Feb, …, Dec
print('       Month   : ',dt_now_itc.strftime('%B')) #  January, February, …, December
print('local datetime : ',dt_now_itc.strftime('%c')) #  Wed Oct 30 12:40:53 2024 (Locale’s appropriate date and time representation)
print('  Day of month : ',dt_now_itc.strftime('%d')) #  01, 02, …, 31 (day of month)
print('  microseconds : ',dt_now_itc.strftime('%f')) #  Microsecond as a decimal number, zero-padded to 6 digits
print('      Hour(24) : ',dt_now_itc.strftime('%H')) #  00, 01, …, 23 (Hour)
print('      Hour(12) : ',dt_now_itc.strftime('%I')) #  00, 01, …, 12 (Hour)
print('   Day of year : ',dt_now_itc.strftime('%j')) #  001, 002, …, 366 (day of the year)
print('         Month : ',dt_now_itc.strftime('%m')) #  01, 02, …, 12 (Month as a zero-padded decimal number)
print('       Minutes : ',dt_now_itc.strftime('%M')) #  00, 01, …, 59 (minutes)
print('      AM or PM : ',dt_now_itc.strftime('%p')) #  AM or PM
print('       Seconds : ',dt_now_itc.strftime('%S')) #  00, 01, …, 59  (seconds)
print('Week num (SUN) : ',dt_now_itc.strftime('%U')) #  00, 01, …, 53 (week number. Sunday as first day of week)
print('Week num (MON) : ',dt_now_itc.strftime('%W')) #  00, 01, …, 53 (week number. Monday as first day of week)
print('    local date : ',dt_now_itc.strftime('%x')) #  10/30/24 (Locale’s appropriate date representation)
print('    Local Time : ',dt_now_itc.strftime('%X')) #  12:43:30 (Locale’s appropriate time representation)
print('          Year : ',dt_now_itc.strftime('%y')) #  00, 01, …, 99 (year)
print('          Year : ',dt_now_itc.strftime('%Y')) #  2001,2002,... (year)
print('    UTC Offset : ',dt_now_itc.strftime('%z')) #  +0530 (UTC Offset)
print('     Time Zone : ',dt_now_itc.strftime('%Z')) #  ITC (Time zone name)