from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, lives):
    if guess > answer:
        print("Too high")
        return lives - 1
    elif guess < answer:
        print("Too low")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return lives


def set_difficulty():
    while True:
        game_difficulty = input("Choose between 'hard' and 'easy' mode: ").lower()
        if game_difficulty == "easy":
            return EASY_LEVEL_TURNS
        elif game_difficulty == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input, please choose either 'hard' or 'easy'.")


def game():
    print("Welcome to the guessing game.")
    print("There is a number between 1 and 100, can you guess it though?")

    answer = randint(1, 100)
    lives = set_difficulty()

    guess = 0

    while guess != answer and lives > 0:

        print(f"You have {lives} attempts remaining.")

        guess = int(input("Make a guess: "))

        lives = check_answer(guess, answer, lives)
        if lives == 0:
            print("You have no attempts remaining. You've lost!")
            return
        elif guess != answer:
            print("Guess again.")


game()
