import random

# Functions


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more the 0"

        # If infinite mode not chosen, check response
        # is an interger that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is to low, go back to
                # start of loop
                if response < 1 :
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue


        return response


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


# Main Routines


# Vaild response lists
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]


# ask user if they have played before.
# If 'no' show instructions


# Ask user for # of rounds, <enter> for infinite mode

rounds_played = 0

# So the scoring is reset
rounds_lost = 0
rounds_drawn = 0

rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    # Checks if Its continuous mode or rounds mode
    print()
    if rounds == "":
        heading = "Continuous Mode:" \
                  " Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        # End game when number of rounds finished
        if rounds_played == rounds - 1:
            end_game = "yes"

    print(heading)

    choose_instruction = "Please choose rock, paper" \
                         ", scissors " \
                         "or 'xxx' to exit "

    choose_error = "Please choose from Rock, " \
                   "Paper or Scissors (or 'xxx' to quit)"


    # Computer choice
    comp_choice = random.choice(rps_list[:-1])

    # Ask user for rock paper scissors
    choose = choice_checker(choose_instruction, rps_list,
                                     choose_error)

    # end game if exit code is typed or rounds are finished
    if choose == "xxx":
        break

    # Compare choices

    if choose == comp_choice:
        result = "tie"
        rounds_drawn += 1
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    # Feedback
    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(choose,
                                              comp_choice, result)

    # rest of loop / game
    print("You chose {}".format(choose))
    print("Comp chose {}".format(comp_choice))
    print()
    print(feedback)

    rounds_played += 1


    # Ask user if they want to see there game history
    # If 'yes' show game history

    # Show game statistics
    # Quick calculations (stats)
    rounds_won = rounds_played - rounds_lost - rounds_drawn
    print("rounds won", rounds_won)

print()
print("***** End Game Summary *****")
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")
