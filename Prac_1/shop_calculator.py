num_items = int(input("Enter the number of items: "))
total_price = 0

for i in range(num_items):
    item_price = float(input("Enter the price of item {}: ".format(i+1)))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9  # Apply 10% discount for orders over $100

print("Total price for {} items: ${:.2f}".format(num_items, total_price))
