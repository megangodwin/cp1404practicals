"""
CP1404 Practical 07 
Megan Godwin
"""

class Guitar:



    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        CURRENT_YEAR = 2017
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
