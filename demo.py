import math

user_input = input("Enter a number: ")

try:
    number = float(user_input)
    
    if number < 0:
        print("invalid item")
    else:
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")

except ValueError:
    print("invalid item")
