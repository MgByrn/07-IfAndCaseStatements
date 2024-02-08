###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def color_picker():
    color = input("enter a color:")

   
    if color == "red":
        print("Success! You picked red.")
    elif color == "white":
        print("Success! You picked white.")
    elif color == "blue":
        print("Success! You picked blue.")
    elif color == "green":
        print("Success! You picked green.")
    elif color == "blue":
        print("Success! You picked blue.")
    else:
        print("Unknown Color!")

color_picker()
    

    



###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def grade():
    grade = float(input("Enter grade as a decimal:"))
    if 0.90 <= grade <= 1.00:
        print("You received an A.")
    elif 0.80 <= grade < 0.89:
        print("You received a B.")
    elif 0.70 <= grade < 0.79:
        print("You received a C.")
    elif 0.60 <= grade < 0.69:
        print("You received a D.")
    else:
        print("Invalid score given.")


grade()

