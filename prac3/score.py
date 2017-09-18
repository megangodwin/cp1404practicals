
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():

    menu = input("'S' to calculate score, 'Q' to quit").lower()
    while menu != "q":
        score = float(input("Enter score: "))
        result = calculate_result(score)
        print(result)
        menu = input("'S' to calculate score, 'Q' to quit").lower()

def calculate_result(score):
    invalid = "Invalid score"
    excellent = "Excellent score"
    passable = "Passable score"
    bad = "Bad score"
    if score > 100:
        return(invalid)
    elif score >= 90:
        return(excellent)
    elif score >= 50:
        return(passable)
    elif score < 50:
        return(bad)
    return(result)

main()