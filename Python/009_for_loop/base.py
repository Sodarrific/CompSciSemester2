direction = (input())
numbe = (input())
number = int(numbe)
horiz = ("h")
verti = ("v")
if direction == horiz:
    for x in range(0,number):
        print("-", end="")
if direction == verti:
    for x in range(0,number):
        print("|")