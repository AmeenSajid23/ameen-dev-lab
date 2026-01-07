def hello_world():
    print("Hello, World!")
    return "hey bro"

print(1)
hello_world()
print("-------------------")
a=hello_world()
print(a)

# Another way to call the function
print("-------------------")
print(hello_world())

#Another way to call the function and store the return value
print("---------Another way to call the function and store the return value----------")
result = hello_world()
print("Returned value:", result)

#Another way to call the function directly in print statement
print("---------Another way to call the function directly in print statement----------")
print("Function returned:", "+", hello_world())

#Another way to call the function multiple times
print("---------Another way to call the function multiple times----------")
for i in range(3):
    print(f"Call {i+1}: ", end="") # Print call number without newline then call function
    hello_world()