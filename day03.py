#######################
# Advent of Code 2023 #
# DAY 3               #
#######################

def print_box(box):
    for row in box:
        print(*row, sep=" ")

##########
# PART 1 #
##########
file = open('Inputs/day03input.txt', 'r')
box = []

for line in file:
    temp = []
    for i in line:
        if i != "\n": temp.append(i)
    box.append(temp)

box.insert(0,["." for _ in range(len(box[0]))])
box.insert(len(box),["." for _ in range(len(box[0]))])
for i in box:
    i.insert(0, ".")
    i.insert(len(i), ".")

print_box(box)

for y in range(len(box)):
    for x in range(len(box[0])):
        if box[y][x] != "." and not box[y][x].isdigit():
            #check surrounding neighbors for digit
            print("")

##########
# PART 2 #
##########
file = open('Inputs/day03input.txt', 'r')