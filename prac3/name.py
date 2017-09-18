def get_name():
    name = input("Enter name: ")
    while not name:
        print("Name must not be empty")
        name = input("Enter name: ")
    return name

def main():
    name = get_name()
    print(name[::2])

main()
