# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

number = input("Enter the number: ")
int1 = int(number)
int2 = int(number + number)
int3 = int(number + number + number)

print(int1 + int2 + int3)
