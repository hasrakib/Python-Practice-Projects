# Write a Python program to create a histogram from a given list of integers.

# Get the array from the user
print("Enter your array with space (Numeric Only)")
pattern = [int(i) for i in input().split()]
array_length = 5


# Print the histogram

for i in pattern:
    for j in range(i):
        print("*", end="")
    print("")
