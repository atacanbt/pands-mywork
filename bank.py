# bank.py
# this program prompts the user and reads in two money amounts (in cent) then prints to sum of them in two decimal € value
# author: Atacan

fnum = int(input("Enter the first value in cent: ")) # I used int() to convert the input to integer
snum = int(input("Enter the second value in cent: ")) 
sum = fnum + snum # I calculated the sum of the two values
answer = sum / 100 # I divided the sum by 100 to convert it to €
print("The sum of these is €",answer)
