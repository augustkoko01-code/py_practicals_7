# User Authentication
# A Python program that reads account information from a text file and authenticates user login credentials. 
# Users have a maximum of 3 attempts to log in successfully before the account is locked.

def read_accounts(accounts):
    # Open the file in read mode
    with open("accounts.txt", 'r') as file:

        # Read the file one line at a time
        for line in file:

            # Remove the new line character (\n)
            # Split the line by comma
            # Example:
            # "peter,pass1" -> ["peter", "pass1"]
            account = line.strip().split(',')

            # Add the account to the accounts list
            accounts.append(account)


def login(user_name, password, accounts):

    # Check every account in the accounts list
    for account in accounts:

        # Compare entered username and password
        # with the username and password in the list
        if user_name == account[0] and password == account[1]:

            # Login is correct
            return True

    # No matching account found
    return False


# Create an empty list
# This list will store all accounts
accounts = []

# Read account data from the file
# and store it in the accounts list
read_accounts(accounts)

# Display a message to the user
print("Please login to your account before proceeding...")

# Start with attempt number 1
attempt = 1

# Allow the user to try 3 times
while attempt <= 3:

    # Ask user to enter username
    user_name = input("Enter your username: ")

    # Ask user to enter password
    password = input("Enter your password: ")

    # Check whether username and password are correct
    if login(user_name, password, accounts):

        # Login successful
        print(f"Hello {user_name.upper()}, you may proceed...")

        # Exit the loop
        break

    else:

        # Login failed
        print("Login incorrect. Please try again...")

        # Increase attempt count by 1
        attempt += 1


# If user used more than 3 attempts
if attempt > 3:

    # Display account locked message
    print("You didn't get it in 3 attempts. Your account is locked.")