import sys


class Coords:
    def __init__(self, val,  x, y):
        self.val = val
        self.x = x
        self.y = y
        return

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Val:{self.val} x:{self.x} y:{self.y}"


class Part:
    def __init__(self, partval):
        self.partval = partval
        self.coords_list = []
        return

    def insert(self, coords):
        self.coords_list.append(coords)
        return

    def length(self):
        return len(self.partval)

    def value(self):
        return int(self.partval)

    def __repr__(self):
        return f"Part: {self.partval} list: {self.coords_list}"


partsCollection = []
symbolCollection = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.rstrip("\r\n")
        parts = [part for part in line.split(".") if part.isdigit()]
        print(parts)

        # part check
        for partstring in parts:
            part_obj = Part(partstring)
            location = line.find(partstring)

            # append every part coordinates inside part
            for idx, part in enumerate(partstring):
                part_obj.insert(Coords(part, idx + location, y))
            partsCollection.append(part_obj)

        # symbol check_call
        for x, char in enumerate(line):
            if char != ".":
                if not char.isdigit():
                    # print(f"char: {char} x:{x} y:{y}")
                    symbolCollection.append(Coords(char, x, y))

for symbol in symbolCollection:
    print(symbol)


print("************************\n")
for part in partsCollection:
    print(part)
