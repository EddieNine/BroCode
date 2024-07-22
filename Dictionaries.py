# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("USA"))
# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("that capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
# print(values)
# for key in capitals.keys():
#    print(key)

items = capitals.items()
for key, value in capitals.items():
    print(f'{key}: {value}')