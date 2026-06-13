# Square of Characters Program
# This program displays a square pattern using a character
# entered by the user. The size of the square is determined
# by the side length entered by the user.

# Print a row of characters.
def print_character(char, time):

    # Print the character repeatedly on the same line.
    for t in range(time):
        print(char, end='')

    # Move to the next line after the row is completed.
    print()


# Print a square pattern.
def print_square(side, char):

    # Print the required number of rows.
    for s in range(side):
        print_character(char, side)


# Prompt the user to enter the side length and character.
side = int(input("Enter side: "))
char = input("Enter character: ")

# Display the square pattern.
print_square(side, char)