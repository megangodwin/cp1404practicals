"""
CP1404 Practical 07 - Tests Guitar Class from guitars.py
Megan Godwin
"""

from cp1404practicals.prac7.guitars import Guitar

gibson_l5_CES = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2012, 5)

print(gibson_l5_CES.name," get_age() - Expected 95. Got ", gibson_l5_CES.get_age())
print(another_guitar.name," get_age() - Expected 5. Got ", another_guitar.get_age())

print(gibson_l5_CES.name, " is_vintage() - Expected True. Got ", gibson_l5_CES.is_vintage())
print(another_guitar.name, " is_vintage() - Expected False. Got ", another_guitar.is_vintage())
