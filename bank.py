# bank.py
# this program prompts the user and reads in two money amounts (in cent) then prints to sum of them in two decimal € value
# author: Atacan

fnum = int(input("Enter the first value in cent: "))
snum = int(input("Enter the second value in cent: "))
sum = fnum + snum
answer = sum / 100
print("The sum of these is €",answer)
