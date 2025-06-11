import random


# 🃏 Function to deal a random card from the deck
def deal_card():
    cards = [
        11,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        10,
        10,
        10,
    ]  # 11 is Ace, 10s are face cards
    card = random.choice(cards)
    return card


# 🧮 Function to calculate the score of a hand
def calculate_score(cards):
    # 🔥 Check for a Blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Special code for Blackjack

    # 🛠️ Replace Ace (11) with 1 if score goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# ⚔️ Function to compare final scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "🤝 It's a Draw!"
    elif computer_score == 0:
        return "😵 You Lose! Opponent has Blackjack!"
    elif user_score == 0:
        return "🎉 You Win with a Blackjack!"
    elif user_score > 21:
        return "💥 You went over. You Lose!"
    elif computer_score > 21:
        return "🔥 Opponent went over. You Win!"
    elif user_score > computer_score:
        return "🏆 You Win!"
    else:
        return "🙃 You Lose!"


# 🕹️ Main game loop
def play_game():
    print("🎲 Welcome to Blackjack! 🃏\n")

    user_cards = []
    computer_cards = []
    is_game_over = False

    # 🃙 Deal initial two cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 🎮 User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"🧍 Your cards: {user_cards}, current score: {user_score}")
        print(f"🤖 Computer's first card: {computer_cards[0]}")

        # 👀 Check for end game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "➕ Type 'y' to draw another card, or 'n' to pass: "
            )
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 🧠 Computer's turn: keep drawing until score reaches 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 🧾 Final results
    print(f"\n🧍 Your final hand: {user_cards}, final score: {user_score}")
    print(f"🤖 Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# 🔁 Keep playing as long as user wants
while input("\n🔄 Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
