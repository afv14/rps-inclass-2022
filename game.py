
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

#welcome message
print("------------")
print("Welcome to my rock Rock-Paper-Scissors game...")
print("------------")

#ask for Player One Name
username = input("Let's get to know each other a little bit. What should I call you? Please enter your name below:")

# ask for use inputs
#???why can't I put a variable into my input box? To use the string stored in the username variable?
user_choice = input("Now that we've exchanged pleasantries let's get started! Please choose one of the following:  'rock', 'paper', 'scissors': ")
print("------------")


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
#???I want it to look back to the input at the beginning
else:
    print("You have entered an invalid input. Please make sure you enter one of the following selections: 'rock', 'paper', 'scissors'!")
    quit()

print(username, "chose:", user_choice)

# computer choice
#import random
import random

#create a list
computer_options = ["rock","paper","scissors"]

#randomize selection
computer_choice = random.choice(computer_options)
print("The computer chose:", computer_choice)
print("------------")

#determine the winner
if computer_choice == user_choice:
    print(username,"you both chose",computer_choice,"it's a tie! Thanks for playing!")
elif computer_choice == "rock":
    if user_choice == "paper":
        print("Paper covers rock, congratulations", username, "you won!")
    elif user_choice == "scissors":
        print("Oops. Rock crushes scissors. Sorry", username, "you lost! Try your luck next time!")
elif computer_choice == "paper":
    if user_choice == "scissors":
        print("Scissors cut paper, congratulations", username, "you won!")
    elif user_choice == "rock":
        print("Oops. Paper covers rock. Sorry", username, "you lost! Try your luck next time!")
elif computer_choice == "scissors":
    if user_choice == "rock":
        print("Rock crushes scissors, congratulations", username, "you won!")
    elif user_choice == "paper":
        print("Oops. Paper is cut by scissors. Sorry", username, "you lost! Try your luck next time!")

#thanks message at end
print("------------")
print("Thanks for playing", username, "Come back and visit again!")
    



#final result


#let user pick their name
