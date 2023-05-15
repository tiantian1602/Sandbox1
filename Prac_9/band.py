class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Have all musicians in the band play their instruments."""
        return '\n'.join(musician.play() for musician in self.musicians)
