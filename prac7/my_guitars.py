"""
CP1404 Practical 07 - Guitar Class Usage
Megan Godwin
"""

from cp1404practicals.prac7.guitars import Guitar

#guitar_1 = Guitar("Fender Stratocaster", 2014, 765.40)
#guitar_2 = Guitar("Gibson L-5 CES", 1922, 16035.40)
#guitar_3 = Guitar("Line 6 JTV-59", 2010, 1512.90)

guitar_list = []

guitar_data = []
    #gets guitar name and checks for valid string and adds to list
    name = input("Name: ")
    while name == "":
        print("Input can not be empty")
        name = input("Name: ")
    guitar_data.append(name)

    #gets guitar manufactored year and checks for valid integer and adds to list


    #gets guitar cost and checks for valid integer and adds to list
    valid_input = False
    while not valid_input:
        try:
            year = int(input("Year: "))
            while year < 0:
                print("Year must be above 0")
                year = int(input("Year: "))
            valid_input = True
            guitar_data.append(year)
        except ValueError:
            print("Must input a number")
            valid_input = False

    #collects data of single guitar in a list
    guitar_list.append(guitar_data)
    print(guitar_list[0], " added")
