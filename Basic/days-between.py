# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)

difference = last_date - first_date

print(difference.days)
