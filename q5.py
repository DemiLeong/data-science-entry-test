def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    
    #assign input to variable
    x = float(num)  
    y = float(divisor)
    
    #check any remainder if x divide y using modulus operator
    if x % y == 0:  
        return True
    else:
        return False
    
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(f"Is 10, 2 divisible = {check_divisibility(10, 2)}")
print(f"Is 7, 3 divisible = {check_divisibility(7, 3)}")