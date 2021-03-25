import random

# Functions


# Statement Generator
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Checks rounds or infinite mode
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
                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


# Checks either Rock paper or scissors
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


# Checks for yes or no response
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Instructions
def instructions():
    statement_generator("How to play", "?", "-")
    print()
    print("Choose a number of rounds you would like to play or")
    print("press <enter> for infinite mode.")
    print()
    print("Choose between either Rock, paper, or scissors and ")
    print("see what the computer choose and if you won lost or")
    print("tie.")
    print()
    print("You can Type r, p, s, instead of the whole word to ")
    print("save time.")
    print()
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats Rock")
    print()
    print("Type 'xxx' to quit when ever you feel and see your ")
    print("game history at the end of the game ")
    print()
    statement_generator("Have fun!", "!", "^")
    print()
    return ""


# Main Routines

# Welcome statement
statement_generator("Welcome to Rock Paper Scissors", "!", "=")
print()


# Valid response lists
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
game_summary = []
round_summary = []


# Ask user if they have played before.
played_before = yes_no("Have you played this game before? ")
print()

# If 'no' show instructions
if played_before == "no":
    instructions()

# Ask user for # of rounds, <enter> for infinite mode

rounds_played = 0

# So the scoring is reset
rounds_lost = 0
rounds_drawn = 0

# If user doesnt play game
result = "Quitter"

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

    statement_generator(heading,  "|", "=")
    print()

    choose_instruction = "Please choose rock, paper" \
                         ", scissors " \
                         "or 'xxx' to exit: "

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
        result = "Tie"
        rounds_drawn += 1
        top_dec = "-"
    elif choose == "paper" and comp_choice == "rock":
        result = "Won"
    elif choose == "rock" and comp_choice == "scissors":
        result = "Won"
    elif choose == "scissors" and comp_choice == "paper":
        result = "Won"
    else:
        result = "Lost"
        rounds_lost += 1
        top_dec = "v"

    if result == "Won":
        top_dec = "*"

    # Add result to list
    game_summary.append("Round #{}: {}".format(rounds_played + 1, result))

    # Feedback
    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(choose, comp_choice, result)

    # rest of loop / game
    print()
    print("You chose | {} |".format(choose))
    print("Comp chose | {} |".format(comp_choice))
    print()
    statement_generator(feedback, "!", top_dec)

    rounds_played += 1

    # Show game statistics
    # Quick calculations (stats)
    rounds_won = rounds_played - rounds_lost - rounds_drawn

# If quit on first round
if result == "Quitter":
    print()
    statement_generator("lol didn't want to play :D", "!", "L")

else:
    # **** Calculate Game Stats ****
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    # Displays game stats with % values to the nearest whole number
    print()
    statement_generator("Game Statistics", "*", "-")
    print("Win: {}, ({:.0f}%)\n"
          "Loss: {}, ({:.0f}%)\n"
          "Tie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                      percent_lose, rounds_drawn, percent_tie))
    print()

    # Ask user if they want to see there game history
    # If 'yes' show game history
    show_history = yes_no("Do you want to see your game history? ")
    print()
    if show_history == "yes":
        statement_generator("Game History", "*", "-")
        for item in game_summary:
            print(item)

        print()
        statement_generator("Thanks for playing :)", "!", "=")
    else:
        statement_generator("Thanks for playing :)", "!", "=")