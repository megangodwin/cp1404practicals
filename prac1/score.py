
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
menu = input("'S' to calculate score, 'Q' to quit").lower()
while menu != "q":
    score = float(input("Enter score: "))
    if score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")
    menu = input("'S' to calculate score, 'Q' to quit").lower()