# - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.
from decorators import log_time 
@log_time
def math_automation():
  import math
  file = open("math_report.txt", "w")
  numbers = list(map(float, input("Enter multiple numbers (comma-separated): ").split(",")))
  for number in numbers:
    floor_value = math.floor(number)
    ceil_value = math.ceil(number)
    sqrt_value = math.sqrt(number)
    area_circle = math.pi * (number ** 2)
    file.write(f"Number: {number}\n")
    file.write(f"  Floor: {floor_value}\n")
    file.write(f"  Ceil: {ceil_value}\n")
    file.write(f"  Square Root: {sqrt_value}\n")
    file.write(f"  Area of Circle: {area_circle}\n\n")
  file.close()
  print("File 'math_report.txt' created successfully.")
  with open("math_report.txt", "r") as file:
    data = file.read()
    print("data of 'math_report.txt':")
    print(data)
    