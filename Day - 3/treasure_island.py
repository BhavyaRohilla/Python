print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision
choice1 = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right": '
).lower()

if choice1 == "left":
    # Second decision
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake. "
        'Type "wait" to wait for a boat. Type "swim" to swim across: '
    ).lower()

    if choice2 == "wait":
        # Third decision
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. "
            "Which color do you choose? "
        ).lower()

        if choice3 == "yellow":
            print("You found the treasure! 🏆 You win!")
        elif choice3 == "red":
            print("It's a room full of fire. 🔥 Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. 🐾 Game Over.")
        else:
            print("You chose a door that doesn't exist. 💀 Game Over.")
    else:
        print("You got attacked by a hungry crocodile while swimming. 🐊 Game Over.")
else:
    print("You fell into a hidden hole. 💀 Game Over.")
