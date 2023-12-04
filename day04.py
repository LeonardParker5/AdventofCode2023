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