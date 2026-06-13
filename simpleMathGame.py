# Simple Math Game
# This program allows a student to practise arithmetic questions.
# The student can choose addition, subtraction, multiplication, division, or a random mix of all question types.

import random

def menu():
    # Display the menu and return the user's choice.
    print("[1]Addition problems only")
    print("[2]Subtraction problems only")
    print("[3]Multiplication problems only")
    print("[4]Division  problems only")
    print("[5]Randomly intermix problems only")

    # Read the user's choice.
    choice = int(input("Enter choice: "))

    return choice

def print_incorrect_msg():
    # Display a random message when the answer is incorrect.
    incorrect = [
        'No. Please try again.',
        'Wrong. Try once more.',
        'Don’t give up!',
        'No. Keep trying.'
    ]

    print(random.choice(incorrect))

def print_correct_msg():
    # Display a random message when the answer is correct.
    correct = [
        'Very good!',
        'Excellent!',
        'Nice work!',
        'Keep up the good work!'
    ]

    print(random.choice(correct))

def ask_questions(choice):
    # Generate two random numbers between 1 and 10.
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    # If option 5 is chosen, randomly select a question type.
    if choice == 5:
        choice = random.randint(1,4)

    # Create the question and calculate the correct answer.
    if choice == 1:
        q = f'How much is {n1} + {n2}? '
        ans = n1 + n2

    elif choice == 2:
        q = f'How much is {n1} - {n2}? '
        ans = n1 - n2

    elif choice == 3:
        q = f'How much is {n1} * {n2}? '
        ans = n1 * n2

    else:
        # Create a division question with a whole-number answer.
        ans = random.randint(1,10)
        n2 = random.randint(1,10)
        n1 = ans * n2

        q = f'How much is {n1} / {n2}? '

    # Keep asking until the correct answer is entered.
    while True:
        user_ans = float(input(q))

        if user_ans == ans:
            # Display a positive message for a correct answer.
            print_correct_msg()
            break

        else:
            # Encourage the student to try again.
            print_incorrect_msg()

# Main program

# Display the menu and get the user's choice.
choice = menu()

# Ask a question based on the selected option.
ask_questions(choice)