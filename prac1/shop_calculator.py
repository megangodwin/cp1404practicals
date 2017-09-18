
price_list = []
number_of_items = int(input("How many items"))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("How many items"))
for i in range(number_of_items):
    price_list.append(float(input("enter item price")))
total = sum(price_list)
if total < 100:
    print("Total price for", number_of_items, "items is ${:.2f}".format(total))
else:
    discount = total * 0.1
    discounted_price = total - discount
    print("Total price for", number_of_items, "items is ${:.2f}".format(discounted_price))
