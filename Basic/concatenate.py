# Write a Python program to concatenate all elements in a list into a string and return it.


def concatenate(list):
    string = ''
    for i in list:
        string += str(i)
    return string


print(concatenate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
