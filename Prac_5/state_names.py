"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Define a dictionary that maps state codes to their full names.
code_to_name = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary to show the mapping between state codes and full names.
print(code_to_name)

# Prompt the user to enter a state code and look up its corresponding full name.
state_code = input("Enter short state: ")
while state_code != "":
    if state_code in code_to_name:
        print(state_code, "is", code_to_name[state_code]) # Print the state code and its corresponding full name.
    else:
        print("Invalid short state") # Print an error message if the state code is not found in the dictionary.
    state_code = input("Enter short state: ") # Prompt the user to enter another state code.

