
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ask for use inputs
user_choice = input("Let's get started! Please choose one of the following:  'rock', 'paper', 'scissors': ")



# validate inputs
#switch capitalization of rock
if user_choice == "Rock":
    user_choice = "rock"
elif user_choice == "ROCK":
    user_choice = "rock"
elif user_choice == "rock":
    user_choice = "rock"
#switch capitalization of paper
elif user_choice == "Paper":
    user_choice = "paper"
elif user_choice == "PAPER":
    user_choice = "paper"
elif user_choice == "paper":
    user_choice = "paper"
#switch capitalization of scissors
elif user_choice == "Scissors":
    user_choice = "scissors"
elif user_choice == "SCISSORS":
    user_choice = "scissors"
elif user_choice == "scissors":
    user_choice = "scissors"
#if input invalid send a message and quit the program
#I want it to look back to the input at the beginning
else:
    print("You have entered an invalid input. Please make sure you enter one of the following selections: 'rock', 'paper', 'scissors'!")
    quit()

print("You chose", user_choice)

# computer choice
#import random
import random

#create a list
computer_options = ["rock","paper","scissors"]

#randomize selection
computer_choice = random.choice(computer_options)
print("The computer chose", computer_choice)


#determine the winner


#final result


#let user pick their name
