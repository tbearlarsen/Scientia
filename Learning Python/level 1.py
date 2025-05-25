name = input("What is your name?")
age = int(input("What is your age"))
to_100 = 100-age

repeat = int(input("How many times do you want the message?"))

for i in range(repeat):
    print(f"User's name is {name} and is {age} years old. They have {to_100} years until they are 100 years old")