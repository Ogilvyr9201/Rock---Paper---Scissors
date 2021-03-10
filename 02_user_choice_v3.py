# Version 3 - checks response is in a given list


# Functions
def choice_checker(question, valid_list, error):



    valid = False
    while not valid:

        # ask user for choice (.lower choice)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error message
        print(error)
        print()

# Main Routine

# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]


# Loop for testing
user_choice = ""
while user_choice != "xxx":

    # Ask user for rock paper scissors
    user_choice = choice_checker("Choose between Rock / Paper "
                                 "/ Scissors r/p/s: ", rps_list,
                                 "Please Choose from Rock / Paper "
                                 "/ Scissors (or 'xxx' to quit)")

    # print out choice
    print("You chose {}".format(user_choice))