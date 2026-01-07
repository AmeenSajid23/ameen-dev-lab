def hello_world():
    print("Hello, World!")

    def addition(x, y):
        
        c = x + y

        return c

    sum = addition(int(input("Enter first number: ")), int(input("Enter second number: ")))

    print("Sum:", sum)

hello_world()