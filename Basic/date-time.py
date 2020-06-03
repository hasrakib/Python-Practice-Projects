# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
import datetime

print("\nCurrent date & Time")
date_time = datetime.datetime.now()

print(f"{date_time.year}-{date_time.month}-{date_time.day} {date_time.hour}:{date_time.minute}:{date_time.second}\n")
