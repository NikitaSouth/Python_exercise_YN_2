number = int(input("Please enter any decimal number: "))
if number % 2 == 0:
    print("This number is even!")
    if number % 4 == 0:
        print("This number is a multiply of 4")
else:
    print("This number is odd!")
num = int(input("Please enter any decimal number: "))
check = int(input("Please enter any decimal number you want first number to be divided by: "))
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "doens't divide evenly by", check)
