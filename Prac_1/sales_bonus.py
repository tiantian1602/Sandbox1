"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
#variables
sales = 0.0


#Constants
rate_10 = 0.1
rate_15 = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:

    if sales < 1000:
        bonus_1 = sales * rate_10
        print(bonus_1)
    else:
        bonus_2 = sales * rate_15
        print(bonus_2)
    sales = float(input("Enter sales: $"))
print("Goodbye")



