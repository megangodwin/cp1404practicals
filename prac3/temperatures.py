
"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Fahrenheit to Celcius
    F - Convert Celcius to Fahrenheit
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "F":
            temp_to_convert = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(temp_to_convert)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "C":
            temp_to_convert = float(input("Fahrenheit: "))
            celsius = calculate_celcius(temp_to_convert)
            print("Result: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calculate_celcius(temp_to_convert):
    celsius = 5 / 9 * (temp_to_convert - 32)


def calculate_fahrenheit(temp_to_convert):
    fahrenheit = temp_to_convert * 9.0 / 5 + 32


main()