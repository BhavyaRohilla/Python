# 🎨 Importing fancy ASCII art logos and the data of famous people/accounts
from art import logo, vs
from data import data
import random


# 🛠️ Function to format account details into a human-readable sentence
def format_data(account):
    """
    Format the account dictionary into a nice string to show the user.
    Example: "Cristiano Ronaldo, a Footballer, from Portugal"
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


# 🔍 Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    """
    Compare follower counts and return True if user's guess is correct.
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# 🎮 Game Start!
print(logo)
score = 0
game_should_continue = True

# 🔁 Randomly choose the first competitor (B)
account_b = random.choice(data)

# 🧠 Main game loop
while game_should_continue:
    account_a = account_b  # B becomes A for the next round
    account_b = random.choice(data)  # Pick new B

    # 💥 Avoid comparing the same person
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"\n🆚 Compare A: {format_data(account_a)}")
    print(vs)
    print(f"🆚 Compare B: {format_data(account_b)}")

    # 🎯 User makes a guess
    guess = input("👉 Who has more followers? Type 'A' or 'B': ").lower()

    # 📊 Get follower counts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # ✅ Check if the guess is right
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # 🎉 If correct, increase score and continue
    if is_correct:
        score += 1
        print(f"✅ You're right! 🏆 Current score: {score}.\n")
    else:
        game_should_continue = False
        print(f"❌ Oops, that's wrong. 💔 Final score: {score}.\n")
