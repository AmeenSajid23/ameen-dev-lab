#  A Tuple containing different data types and does not allow modifications
# Note: Tuples are immutable, so operations that modify the tuple (like adding or removing elements) are not allowed and will raise an error if attempted.
#############################################################################################

a = (1, True, "Hello", 3.14, 205, 205)  # A tuple containing different data types
print("Tuple contents:", a)

access_first = a[0]  # Accessing the first element
print("First element:", access_first)

access_second = a[1]  # Accessing the second element
print("Second element:", access_second)

a[1] = False  # Attempting to modify the second element (will raise an error)

print("min(a):", min(a[:2]))  # Finding the minimum among the first two elements
print("Length of tuple:", len(a))  # Getting the length of the tuple
print("Type of a:", type(a))  # Checking the type of 'a'
print("Sliced tuple (first two elements):", a[:2])  # Slicing the tuple to get the first two elements
print("Sliced tuple (from index 2 to end):", a[2:])  # Slicing the tuple from index 2 to the end
print("Sliced tuple (from index 1 to 3):", a[1:4])  # Slicing the tuple from index 1 to 3
print("Reversed tuple:", a[::-1])  # Reversing the tuple
print("Tuple repeated twice:", a * 2)  # Repeating the tuple twice
print("Sliced tuple (first two elements):", a[:2])  # Slicing the tuple to get the first two elements
