# A List containing different data types
# A lists are mutable, meaning you can modify them after creation 
# (e.g., adding, removing, or changing elements)
# Lists maintain the order of elements and allow duplicates
#############################################################################################   

a = [1, True, "Hello", 3.14, 205]  # A list containing different data types

print("List contents:", a)
print("First element:", a[0])  # Accessing the first element
print("Second element:", a[1])  # Accessing the second element
print("min(a):", min(a[:2]))  # Finding the minimum among the first two elements
print("Length of list:", len(a))  # Getting the length of the list
print("Type of a:", type(a))  # Checking the type of 'a' two elements
print("Sliced list (first two elements):", a[:2])  # Slicing the list to get the first
print("Sliced list (from index 2 to end):", a[2:])  # Slicing the list from index 2 to the end
print("Sliced list (from index 1 to 3):", a[1:4])  # Slicing the list from index 1 to 3
print("Reversed list:", a[::-1])  # Reversing the list
print("List repeated twice:", a * 2)  # Repeating the list twice