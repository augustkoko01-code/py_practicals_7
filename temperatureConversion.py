# Temperature Conversion Program
# This program converts temperatures between Fahrenheit and Celsius.
# The user selects a conversion option from the menu.
# The program repeats until the user chooses to exit.


# Display the main menu.
def display_menu():
    print("Temperature Conversion\n[1]Fahrenheit to Celsius\n[2]Celsius to Fahrenheit\n[3]Exit")


# Convert Fahrenheit to Celsius.
def fahr_to_cel(f):
    return (5.0 / 9.0) * (f - 32)


# Convert Celsius to Fahrenheit.
def cel_to_fahr(c):
    return ((9.0 / 5.0) * c) + 32


# Check whether the option is within the valid range.
# Return True if valid, otherwise return False.
def validate_input(option, lower, upper):
    return lower <= option <= upper


# Repeat the program until the user chooses to exit.
while True:

    # Display the menu and get the user's choice.
    display_menu()
    option = int(input("Please enter your option: "))

    # Check whether the option is valid.
    if validate_input(option, 1, 3):

        # Option 1: Convert Fahrenheit to Celsius.
        if option == 1:
            fahr = float(input("Please enter the temperature in Fahrenheit: "))
            cel = fahr_to_cel(fahr)

            print(f"The temperature in Celsius is {cel:.1f} degrees\n")

        # Option 2: Convert Celsius to Fahrenheit.
        elif option == 2:
            cel = float(input("Please enter the temperature in Celsius: "))
            fahr = cel_to_fahr(cel)

            print(f"The temperature in Fahrenheit is {fahr:.1f} degrees\n")

        # Option 3: Exit the program.
        else:
            print("Thank you")
            break

    # Display an error message if the option is invalid.
    else:
        print("Invalid option, please try again\n")