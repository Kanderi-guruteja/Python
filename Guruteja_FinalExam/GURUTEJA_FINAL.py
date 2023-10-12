import random
# Function to get a random card value from a standard deck of 52 cards
def get_random_card():
    random_card = random.randint(1, 13)  # Randomly select a card value from 1 to 13
    if random_card <= 10:
        return random_card
    elif random_card == 11:
        return 11
    else:
        return 10

# Function to calculate the total score of a player's cards
def calculate_total_score(cards):
    total_score = sum(cards)  # Calculate the sum of card values
    if total_score > 21 and 11 in cards:  # Check if total score is greater than 21 and there is an Ace (11) in the cards
        cards.remove(11)  # Replace Ace (11) with Ace (1)
        cards.append(1)
        total_score = sum(cards)  # Recalculate the total score with the new Ace value (1)
    return total_score

# Function to display the player's cards with a visual separation between each card
def display_cards(player_name, cards):
    card_strings = [str(card) for card in cards]
    cards_display = " - ".join(card_strings)  # Join cards with '-' separator
    print(f"{player_name}'s cards: {cards_display}, Score: {calculate_total_score(cards)}")

# Function to get the player's choice of whether to take another card
def get_player_choice(player_name):
    while True:
        try:
            print(f"{player_name}, do you want another card? (y/n):")
            player_choice = input().lower()
            if player_choice == 'y' or player_choice == 'n':
                return player_choice == 'y'
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input! Please enter 'y' or 'n'.")

# Function to play the game
def play_game(player1_name="Player 1", player2_name="Player 2"):
    # Initialize initial cards for each player
    player1_cards = [get_random_card(), get_random_card()]
    player2_cards = [get_random_card(), get_random_card()]

    while True:
        # Display player cards with spacing after each card is shown
        display_cards(player1_name, player1_cards)
        # print("*******************************")  # Visual separation between turns
        display_cards(player2_name, player2_cards)
        # print("*******************************")  # Visual separation between turns

        # Check if any player's score is above 21
        if calculate_total_score(player1_cards) > 21:
            print(f"{player1_name} busts.")
            winner = player2_name
            break
        elif calculate_total_score(player2_cards) > 21:
            print(f"{player2_name} busts.")
            winner = player1_name
            break

        # Ask players for their choices
        player1_choice = get_player_choice(player1_name)
        if player1_choice:
            player1_cards.append(get_random_card())

        player2_choice = get_player_choice(player2_name)
        if player2_choice:
            player2_cards.append(get_random_card())

    # Compare scores and determine the winner
    player1_score = calculate_total_score(player1_cards)
    player2_score = calculate_total_score(player2_cards)

    print("*******************************")  # Visual separation before displaying final scores
    print("Final Scores are:") #Prints the Final scores before announcing winner
    display_cards(player1_name, player1_cards)
    display_cards(player2_name, player2_cards)

    if player1_score > 21 and player2_score > 21:
        winner = "Tie"
    elif player1_score > 21:
        winner = player2_name
    elif player2_score > 21:
        winner = player1_name
    elif player1_score == player2_score:
        winner = "Tie"
    else:
        winner = player1_name if player1_score > player2_score else player2_name

    return winner

if __name__ == "__main__":
    print("Welcome to Python Card Game!")
    print("************************")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    winner = play_game(player1_name, player2_name)

    # Print below statement if the condition is Tie
    if winner == "Tie":
        print("It's a tie!")
    else:
        # Print the below statement if the condition is not a tie
        print(f"Congratulations! {winner} you won!!")
