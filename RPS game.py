import random
try_count = 1
print("!Welcome to RPS game!")
while try_count <= 3:   
    player1 = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    player2 = random.choice(possible_actions)
    print(f"\nYou chose {player1}, computer chose {player2}.\n")

    if player1 == player2:
        print(f"Both players selected {player1}. It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    print("How many time you have played: ",try_count, "(MAX : 3)")
    print("=================================================================")
    if play_again.lower() != "y":
        break
    try_count += 1
print("Ty for playing!")

