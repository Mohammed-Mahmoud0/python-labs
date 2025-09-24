# - write a program that prints hello world
print("Hello, World")
# 	- application to take a number in binary form from the user, and print it as a decimal

try:
    binary_number = input("Enter a binary number: ")
    decimal_number = int(binary_number, 2)
    print(f"The decimal equivalent of {binary_number} is {decimal_number}")
except:
    print("please enter a valid binary number")

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

def checkNumber(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return "not divisible by 3 or 5"


try:
    num = int(input("enter a number: "))
    print(checkNumber(num))
except:
    print("please enter a valid number")

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

try:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    print(f"The area of the circle is {area}")
    print(f"The circumference of the circle is {circumference}")
except:
    print("please enter a valid radius")

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

try:
    name = input("Enter your name: ")
    if not name.strip() or name.isdigit():
        print("Invalid name. Please enter a valid name.")

    email = input("Enter your email: ")
    print("Name: ", name)
    print("Email: ", email)
except:
#     print("please enter a valid name")

# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

s = input()
counter = 0

for i in range(len(s) - 2):
    if s[i:i+3] == "iti":
        counter += 1

print("The substring 'iti' occurs", counter, "times.")