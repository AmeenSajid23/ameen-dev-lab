#try except block to handle division by zero error

a= int(input("Enter numerator: "))
b= int(input("Enter denominator: "))

try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")