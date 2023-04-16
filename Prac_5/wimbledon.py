import csv

def read_csv_file(filename):
    """
    Reads a CSV file and returns a list of rows.
    """
    with open(filename, "r", encoding="utf-8-sig") as csvfile:
        # Use csv.reader to read the file and parse it as CSV
        csvreader = csv.reader(csvfile)
        # Convert the csvreader object into a list of lists
        rows = list(csvreader)
        # Return the list of rows
        return rows

def extract_champions(rows):
    """
    Extracts the champions and the number of times they have won Wimbledon
    from the list of rows, and returns a dictionary mapping champions to
    their number of wins.
    """
    # Create an empty dictionary to store the champions and their wins
    champions = {}
    # Iterate over each row in the list of rows
    for row in rows:
        # The champion's name is in the first column of the row
        champion = row[0]
        # The number of wins is in the second column of the row
        wins = int(row[1])
        # Add the champion and their number of wins to the dictionary
        champions[champion] = wins
    # Return the dictionary of champions and their wins
    return champions

def extract_countries(rows):
    """
    Extracts the countries of the champions from the list of rows, and
    returns a set containing the unique countries in alphabetical order.
    """
    # Create an empty set to store the countries
    countries = set()
    # Iterate over each row in the list of rows
    for row in rows:
        # The country is in the third column of the row
        country = row[2]
        # Add the country to the set of countries
        countries.add(country)
    # Convert the set of countries to a sorted list
    countries_list = sorted(list(countries))
    # Join the countries list into a single string separated by commas
    countries_string = ", ".join(countries_list)
    # Return the string of countries
    return countries_string

def main():
    """
    The main function reads the CSV file, extracts the champions and their
    wins, and extracts the countries of the champions. It then prints the
    champions and their wins, and the countries of the champions.
    """
    # Read the CSV file
    rows = read_csv_file("Wimbledon-Mens-Singles-Champions.csv")
    # Extract the champions and their wins
    champions = extract_champions(rows)
    # Print the champions and their wins
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(champion, wins)
    # Extract the countries of the champions
    countries = extract_countries(rows)
    # Print the countries of the champions
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries)

if __name__ == "__main__":
    main()
