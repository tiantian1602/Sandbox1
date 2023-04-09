def get_income_input(month):
    income = float(input(f"Enter income for month {month}: "))
    return income

def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    income_list = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = get_income_input(month)
        income_list.append(income)

    print_income_report(income_list)

main()
