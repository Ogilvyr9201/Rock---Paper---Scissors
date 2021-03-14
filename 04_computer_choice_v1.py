import random

# main routine

rps_list = ["rock", "paper", "scissors",]

#  testing loop generate 20 tokens
for item in range(0, 20):
    comp_choice = random.choice(rps_list)
    print(comp_choice)