def check_number(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")
number = int(input("Enter a number:"))
check_number(number)