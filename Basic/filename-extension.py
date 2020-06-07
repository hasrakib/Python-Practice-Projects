# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java


# Get the filename from user
filename = input("Enter the filename: ")

# check if it is a valid filename
if (filename.find('.') == -1):
    print("This is not a valid filename.")
else:
    words = filename.split('.')  # Divide the filename from '.'
    words_length = len(words)  # Get the length of the divide
    print(words[words_length-1])  # print only the last piece of divide
