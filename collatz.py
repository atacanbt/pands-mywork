# collatz.py
# this program prompts a positive integer from the user and execute '3x+1' problem until reaches to 1 and outputs every value of the steps taken
# author: atacan buyuktalas

number = int(input("Enter a positive integer: "))
# below line is to record the initial input in the output variable to print at the end
output = str(number)
# I set the while loop until it reaches to '1'
while number != 1:
    # then proceeded with if statement to make the calculation. first the program checks whether the number is even
    # if it's even number it divides the number by 2
    if number % 2 == 0:
        number = number // 2
    # if the number is odd, the program multiplies the number by 3 and adds 1
    else:
        number = 3 * number + 1
    # when the program reaaches to value '1', it assignes all numbers emerged during the calculation into output variable with spaces between them
    output += f" {number}"
# I have to strip the variable because there was "%" sign in every result, I couldn't think any other way to resolve it
print(output.strip()) 