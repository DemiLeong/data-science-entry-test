#!/usr/bin/env python3
def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    
    x = lst     #assign the list to x
    
    if find_val in x:    # if find_val find in lst 
        replace_lst = [replace_val if val == find_val else val for val in x]    # replace find_val with replace_val
    else:
        return x
    return replace_lst



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print(f'1st Test set "[1, 2, 3, 4, 2, 2], 2, 5", \nresult= {find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)}')
print(f'2nd Test set ["apple", "banana", "apple"], "apple", "orange", \nresult= {find_and_replace(["apple", "banana", "apple"], "apple", "orange")}')

