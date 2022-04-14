from random import randint

filename = "large.in"

fileHandler = open(filename, "w")

fileHandler.write("198\n")
fileHandler.write("100\n")
fileHandler.write("3\n")
fileHandler.write("14\n")

cities = []
while len(cities) < 198:
    x = randint(0, 99)
    y = randint(0, 99)
    if not (x,y) in cities:
        cities.append( (x, y) )
        fileHandler.write(f"{x} {y}\n")



fileHandler.close()
