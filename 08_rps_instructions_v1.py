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


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules go here")
    print()
    return""

# Main routines
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print("Program continues")