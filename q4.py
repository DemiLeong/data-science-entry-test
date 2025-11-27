def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    
    input_txt = str(s)  # ensure input a string
    reverse_txt = input_txt[::-1] # slicing feature using negative step to reverse the list 
    
    return reverse_txt


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

given_txt = "Hello World"
reverse_txt = string_reverse(given_txt)
print(f"Reverse text for {given_txt} = {reverse_txt}")

given_txt = "Python"
reverse_txt = string_reverse(given_txt)
print(f"Reverse text for {given_txt} = {reverse_txt}")