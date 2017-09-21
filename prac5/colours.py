"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_NAMES = {"DARK ORCHID": "#9932cc", "LEMON CHIFFON": "#fffacd", "OLIVE DRAB": "#6b8e23", "PAPAYA WHIP": "#ffefd5",
                "PEACH PUFF": "#ffdab9", "WHITE SMOKE": "#f5f5f5", "SEASHELL": "#fff5ee", "SIENNA": "#a0522d",
                "MINT CREAM": "#f5fffa", "MISTY ROSE": "#ffe4e1"}

names_tuple = COLOUR_NAMES.items()

for item in names_tuple:
    print("{:<5s} is {}".format(item[0], item[1]))

colour = input("Enter colour name: ").upper()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").upper()
