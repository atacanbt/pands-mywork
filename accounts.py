# accounts.py
# this program prompts the user their 10-digit account number and prints it out by revelaing only the last 4-digit 
# rest is replaced by X for security reasons

# author: atacan buyuktalas

'''
accnum = input('Enter your 10-digit account number: ')
last_four_digit = int(accnum[6:10])
masked_accnum = 'X' * 6
# since the first 6-digit of the account number will always be replaced by X
print(f'{masked_accnum}{last_four_digit}')
'''
accnum = input('Enter your account number: ')
last_four_digit = int(accnum[-4:])
# here I thought that slicing last four digit will be the best approach as we are not sure exact lenght of account number
rest_of_accnum = len(accnum) - 4
# then I needed to calculate the exact lenght of the account number portion to mask it
masked_accnum = int(rest_of_accnum) * 'X' # I had to convert it to int to multiply it with string
print(f'{masked_accnum}{last_four_digit}') # I used f-string to print the masked account number with the last four digit
