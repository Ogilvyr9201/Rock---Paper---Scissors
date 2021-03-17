rps_list = ["rock", "scissors", "paper"]

user_index = 1
comp_index = 0


user_choice = rps_list[user_index]
comp_choice = rps_list[comp_index]


print(user_choice)
print(comp_choice)

if comp_index == user_index:
    result = "tie"
elif comp_index == user_index - 2 or user_index + 1:
    result = "win"
elif comp_index == user_index + 2 or user_index - 1:
    result = "lose"



print(result)