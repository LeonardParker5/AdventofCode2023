#######################
# Advent of Code 2023 #
# DAY 6               #
#######################

##########
# PART 1 #
##########
file = open('Inputs/day06input.txt', 'r')
time, distance = file.readline().split(":")[1].split(), file.readline().split(":")[1].split()
product_of_wins = 1

for i in range(len(time)):
    wins = 0
    for j in range((int(time[i])+1)):
        distance_traveled = (int(time[i]) - j) * j
        if distance_traveled > int(distance[i]): wins += 1
    product_of_wins *= wins
print(product_of_wins)

##########
# PART 2 #
##########
file = open('Inputs/day06input.txt', 'r')
time, distance = "".join(file.readline().split(":")[1].split()), "".join(file.readline().split(":")[1].split())
wins = 0

for j in range(int(time)+1):
    distance_traveled = (int(time) - j) * j
    if distance_traveled > int(distance): wins += 1
print(wins)