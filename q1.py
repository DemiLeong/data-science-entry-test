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
    
    # swap
    x = x + y
    y = x - y
    x = x - y
    
    print("x: ", x, "y: ", y)
    
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("Test1: swap('Apple', 10)")
Swap("Apple", 10)

print("Test2: swap(9, 17)")
Swap(9 , 17)



