# Find Largest Value Program
# This program uses a function to compare two integers and return
# the larger value. It then uses the function repeatedly to find
# the largest integer among four numbers entered by the user.

# Return the larger of two integers.
def find_larger(n, m):
    if n > m:
        return n
    else:
        return m


# Prompt the user to enter four integers.
n1 = int(input("Enter the first integer number: "))
n2 = int(input("Enter the second integer number: "))
n3 = int(input("Enter the third integer number: "))
n4 = int(input("Enter the fourth integer number: "))

# Compare the first two integers.
largest = find_larger(n1, n2)

# Compare the current largest value with the third integer.
largest = find_larger(largest, n3)

# Compare the current largest value with the fourth integer.
largest = find_larger(largest, n4)

# Display the largest integer.
print(f"The largest integer is {largest}")