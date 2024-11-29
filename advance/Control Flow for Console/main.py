# # Milestone 1:

import random

# NUM_ROUNDS = 5
# current_round = 0
# score = 0

# while True:
#     current_round += 1

#     if current_round > NUM_ROUNDS:
#         break
#     # Check Rounds
#     print("Welcome to the High Low Game!")
#     print("-------------------------------")

#     user_number = random.randint(1, 100)
#     compute_number = random.randint(1, 100)

#     print("Your Number:", user_number)

#     # Milestone 2:

#     high_low_choice = input("Do you think your number is higher or lower than the computer's? (high/low): ")
#     print(high_low_choice)

#     # Milestone 3:

#     is_user_higher_than_computer: bool = True if user_number > compute_number else False
#     is_user_choice_correct: bool = True if (high_low_choice == "high" and is_user_higher_than_computer) or (high_low_choice == "low" and not is_user_higher_than_computer) else False

#     if is_user_choice_correct:
#         score += 1
#         print("You were right!")
#     else:
#         print("You were wrong!")

#     print("is_user_choice_correct", is_user_choice_correct)
#     print("computer's Number:", compute_number)
#     print("Your total scores are:", score)

# # Milestone 4:
# # Make 3 Rounds:

# # Milestone 5:
# # Adding scores:

# Assignment through Oop:

# Milestone 1:

class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__score = 0
        self.age = age

    def update_score(self, points: int):
        self.__score += points

    def get_score(self) -> int:
        return self.__score


class Game:
    def __init__(self, number_of_rounds: int):
        self.number_of_rounds = number_of_rounds
        self.attempts: int = 0

    def play_round(self, player: Player):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"\nYour number is {player_number}.")
        guess = input("Do you think your number is higher or lower than the computer's? Type 'high' or 'low': ").strip().lower()

        is_human_number_higher_than_computer = player_number > computer_number
        is_user_choice_correct = (
            (guess == "high" and is_human_number_higher_than_computer) or
            (guess == "low" and not is_human_number_higher_than_computer)
        )

        if is_user_choice_correct:
            print("You were right!")
            player.update_score(1)
        else:
            print(f"Aww, that's incorrect. The computer's number was: {computer_number}.")

        self.attempts += 1
        print(f"Your score is now {player.get_score()}.\n")

    def play_game(self, player: Player):
        print("Welcome to the High/Low Game!\n-----------------------")
        while self.attempts < self.number_of_rounds:
            self.play_round(player)
        print(f"\nGame over! Final score for {player.name}: {player.get_score()}.")


# Get user input for name and age
name = input("Enter your name: ").strip()
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid age.")

# Initialize the player and game
player_1 = Player(name=name, age=age)
game_1 = Game(number_of_rounds=5)

# Start the game
game_1.play_game(player_1)
