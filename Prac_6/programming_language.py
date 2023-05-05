"""
CP1404/CP5632 Practical
Programming Language
Estimate: 20 minutes
Current:  10:20
Finish:   10:50
Actual:   30 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing.title() == "Dynamic"