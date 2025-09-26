# 3) Datetime Reminder Script
#    - Ask user for a date (YYYY-MM-DD).
#    - Calculate how many days remain until that date.
#    - If it is in the past, print "This date has already passed."
#    - Otherwise, save the reminder into "reminders.txt" in format:
#         "{date} -> {days_left} days left"


def date_time_reminder():
    from datetime import datetime

    user_date_str = input("Enter a date (YYYY-MM-DD): ")
    user_date = datetime.strptime(user_date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    days_left = (user_date - today).days

    if days_left < 0:
        print("This date has already passed.")
    else:
        with open("reminders.txt", "a") as file:
            file.write(f"{user_date} -> {days_left} days left\n")
        print("Done")

