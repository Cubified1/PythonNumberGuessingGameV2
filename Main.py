import random
import time


print("welcome to python number guessing game")

input("Press hit enter to continue")

def number_guessing():
    user_level = input("Please enter your level Easy, Medium or Hard: ").lower()
    if user_level == "easy":
        lowest_number = 1
        highest_number = 50
    elif user_level == "medium":
        lowest_number = 1
        highest_number = 100
    elif user_level == "hard":
        lowest_number = 1
        highest_number = 1000
    else:
        print("Invalid input")
    guesses = 0
    is_running = True

    RandomNum = random.randint(lowest_number, highest_number)



    while is_running:

        user_guess = input(f"Please enter your guess from {lowest_number} to {highest_number}: ")

        if user_guess.isdigit():

            user_guess = int(user_guess)
            guesses += 1

            if user_guess < lowest_number or user_guess > highest_number:
                print(f"Please enter a number between {lowest_number} and {highest_number}")

            elif user_guess > RandomNum:
                print("Your guess is too high")

            elif user_guess < RandomNum:
                print("Your guess is too low")

            else:
                print("You guessed the number!")
                if guesses == 1:
                    print(f"it took you {guesses} guess")
                else:
                    print(f"it took you {guesses} guesses")
                is_running = False
        else:
            print("Invalid input")


def continue_again():
    close_counter = 0


    again = input("Do you want to continue (y/n)? ")
    while again == "y":
        number_guessing()
        continue_again()

    if again == "n":
        print("Goodbye!")
        for close_counter in reversed(range(0, 4)):
            time.sleep(1)
            print(f"closing in {close_counter}")

    else:
        print("Please enter y or n")
        continue_again()







number_guessing()
continue_again()
