import random
def get_choices():
    options = ["rock", "scissors", "paper"]
    while True:
        player_choice = input("Please enter 'rock', 'paper' or 'scissors': ").lower()
        if player_choice in options:
            break
        print("Invalid input. You must enter 'rock', 'paper' or 'scissors'.")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print (f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It´s a tie"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock. You lose."

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You win!"
        else:
            return "Scissors cut paper. You lose."

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper. You win!"
        else:
            return "Rock smashes scissors. You lose."

def run_game():
    while True:
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play?: "))
            except ValueError:
                print("You must enter a number.")
        while game_number < games_to_play:
            game_number += 1
            print(f"Game {game_number} of {games_to_play}")
            choices = get_choices()
            result = check_win(choices["player"], choices["computer"])
            print(result)

            if game_number < games_to_play:
                input("\nPress enter for another game round... ")

        while True:
            reply = input("Do you want to play another session? ")
            if reply in ["yes", "y"]:
                break
            elif reply in ["no", "n"]:
                print("Thanks for playing! Goodbye!:)")
                return
            else:
                print("Invalid input. Please answer 'yes' or 'no'(or y/n).")

if __name__ == "__main__":
    run_game()


