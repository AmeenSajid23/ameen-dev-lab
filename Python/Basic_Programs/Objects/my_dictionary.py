# Dictionary is a collection of key-value pairs
# Keys must be unique and immutable (e.g., strings, numbers, tuples)
# Values can be of any data type and can be duplicated
#############################################################################################

a = {
    "name": "Ameen",
    "age": 25,
    "city": "New York"
    }
a[3] = "New Value"  # Adding a new key-value pair

print(a)  # Output: {'name': 'Ameen', 'age': 25, 'city': 'New York', 3: 'New Value'}

del a[3] # Deleting the key-value pair with key 3

print(a)  # Output: {'name': 'Ameen', 'age': 25, 'city': 'New York'}