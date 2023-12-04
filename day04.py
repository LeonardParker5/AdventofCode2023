#######################
# Advent of Code 2023 #
# DAY 4               #
#######################

##########
# PART 1 #
##########
file = open('Inputs/day04input.txt', 'r')
point_sum = 0
for line in file:
    wins = len((set(line.split(":")[1].split("|")[0].split()) & set(line.split(":")[1].split("|")[1].split())))
    points = 0 if wins == 0 else 1
    for i in range(wins - 1): points *= 2
    point_sum += points
print(point_sum)

##########
# PART 2 #
##########
file = open('Inputs/day04input.txt', 'r')
cards = [1] * 219
index = 0
for line in file:
    wins = len((set(line.split(":")[1].split("|")[0].split()) & set(line.split(":")[1].split("|")[1].split())))
    for i in range(cards[index]):
        if wins == 0: break
        for j in range(1, wins+1): cards[index+j] += 1
    index += 1
print(sum(cards))