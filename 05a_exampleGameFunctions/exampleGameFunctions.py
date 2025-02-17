# Example Game Functions Project, Kristopher Cooper v2
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock/paper/scissors):\n").lower()

    if user_choice not in choices:
        print("Invalid choice, Please try again.:")
        play_game()

    print("Computer chose:", computer_choice)
    print("You chose:", user_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice =='scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == "scissors" and computer_choice == 'paper'):
        print("You win!")
        global user_score
        user_score += 1
    else:
        print("Computer wins")
        global computer_score
        computer_score += 1

    print("Score: You", user_score, "- Computer", computer_score)    

    play_again = input("Do you want to play again? (yes/no):\n").lower()
    if play_again == 'yes' or "y":
        play_game()
    else:
        print("Thanks for playing!")
# Initialize scores
user_score = 0
computer_score = 0

play_game()


# Code Review by Gabriel Coffey

# Line 32 to 36: You always play again even if you decline.

# The code below was an attempted fix(It dosen't work)

#play_again = input("Do you want to play again? (yes/no):\n").lower()
    #if play_again == 'yes' or "y":
   #     play_game()
   # elif play_again == 'no' or "n":
   #      print("Thanks for playing!")