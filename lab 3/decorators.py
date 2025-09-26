# 7) Decorators Task
#    - Create a decorator called "log_time" that:
#         - Records the execution time of any function.
#         - Saves the function name and runtime into "execution_log.txt".
#    - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
#    - Verify that the log file contains entries after running.

import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_log.txt", "a") as log_file:
            log_file.write(
                f"Function '{func.__name__}' executed in {execution_time} seconds\n"
            )
        return result

    return wrapper
