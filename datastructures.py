#Tuples
cars = ("Mercedes", "R34", "Pagani", "Supra", "GTR")
print(cars)
print(cars[2])
print(cars[1:4])
print(cars[1:])
for gari in cars:
    print(gari)

#Lists
colours = ["Red", "Green", "Purple", "Blue", "Gray", "Black"]
print(colours)
print(colours[2])
colours[0] = "Light red"
print(colours[1:4])
print(colours[1:])
for rangi in colours:
    print(rangi)

print(colours)
colours.pop(2)
print(colours)
colours.sort(reverse=True)
print(colours)
colours.sort()
print(colours)
colours.reverse()
print(colours)

#Dictionaries
students = {"ADM1": "Tracy", "ADM2": "Moses", "ADM3": "Eugene"}
print(students["ADM1"])
for funguo in students.keys():
    print(funguo)

for jina in students.values():
    print(jina)

#Sets
ranks = {1, 5, 8, 4, 0, 5, 3, 2, 1, 6, 8, 10, 11, 12, 10}
print(ranks)

names = ["James", "Abigael", "Jane", "Sandra", "Jefferson", "Bree"]
generateslist = []
for n in names:
    if len(n) > 5:
        generateslist.append(n)

for x in generateslist:
    print(x)