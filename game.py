
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

#welcome message
print("------------")
print("Welcome to my rock Rock-Paper-Scissors game...")
print("------------")

#Let the player input their name
import os

username = os.getenv("USERNAME", default="Player One")

# ask for use inputs
#???why can't I put a variable into my input box? To use the string stored in the username variable? 
#Had to use a formatted string (indicated by the f below) to insert the environment variable
user_choice = input(f"Let's get started! {username} choose one of the following:  'rock', 'paper', 'scissors': ")
print("------------")


# validate inputs
#switch capitalization of rock
#Eugenie Chandon-Moet gave me this line of code, I originally had if statements that transformed the strings passed through it.
user_choice = user_choice.lower()

#if input invalid send a message and quit the program
#???I want it to look back to the input at the beginning
#going to practice this with next project
if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("You have entered an invalid input. Please make sure you enter one of the following selections: 'rock', 'paper', 'scissors'!")
    exit()

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
#final result included in the logic that determines the winner
if computer_choice == user_choice:
    print(username,"it looks like both of you chose",computer_choice,"it's a tie!")
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
print("Thanks for playing", username, "come back and visit again!")
    

