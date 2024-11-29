# Number gussing game:

# generate random number:

import random

random_generated_number = random.randint(1, 100)

allowed_attempts: int = 5

user_attempt: int = 0

# while loop:
while True:
    print(f"Attempts Left: {allowed_attempts - user_attempt}")

    if (user_attempt == allowed_attempts):
        print("Game Over")
        break

    # user input:
    user_input = int(input("Guess Number between 1-100 "))
    user_attempt += 1

    # if statement:
    if user_input == random_generated_number:
        print("Congrats! The number was:", random_generated_number)
        break
    elif user_input < random_generated_number:
        print("Too Low")
    elif user_input > random_generated_number:
        print("Too High")
    else:
        print("Invalid Input")
        break







 