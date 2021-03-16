# RPS Component 3 - compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options

        if comp_choice == user_choice:
            result = "its a tie"

        elif user_choice == "rock":
            if comp_choice == "paper":
                result = "you lose"
            else:
                result = "you win"

        elif user_choice == "paper":
            if comp_choice == "scissors":
                result = "you lose"
            else:
                result = "you win"

        elif user_choice == "scissors":
            if comp_choice == "rock":
                result = "you lose"
            else:
                result = "you win"

        print("You chose {}, the computer chose {}"
              " Result {} ". format(user_choice, comp_choice, result))
    comp_index += 1
    print()