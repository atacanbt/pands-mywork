# accounts.py
# this program prompts the user their 10-digit account number and prints it out by revelaing only the last 4-digit 
# rest is replaced by X for security reasons

# author: atacan buyuktalas

accnum = input('Enter your 10-digit account number: ')

last_four_digit = int(accnum[6:10])
masked_accnum = 'X' * 6
# since the first 6-digit of the account number will always be replaced by X
print(f'{masked_accnum}{last_four_digit}')
