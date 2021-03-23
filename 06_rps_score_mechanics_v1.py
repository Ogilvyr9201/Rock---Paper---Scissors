# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0
rounds_won = 0

# Results for testing purposes
test_results = ["won", "won", "lose", "lose", "tie"]

# Play game
for item in test_results:
    rounds_played += 1

    # Generate computer choice


    result = item

    if item == "tie":
        result = "its a tie"
        rounds_drawn += 1
    elif result == "lose":
        rounds_lost += 1

# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End game statements
print()
print("***** End Game Summary *****")
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")
