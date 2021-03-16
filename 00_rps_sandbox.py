import random

# Functions
def choice_checker(question):

    error = "Please Choose from Rock / Paper / Scissors " \
            "(or 'xxx' to quit)"

    valid = False
    while not valid:

        # ask user for choice (.lower choice)
        response = input(question).lower()

        # if response is too high
        if response =="r" or response == "rock":
            return "rock"
        elif response =="p" or response == "paper":
            return "paper"
        elif response =="s" or response == "scissors":
            return "scissors"

        # checks exit code
        elif response == "xxx":
            return response

        else:
            print(error)



# main routine
options = ["rock", "paper", "scissors"]

valid = False
while not valid:
    user = choice_checker("Rock Paper Scissors: ")
    comp = random.choice(options)

    if user == comp:
        result = "tie"
    elif user == "paper" and comp == "rock":
        result = "you win"
    elif user == "rock" and comp == "scissors":
        result = "you win"
    elif user == "scissor" and comp == "paper":
        result = "you win"
    else:
        result = "you lose"


    print("{} vs {} - {}".format(user, comp, result))


