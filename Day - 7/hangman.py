import random
from hangman_word import word_list
from hangman_art import stages, hangman_logo

print(hangman_logo)
chosen_word = random.choice(word_list)
lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter => ").lower()

    # Replace "_" with guessed letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess not in word, reduce life
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print(stages[lives])

    # Check win
    if "_" not in display:
        end_of_game = True
        print("You Win")
