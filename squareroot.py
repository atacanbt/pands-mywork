# squareroot.py
# this program takes positive positive number and outputs its approximate square root value
# author: atacan buyuktalas


def sqrt(n):
    # according to the newton's method, we start with an assumed approx value as the half of the given number
    approx = 0.5 * n
    # to reach better approximation we use below formula 
    better_approx = 0.5 * (approx + n/approx)
    # until we reach a point where assumed approx value is equal to better_approx value, 
    # we should continue our calculation
    # while loop here is calculating the best estimated square root value until the calculation reaches the point
    # where our initial approximation value is equal to better approximation value
    while (better_approx != approx):
        # to reach the better estimated square root value, we consider the previous 'better_approx' as new 'approx'
        # and we are opretating the same calculation 
        approx = better_approx
        better_approx = 0.5 * (approx + n/approx)
    return approx

x = 14.5
y = sqrt(x)

print(f'The sqaure root of {x} is {y}')
