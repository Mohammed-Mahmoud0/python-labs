import time

numbers = list(range(1000000))
nums_set = set(numbers)

search_element = 999999


start_time = time.time()
found_in_list = search_element in numbers
list_time = time.time() - start_time

print("list ------------------------")
print(f"  Time: {list_time} seconds")
print("list ------------------------")

start_time = time.time()
found_in_set = search_element in nums_set
set_time = time.time() - start_time

print("set ------------------------")
print(f"  Time: {set_time} seconds")
print("set ------------------------")
