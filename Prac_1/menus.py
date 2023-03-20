#Pseudocode
"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message  """

#Code


# Get the user's name
name = input("Enter your name: ")

# Display the initial menu
print("Menu:")
print("H - Say hello")
print("G - Say goodbye")
print("Q - Quit")

# Get the user's choice
choice = input("Enter your choice: ")

# Loop until the user chooses to quit
while choice != "Q":
    # Perform the selected task
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid input. Please try again.")

    # Display the menu again and get the user's choice
    print("Menu:")
    print("H - Say hello")
    print("G - Say goodbye")
    print("Q - Quit")
    choice = input("Enter your choice: ")

# Display a final message
print("Finished")


