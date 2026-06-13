# Parcel Delivery Charge Program
# This program calculates the delivery charge for a parcel
# based on its weight and whether express delivery is selected.

def calculate_base_charge(weight):
    # Return the standard delivery charge based on parcel weight.
    if weight <= 2:
        return 3.00
    elif weight <= 5:
        return 5.50
    elif weight <= 10:
        return 8.00
    else:
        return 12.00


def calculate_express_surcharge(base_charge, express):
    # Return the surcharge amount for express delivery.
    if express:
        # Express delivery adds a 25% surcharge.
        return base_charge * 0.25
    else:
        return 0.00


def display_delivery_summary(weight, base_charge, surcharge, total):
    # Display the parcel details and delivery charges.
    print(f"Parcel weight: {weight:.1f} kg")
    print(f"Base charge  : ${base_charge:.2f}")
    print(f"Surcharge    : ${surcharge:.2f}")
    print(f"Total charge : ${total:.2f}")


# Prompt the user to enter the parcel weight in kilograms.
weight = float(input("Enter parcel weight (kg): "))

# Prompt the user to choose express delivery (y or n).
choice = input("Express delivery (y/n): ").lower()

# Convert the user's choice into a Boolean value.
# True if the user enters 'y', otherwise False.
express = (choice == 'y')

# Calculate the standard delivery charge.
base_charge = calculate_base_charge(weight)

# Calculate the express delivery surcharge.
surcharge = calculate_express_surcharge(base_charge, express)

# Calculate the total delivery charge.
total = base_charge + surcharge

# Display the delivery summary.
display_delivery_summary(weight, base_charge, surcharge, total)