# Importing necessary classes
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def taxi_simulator():
    """Main function for taxi simulator."""
    print("Let's drive!")
    total_bill = 0.0  # Total bill for the user
    current_taxi = None  # Current taxi that the user is using
    # List of available taxis
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        # Print the menu options
        print("q)uit, c)hoose taxi, d)rive")
        user_input = input(">>> ").lower()

        if user_input == 'q':
            # User wants to quit the program. Print the total cost and the final state of the taxis.
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            break
        elif user_input == 'c':
            # User wants to choose a taxi. Display the list of available taxis and ask for the user's choice.
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < len(taxis):
                # The user's choice is valid. Set the current taxi to the chosen one.
                current_taxi = taxis[taxi_choice]
            else:
                # The user's choice is invalid. Print an error message.
                print("Invalid taxi choice")
        elif user_input == 'd':
            # User wants to drive the taxi. Check if a taxi has been chosen.
            if current_taxi:
                # A taxi has been chosen. Ask the user for the driving distance and drive the taxi.
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                total_bill += trip_cost  # Add the trip cost to the total bill
            else:
                # No taxi has been chosen. Print an error message.
                print("You need to choose a taxi before you can drive")
        else:
            # The user's input does not match any of the menu options. Print an error message.
            print("Invalid option")

        # Print the bill up to the current moment.
        print("Bill to date: ${:.2f}".format(total_bill))


if __name__ == '__main__':
    taxi_simulator()
