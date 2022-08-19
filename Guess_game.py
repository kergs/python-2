import random

computer_guess = random.randint(1, 100)
number_of_attempts = 0

while True:
    try:
        user_guess = int(input("Guess the number: "))
        if computer_guess == user_guess:
            number_of_attempts = number_of_attempts + 1
            print(f"You won in {number_of_attempts} attempts.")
            break
        elif user_guess < computer_guess:
            print("Too low, Try again...")
            number_of_attempts = number_of_attempts + 1
        else:
            print("Too high, Try again...")
            number_of_attempts = number_of_attempts + 1
    except:
        print("choose number between 1 to 100...")