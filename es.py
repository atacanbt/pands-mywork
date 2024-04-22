# es.py
# this program consist of a function that reads a file and prints out the accurance of given letter in the file
# author: atacan buyuktalas


# here we are defining a function that takes two arguments, filename and letter
def letterCount (fileName, letter):
    # we are opening the file in the read mode
    with open(fileName, 'r') as f:
        # here the content of the file is assigned to a variable
        content = f.read()
        # then we use the built-in function count to count the occurance of the given letter in the content
    return content.count(letter)

# we are calling the function and printing the result
print(letterCount("moby-dick.txt", 'e'))