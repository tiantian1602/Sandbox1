import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        # Initialize object attributes
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        # Convert the start_date attribute to a formatted string
        start_date = self.start_date.strftime("%d/%m/%Y")
        # Return a formatted string representation of the object
        return f"{self.name}, start: {start_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __repr__(self):
        # Convert the start_date attribute to a formatted string
        start_date = self.start_date.strftime("%d/%m/%Y")
        # Return a string representation of the object
        return f"{self.name}, start: {start_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        # Compare two projects based on their priority
        return self.priority < other.priority

    def is_after_certain_time(self, date):
        # Check if the start_date of the project is after a certain time
        return self.start_date >= date
