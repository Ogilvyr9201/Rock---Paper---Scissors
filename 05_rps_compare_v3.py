# RPS Component 3 - compare user choice and computer choice


# V2 uses 3 'if' statements
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options

        if comp_index == user_index:
            result = "tie"
        elif comp_index == user_index + 1 or user_index - 1:
            result = "lose"
        elif comp_index == user_index + 2 or user_index - 2:
            result = "win"


        print("You chose {}, the computer chose {}"
              " Result: {} ". format(user_choice, comp_choice, result))
    comp_index += 1
    print()