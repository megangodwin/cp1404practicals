
name_file = open('names.txt', 'w')

username = input("Enter your name:")
print(username, file = name_file)

name_file.close()

name_file = open('names.txt', 'r')

give_name = name_file.readline()
print("Your name is {}".format(give_name))

name_file.close()

total = 0
in_file = open('numbers.txt', 'r')
for line in in_file.readlines():
    total += int(line.strip())
print(total)

in_file.close()
