# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


exam_st_date = (11, 12, 2014)

length = len(exam_st_date)

for i in range(0, length):
    print(exam_st_date[i], end='/')
print('\n')
