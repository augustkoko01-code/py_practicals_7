# Square of Asterisks Program
# This program displays a solid square made of asterisks.
# The user enters the length of the side, and the program
# prints a square with the same number of rows and columns.

# Print a character multiple times on one line.
def print_character(char, times):
    for i in range(times):
        print(char, end="")

    # Move to the next line after printing the row.
    print()


# Print a square of asterisks.
def print_square(side):

    # Print one row at a time.
    for i in range(side):
        print_character("*", side)


# Prompt the user to enter the side length.
side = int(input("Enter side: "))

# Display the square pattern.
print_square(side)