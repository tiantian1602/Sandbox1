def extract_name(email):
    """Extracts the name from an email"""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name_parts = [part.title() for part in name_parts]
    return " ".join(name_parts)

emails_to_names = {}

while True:
    email = input("Email: ")
    if email == "":
        break
    name = extract_name(email)
    is_name_correct = input(f"Is your name {name}? (Y/n)").lower()
    if is_name_correct == "" or is_name_correct == "y":
        emails_to_names[email] = name
    else:
        name = input("Name: ")
        emails_to_names[email] = name

for email, name in emails_to_names.items():
    print(f"{name} ({email})")
