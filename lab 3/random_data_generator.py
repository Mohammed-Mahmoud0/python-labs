# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.


def random_data_generator():
  import random
  import csv

  count = int(input("How many random numbers to generate? "))
  numbers = [random.randint(1, 1000000) for _ in range(count)]

  with open("random_numbers.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index", "value"])
    for index, value in enumerate(numbers, start=1):
      writer.writerow([index, value])

  average = sum(numbers) / count if count > 0 else 0
  print(f"Total count: {count}")
  print(f"Average of numbers is: {average}")
  