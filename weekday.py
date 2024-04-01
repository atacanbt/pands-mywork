# weekday.py
# this program outputs whether today is a weekday or not
# author: atacan buyuktalas

import datetime
# here 'datetime' module imported 
x = datetime.datetime.now()
# this line checks today's date and time
y = x.strftime("%A")
# here 'strftime()' method used for formatting the info into readable output 
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
# we defined the weekdays 
if y in weekdays:
    # we are checking whether today's date is a weekdays and printing output accordingly. 
    # if today's date can be find in 'weekdays' 
    print('Yes, unfortunatly today is a weekday.')
else:
    # else, we print out this
    print('It is the weekend, yay!')