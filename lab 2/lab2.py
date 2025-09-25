def sort_numbers():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("asc sort: ", sorted(nums))
    print("desc sort: ", sorted(nums, reverse=True))


def generate_seq(length, start):
    seq = []

    for i in range(start, length + 1):
        seq.append(i)
    print("Generated sequence:", seq)


def ask_user_num():
    res = []
    counter = 0
    while True:
        counter += 1
        num = input("Enter a number or 'done' to finish: ")
        if num != "done" and num.isdigit():
            res.append(int(num))
        elif num == "done":
            break
        else:
            print("Invalid input")
            continue
    print("the sum is: ", sum(res))
    print("the average is: ", sum(res) / len(res))
    print("the count of valid numbers is: ", len(res), "from ", counter, "inputs")


def operations_on_list():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    nums_set = set(nums)
    nums_set = sorted(nums_set)
    print("numbers(sorted and unique):", nums_set)


def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        print("word: ", word, " count: ", count)


def shopping_cart():
    cart = {}
    while True:
        print(
            "1 to add item\n2 to remove item\n3 to view cart\n4 to checkout\n5 to exit"
        )
        choice = input("Choose an option: ")
        if choice == "1":
            item = input("Enter item name: ")
            price = float(input("Enter {item} price: "))
            if item in cart:
                cart[item] += price
            else:
                cart[item] = price
        elif choice == "2":
            if cart:
                item = input("Enter item name to remove: ")
                cart.pop(item)
            else:
                print("Cart is empty, press 1 to add items.")
        elif choice == "3":
            if cart:
                print("Shopping Cart:")
                for item, price in cart.items():
                    print(f"Item: {item}, Price: {price}")
            else:
                print("Cart is empty.")
        elif choice == "4":
            total = sum(cart.values())
            print(f"Total checkout amount: {total}")
        elif choice == "5":
            break


def number_guessing_game():
    import random

    number_to_guess = random.randint(1, 20)
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 20: ")
        if not guess.isnumeric():
            print("Invalid input, please enter a number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
            )
            break


def gradebook_system():
    gradebook = {}
    i = 0
    while i < 5:
        name = input(f"Enter student {i + 1} name: ")
        try:
            grade = float(input(f"Enter student {i + 1} grade: "))
            gradebook[name] = grade
            i += 1
        except ValueError:
            print("Invalid grade, please enter a numeric value.")
            continue
    highest_grade = max(gradebook.values())
    minimum_grade = min(gradebook.values())
    average_grade = sum(gradebook.values()) / len(gradebook)
    print("the highest grade is: ", highest_grade)
    print("the minimum grade is: ", minimum_grade)
    print("the average grade is: ", average_grade)


def main():
    while True:
        print(
            "1. Sort Numbers\n2. Generate Sequence\n3. User Number Input\n4. List Operations\n5. Word Count\n6. Shopping Cart\n7. Number Guessing Game\n8. Grading System \n9. Exit"
        )
        choice = input("Choose an option: ")
        if choice == "1":
            sort_numbers()
        elif choice == "2":
            length = int(input("Enter the length of the sequence: "))
            start = int(input("Enter the starting number: "))
            generate_seq(length, start)
        elif choice == "3":
            ask_user_num()
        elif choice == "4":
            operations_on_list()
        elif choice == "5":
            count_words()
        elif choice == "6":
            shopping_cart()
        elif choice == "7":
            number_guessing_game()
        elif choice == "8":
            gradebook_system()
        elif choice == "9":
            break
        else:
            print("Invalid choice, please enter a valid number.")


main()
