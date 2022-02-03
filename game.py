
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ask for use inputs
user_choice = input("Let's get started! Please choose one of the following:  'rock', 'paper', 'scissors': ")

print("You chose", user_choice)


# validate inputs
#switch capitalization of rock
if user_choice == "Rock":
    user_choice = "rock"
elif user_choice == "ROCK":
    user_choice = "rock"
#switch capitalization of paper
elif user_choice == "Paper":
    user_choice = "paper"
elif user_choice == "PAPER":
    user_choice = "paper"
#switch capitalization of scissors
elif user_choice == "Scissors":
    user_choice = "scissors"
elif user_choice == "SCISSORS":
    user_choice = "scissors"
#if input invalid send a message and quit the program
#I want it to look back to the input at the beginning
else:
    print("You have entered an invalid input. Please make sure you enter one of the following selections: 'rock', 'paper', 'scissors'!")
    quit()

print(user_choice)

# computer choice
computer_options = ["rock","paper","scissors"]
computer_choice = random(computer_options)
print(computer_choice)




#determine the winner


#final result


#let user pick their name
