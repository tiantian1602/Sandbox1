import random

NUM_QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUMBERS_PER_PICK = 6


# Function to generate a single random quick pick
def generate_quick_pick():
    # Create a list of all possible numbers
    all_numbers = list(range(MIN_NUM, MAX_NUM + 1))

    # Randomly select 6 unique numbers from the list
    quick_pick = random.sample(all_numbers, k=NUMBERS_PER_PICK)

    # Sort the numbers in ascending order and return as a string
    return " ".join(str(num) for num in sorted(quick_pick))


# Get the number of quick picks to generate from the user
num_picks = int(input("How many quick picks? "))

# Generate and print each quick pick
for i in range(num_picks):
    quick_pick = generate_quick_pick()
    print(quick_pick)
