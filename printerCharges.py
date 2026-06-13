# Printer Charges Program
# This program calculates the printing charge for paper usage
# from 0 to 500 pages in steps of 50 pages. It also calculates
# the total amount including 9% GST.

# Calculate the printing charge based on the number of pages.
def calculate_charge(pages):

    # First 100 pages are charged at 3 cents per page.
    if pages <= 100:
        return pages * 0.03

    # Next 200 pages are charged at 2 cents per page.
    elif pages <= 300:
        return (100 * 0.03) + (pages - 100) * 0.02

    # Pages above 300 are charged at 1 cent per page.
    else:
        return (100 * 0.03) + (200 * 0.02) + (pages - 300) * 0.01


# Calculate the amount including 9% GST.
def calculate_gst(amount):
    return amount + (amount * 0.09)


# Display the table heading.
print(f"{'Pages':<12}{'Charge':<12}{'Include GST($)':<12}")

# Generate page counts from 0 to 500 in steps of 50 pages.
for p in range(0, 501, 50):

    # Calculate the printing charge.
    charge = calculate_charge(p)

    # Calculate the total amount including GST.
    gst = calculate_gst(charge)

    # Display the page count, charge, and amount including GST.
    print(f"{p:<12}{charge:<12.2f}{gst:<12.2f}")