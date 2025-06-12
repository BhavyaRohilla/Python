from random import randint
from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Check the user's guess against the answer and return remaining turns."""
    if guess > answer:
        print("📈 Too high! Try a smaller number.")
        return turns - 1
    elif guess < answer:
        print("📉 Too low! Try a bigger number.")
        return turns - 1
    else:
        print(f"🎉 Correct! The answer was {answer} 🎯")


def set_difficulty():
    """Set the difficulty level."""
    level = input("Choose a difficulty. Type 'easy' 🐣 or 'hard' 💀: ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100 🤔")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\n🔢 You have {turns} attempts left to guess the number.")
        try:
            guess = int(input("👉 Enter your guess: "))
        except ValueError:
            print("🚫 Please enter a valid number!")
            continue

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("😢 You've run out of guesses. Game Over!")
            print(f"The number was {answer} 💡")
            return
        elif guess != answer:
            print("🔁 Guess again!")


game()
