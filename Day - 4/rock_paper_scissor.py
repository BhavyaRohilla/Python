import random

# Symbols
rock = " 🗿 Rock"
paper = "📄 Paper"
scissors = "✂️ Scissors"

# Store in a list
game_choices = [rock, paper, scissors]

# Ask user for input
print("What do you choose?")
print("0 for Rock  🗿")
print("1 for Paper 📄")
print("2 for Scissors ✂️")

# Get user input
user_choice = int(input("Enter your choice (0/1/2): "))

# 🛡️ Check if input is valid
if user_choice < 0 or user_choice > 2:
    print("❌ Invalid input! Please enter 0, 1, or 2.")
else:
    # Computer randomly chooses
    computer_choice = random.randint(0, 2)

    # Show both choices
    print("\nYou chose:", game_choices[user_choice])
    print("Computer chose:", game_choices[computer_choice])

    # Decide the winner
    if user_choice == computer_choice:
        print("It's a draw! 🤝")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! 🎉")
    elif user_choice == 1 and computer_choice == 0:
        print("You win! 🎉")
    elif user_choice == 2 and computer_choice == 1:
        print("You win! 🎉")
    else:
        print("Computer wins! 💻🏆")
