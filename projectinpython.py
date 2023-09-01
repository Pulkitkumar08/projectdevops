import random
def get_player_choice():
    while True
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.");

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]);
def main():
    print("Welcome to Rock, Paper, Scissors!")
        elif mode == "computer vs. computer":
            computer1_choice = get_computer_choice()
            computer2_choice = get_computer_choice()
            print(f"Computer 1 chose {computer1_choice}.")
            print(f"Computer 2 chose {computer2_choice}.")
            print(determine_winner(computer1_choice, computer2_choice))
        elif mode == "computer vs. player":
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            printf(f"Player chose {player_choice}.")
            print(f"Computer chose {computer_choice}.")
            print(determine_winner(player_choice, computer_choice))
        elif mode == "player vs. player":
            player1_choice = get_player_choice()
            player2_choice = get_player_choice()
            print(f"Player 1 chose {player1_choice}.")
            print(f"Player 2 chose {player2_choice}.")
            print(determine_winner(player1_choice, player2choice))
        else:
            print("Invalid mode. Please choose a valid mode.")
