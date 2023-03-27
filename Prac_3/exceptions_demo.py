"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when the user enters a non-numeric value for either the numerator or denominator.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters 0 as the value for the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you could add an if statement to check if the denominator is zero before performing the division
operation, and then print an appropriate message instead of raising an error.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")