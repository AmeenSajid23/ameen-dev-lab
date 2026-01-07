# Function with Arguments
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

# Calling the function with different arguments
print("-------------------")
greet("Alice")
print("-------------------")
message = greet("Bob")
print(message)

# Another way to call the function and store the return value
print("-------------------")
result = greet("Charlie")
print("Returned value:", result)

# Another way to call the function directly in print statement
print("-------------------")
print("Function returned:", "+", greet("Diana"))

# Another way to call the function multiple times with different names
print("-------------------")
names = ["Eve", "Frank", "Grace"]
for i, name in enumerate(names):
    print(f"Call {i+1}: ", end="")  # Print call number without newline then call function
    greet(name)


# Add two numbers function
def add_numbers(a, b):
    c = a + b
    return c
# Calling the add_numbers function
print("-------------------")
sum_result = add_numbers(int(input("Enter first number: ")), int(input("Enter second number: ")))
print("The sum is:", sum_result)

# Another way to call the add_numbers function directly in print statement
print("-------------------")
print("The sum is:", add_numbers(15, 25))

# Another way to call the add_numbers function with different values
print("-------------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum of {num1} and {num2} is:", add_numbers(num1, num2))


# Nested function calls
def multiply(x, y):
    return x * y
def square(n):
    return multiply(n, n)
# Calling the square function
print("-------------------")
number = int(input("Enter a number to square: "))
squared_value = square(number)
print(f"The square of {number} is:", squared_value)

