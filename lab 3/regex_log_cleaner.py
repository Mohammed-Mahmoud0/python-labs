# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.

from decorators import log_time 
@log_time
def regex_log_cleaner():
    file = open("access.log", "w")
    log_lines = [
        "invalid emails here",
        "mohamed." "gmail.com",
        "iam the email.com",
        "@google.com",
        "m.f@gmail.com",
        "john.doe@example.com",
        "jane_doe123@domain.co",
        "alice@wonderland.com",
        "m.f@gmail.com",
    ]
    for line in log_lines:
        file.write(line + "\n")
    file.close()
    import re

    file = open("access.log", "r")
    data = file.read()
    valid_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)
    file.close()
    valid_emails = list(set(valid_emails))
    with open("valid_emails.txt", "w") as file:
        for email in valid_emails:
            file.write(email + "\n")
    print(f"Unique valid emails found: {len(valid_emails)}")


