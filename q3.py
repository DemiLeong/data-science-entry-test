def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    if key in dct:  # check if key exist in dictionary
        # print the original key-value and update old value with new value
        print(f"Original value: {dct}")
        dct[key] = value
    else:
        # if key value not exist in dictionary, add in new key-value
        dct[key] = value
        
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


print("1st Test:")
updated_value = update_dictionary({}, "name", "Alice")
print (f"Updated value: {updated_value}")

print("2nd Test:")
updated_value = update_dictionary({"age": 25}, "age", 26)
print (f"Updated value: {updated_value}")
