import random
import time


print("welcome to python number guessing game")

input("Press hit enter to continue")


def number_guessing():
    RandomNum = random.randint(1, 100)
    lowest_number = 1
    highest_number = 100
    guesses = 0
    is_running = True


    while is_running:

        user_guess = input("Guess your number from 1 to 100: ")

        if user_guess.isdigit():

            user_guess = int(user_guess)
            guesses += 1

            if user_guess < 1 or user_guess > 100:
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