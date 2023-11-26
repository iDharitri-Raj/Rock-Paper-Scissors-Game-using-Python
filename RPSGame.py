import random


def get_choices():
    player_choice = input("Enter your choice: ")
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    inputs = {"Player": player_choice, "Computer": computer_choice}
    return inputs


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Paper":
            return "Paper covers Rock! You lose."
        else:
            return "Rock smashes Scissors! You win!"
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers Rock! You win!"
        else:
            return "Scissors cuts Paper! You lose."
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper! You win!"
        else:
            return "Rock smashes Scissors! You lose."


choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)
