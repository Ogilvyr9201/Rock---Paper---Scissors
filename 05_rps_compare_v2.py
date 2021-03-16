# RPS Component 3 - compare user choice and computer choice


# V2 uses 5 'if' statements
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options

        if user_choice == comp_choice:
            result = "Tie"
        elif user_choice == "paper" and comp_choice == "rock":
            result = "You Win"
        elif user_choice == "rock" and comp_choice == "scissors":
            result = "You Win"
        elif user_choice == "scissor" and comp_choice == "paper":
            result = "You Win"
        else:
            result = "You Lose"

        print("You chose {}, the computer chose {}"
              " Result: {} ". format(user_choice, comp_choice, result))
    comp_index += 1
    print()