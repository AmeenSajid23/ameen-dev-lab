print ("Hi Enter your AGE")

age = int(input())

if age < 18:
    print("You are " + str(age) + " Y/O and are a minor.")
elif age >= 18 and age < 65:
    print("You are " + str(age) + " Y/O and are an adult.")
else:
    print("You are " + str(age) + " Y/O and are a senior citizen.")