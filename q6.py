def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    
    i = 0 # assign 0 to i which is the running number for the list
    while i < len(lst): # is true if i less than the total list number
        if lst[i] < 0:  # if value of the list less than 0 which is negative value return to main
            return lst[i]
            
        i = i + 1 # increase 1 to i
    
    return "No negatives" # if none of the values in list is negative return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print(f"The first negative value for [3, 5, -1, 7, -2, 8]: {find_first_negative([3, 5, -1, 7, -2, 8])}")
print(f"The first negative value for [2, 10, 7, 0]: {find_first_negative([2, 10, 7, 0])}")