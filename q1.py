#!/usr/bin/env python3
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # first check if the input x, y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # swap x, y values
    x = x + y   # sum the values of x + y and assign to x, e.g. 9+17=26
    y = x - y   # take the new x value (total sum) minus y value and assign back to y, hence y now is having x initial value
    x = x - y   # take the new x value (total sum) minus y value and assign back to x, hence x now is having y initial value
    
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("Test 1: 'Apple', 10")
print(swap("Apple", 10), ' not all values numeric')

print("Test 2: 9, 17")
print(swap(9 , 17), 'values swapped')




