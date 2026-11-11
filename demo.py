import math

user_input = input("Enter a value: ")

try:
    number = float(user_input)
    
    if number < 10:
        print("invalid char")
    else:
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")

except ValueError:
    print("invalid item")
