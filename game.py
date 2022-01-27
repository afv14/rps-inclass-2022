
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ask for use inputs
user_choice = input("Let's get started! Please choose one of the following:  'rock', 'paper', 'scissors': ")

print("You chose", user_choice)


# validate inputs
if user_choice == "Rock":
    user_choice = "rock"
elif user_choice == "ROCK":
    user_choice = "rock"
elif user_choice == "rock":
    user_choice = "rock"
elif user_choice == "Paper":
    user_choice = "paper"
elif user_choice == "PAPER":
    user_choice = "paper"
elif user_choice == "paper":
    user_choice = "paper"
elif user_choice == "Scissors":
    user_choice = "scissors"
elif user_choice == "SCISSORS":
    user_choice = "scissors"
elif user_choice == "scissors":
    user_choice = "scissors"
else:
    print("Please choose one of the following selections: 'rock', 'paper', 'scissors'!")
    quit()
#I have to get it to loop around so that it keeps asking the user for an input
#not done with this section


# computer choice



#determine the winner


#final result


#let user pick their name
