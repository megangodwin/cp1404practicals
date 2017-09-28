"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from cp1404practicals.prac7.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    limo = Car(100)

    limo.add_fuel(20)

    print("Limo's fuel is {}".format(limo.fuel))

    limo.drive(115)

    print("Limo's odometer reads {}".format(limo.odometer))


    #my_car.drive(30)
    #print("fuel =", my_car.fuel)
    #print("odo =", my_car.odometer)
    #print(my_car)

    #print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    #print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()