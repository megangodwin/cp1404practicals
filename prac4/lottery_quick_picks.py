import random

def main():
    valid_number = False
    while not valid_number:
        try:
            num_picks = int(input("How many quick picks: "))
            valid_number = True
        except ValueError:
            print("Enter valid number")

    for num in range(num_picks):
        picks = [random.randint(1, 45) for num in range(6)]
        print("{:>2d} {:>2d} {:>2d} {:>2d} {:>2d} {:>2d}".format(picks[0], picks[1], picks[2], picks[3], picks[4], picks[5]))
main()
