names_to_ages = {"Jesse": 37, "Hana": 19, "Ana": 60}
d = {name: age for name, age in names_to_ages.items() if age > 50}
print(d)

print(dict(zip("abc", [1,2,3])))


