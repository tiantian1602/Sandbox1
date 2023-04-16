# Define a dictionary of colour names and their hexadecimal codes
COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Prompt the user to enter a colour name
color_name = input("Enter a color name (or blank to stop): ")

# Loop until the user enters a blank line
while color_name.strip() != "":
    # Look up the color in the dictionary (case-insensitive)
    hex_code = COLOR_TO_HEX.get(color_name.title())
    if hex_code is not None:
        print(f"The hexadecimal code for {color_name.title()} is {hex_code}.")
    else:
        print(f"Sorry, {color_name.title()} is not a valid color name.")

    # Prompt the user to enter another colour name
    color_name = input("Enter a color name (or blank to stop): ")
