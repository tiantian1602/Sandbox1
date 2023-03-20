MIN_LENGTH = 8

while True:
    password = input("Enter a password: ")
    if len(password) < MIN_LENGTH:
        print("Password must be at least", MIN_LENGTH, "characters long")
    else:
        print("*" * len(password))

