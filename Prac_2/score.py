import random

def score_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    result = score_result(user_score)
    print(result)

    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    result = score_result(random_score)
    print(result)

if __name__ == "__main__":
    main()
