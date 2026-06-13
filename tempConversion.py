# Celsius to Fahrenheit Conversion Program
# This program converts a temperature from Celsius to Fahrenheit.
# It uses a function to calculate the Fahrenheit equivalent.

# Convert Celsius to Fahrenheit and return the result.
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


# Prompt the user to enter a temperature in Celsius.
celsius = int(input("Enter the temperature in degree Celsius: "))

# Call the function to calculate the Fahrenheit temperature.
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the converted temperature.
print(f"The temperature is equivalent to {fahrenheit} Fahrenheit.")