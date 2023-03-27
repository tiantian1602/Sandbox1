#1. Writing to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)
#2. Reading from a file
with open("name.txt", "r") as file:
    name = file.read()
print("Your name is", name)
#3.Adding the first two numbers in a file:
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
result = num1 + num2
print(result)


