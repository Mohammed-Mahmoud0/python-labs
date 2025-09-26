from date_time_script import date_time_reminder
from decorators import log_time
from math_automation import math_automation
from os_file_manager import os_file_manager
from product_data_transformation import product_data_transformation
from random_data_generator import random_data_generator
from regex_log_cleaner import regex_log_cleaner

def main():
  while True:
    print("choose an option:")
    print("1. Date and Time Script")
    print("2. Math Automation")
    print("3. OS File Manager")
    print("4. Product Data Transformation")
    print("5. Random Data Generator")
    print("6. Regex Log Cleaner")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
      date_time_reminder()
    elif choice == "2":
      math_automation()
    elif choice == "3":
      os_file_manager()
    elif choice == "4":
      product_data_transformation()
    elif choice == "5":
      random_data_generator()
    elif choice == "6":
      regex_log_cleaner()
    elif choice == "7":
      print("see you later!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()