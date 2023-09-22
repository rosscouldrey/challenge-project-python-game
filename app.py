#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#rules
##Rock beats scissors (breaking it).
#Scissors beat paper (cutting it).
#Paper beat rock (wrapping it).

#set up score variables
user_score = 0
computer_score = 0

#write welcome message to console
print("Hello Quinn! \n Welcome to Rock, Paper, Scissors!")

#write rules to console
print("Rules:")
print("\tRock beats scissors (breaking it).")
print("\tScissors beat paper (cutting it).")
print("\tPaper beat rock (wrapping it).")

#write directions to end game
print("\nTo end the game, enter 'n' when asked to play again.")

#get play_again variable
play_again = input("Would you like to play? (y/n): ")

while play_again.lower() != "n":
    #set user selection variable
    user_selection = input("\nEnter Rock, Paper, or Scissors: ")
    #convert user selection to lowercase
    user_selection = user_selection.lower()

    #validate user_selection   
    while user_selection != "rock" and user_selection != "paper" and user_selection != "scissors":

        print("You did not select Rock, Paper, or Scissors. Please try again.\n")
        user_selection = input("Enter Rock, Paper, or Scissors: ")
        #convert user selection to lowercase
        user_selection = user_selection.lower()

    #end while

    #set computer selection variable as a random value between 1 and 3
    import random
    computer_selection = random.randint(1,3)

    #if computer selection = 1 then rock, if 2 then paper, if 3 then scissors
    if computer_selection == 1:
        computer_selection = "rock"
    elif computer_selection == 2:
        computer_selection = "paper"
    elif computer_selection == 3:
        computer_selection = "scissors"
    #end if

    #print "you selected" and user selection
    print("Quinn selected " + user_selection)

    #print "computer selected" and computer selection
    print("Computer selected " + computer_selection)

    #determine winner
    if user_selection == computer_selection:
        print("It's a tie!")
    elif user_selection == "rock" and computer_selection == "paper":
        print("Paper beats rock. You lose!")
        #increase computer score by 1
        computer_score = computer_score + 1
    elif user_selection == "rock" and computer_selection == "scissors":
        print("Rock beats scissors. You win!")
        #increase user score by 1
        user_score = user_score + 1
    elif user_selection == "paper" and computer_selection == "rock":
        print("Paper beats rock. You win!")
        #increase user score by 1
        user_score = user_score + 1
    elif user_selection == "paper" and computer_selection == "scissors":
        print("Scissors beats paper. You lose!")
        #increase computer score by 1
        computer_score = computer_score + 1
    elif user_selection == "scissors" and computer_selection == "rock":
        print("Rock beats scissors. You lose!")
        #increase computer score by 1
        computer_score = computer_score + 1
    elif user_selection == "scissors" and computer_selection == "paper":
        print("Scissors beats paper. You win!")
        #increase user score by 1
        user_score = user_score + 1
    #end if

    #ask user to play again?
    play_again = input("\nWould you like to play again? (y/n): ")

#write user score to console
print("Quinn's score: " + str(user_score))

#write computer score to console
print("Computer score: " + str(computer_score))

#if user_score + computer_score > 0 then write proportion of user wins to console
if user_score + computer_score > 0:
    print("Win %: " + str(user_score / (user_score + computer_score)*100) + "%")   

#write goodbye message to console
print("Thanks for playing!")