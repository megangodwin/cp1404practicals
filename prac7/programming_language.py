"""
CP1404 Practical 07 
Megan Godwin
"""

class ProgrammingLanguage:

    def __init__(self, name='', typing='', reflection='', year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """returns True/False if the programming lang is dynamically typed or not"""
        if 'dynamic' in self.typing:
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
