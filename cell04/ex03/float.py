number = input("Give me a number: ")

try:
    float_num = float(number)

    if float_num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valid number.")