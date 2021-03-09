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
            return response
        elif response =="p" or response == "paper":
            return response
        elif response =="s" or response == "scissors":
            return response

        # checks exit code
        elif response == "xxx":
            return response

        else:
            print(error)



# main routine
rps = choice_checker("Rock Paper Scissors: ")

print
print("You choose {}".format(rps))