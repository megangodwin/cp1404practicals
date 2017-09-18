number_list = []

for num in range(5):
    number = int(input("Enter number"))
    number_list.append(number)

print("First number is ", number_list[0])
print("Last number is ", number_list[4])
print("Smallest number is ", min(number_list))
print("Largest number is ", max(number_list))
print("Average number is ", sum(number_list)/5)