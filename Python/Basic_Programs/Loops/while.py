# A simple while loop that prints numbers from 1 to 5
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

print("While loop has ended.")

# End of program

# Another way of writing the same while loop
print("\nAnother way to write the same while loop:\n")
count = 1
while (count <= 5):
    print("Count is:", count)
    count = count + 1
print("While loop has ended.")
# End of program

#Compact form of while loop
print("\nCompact form of while loop:\n")
count = 1
while count <= 5: print("Count is:", count); count += 1
print("While loop has ended.")
# End of program


while True:
    user_input = input("Type 'exit' to quit the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print("You entered:", user_input)   
print("Loop has ended.")
# End of program
i = 10
while i > 0:
    print("Countdown:", i)
    i -= 1
print("Liftoff!")
# End of program