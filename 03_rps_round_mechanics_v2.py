# function used to check input is valid

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more the 0"

        if response != "":
            try:
                response = int(response)

                if response < 1 :
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue


        return response

# Main routine

rounds_played = 0
choose_instruction = "Please choose rock (r), paper " \
                     "(p), scissors (s)"


# Ask user for # of rpunds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode Round:" \
                  "Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    # end game if exit code is typed or rounds are finished
    if choose == "xxx":
        break

    if rounds_played == rounds - 1:
        end_game = "yes"

    # rest of loop / game
    print("you choose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")
