def find(group, n):
    for value in group:
        if n == value:
            return True
    return False


number_group = [1, 3, 5, 7, 9]
number = input("Enter the number to find: ")

print(find(number_group, int(number)))
