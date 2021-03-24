# Taken from Lucky Unicorn Game
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine

statement_generator("Welcome to Rock Paper Scissors", "!", "=")
print()
statement_generator("Game History", "?", "=")