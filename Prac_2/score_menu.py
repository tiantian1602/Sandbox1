def get_score():
    while True:
        score = float(input("Enter score (0-100): "))
        if score >= 0 and score <= 100:
            return score
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

def print_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")

def show_stars(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        print("*" * int(score / 10))

def main():
    score = get_score()
    while True:
        choice = input("\nEnter choice:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n").lower()
        if choice == "g":
            score = get_score()
        elif choice == "p":
            print_result(score)
        elif choice == "s":
            show_stars(score)
        elif choice == "q":
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please enter G, P, S or Q.")

if __name__ == "__main__":
    main()
