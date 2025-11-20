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
    
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

result_1 = swap("Apple", 10)
print(f"Input: Apple, 10, Results: {result_1}")

result_2 = swap(9, 7)
print(f"Input: 9, 7, Results: {result_2}")



