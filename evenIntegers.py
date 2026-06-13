# Even Integers Program
# This program generates 5 random integers between 1 and 100.
# It uses a function to determine whether each number is even or odd.

import random

# Return True if the number is even, otherwise return False.
def is_even(n):
    return n % 2 == 0


# Generate and check 5 random integers.
for i in range(5):

    # Generate a random integer between 1 and 100.
    num = random.randint(1, 100)

    # Display whether the number is even or odd.
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")