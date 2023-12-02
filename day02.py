#######################
# Advent of Code 2023 #
# DAY 2               #
#######################

###############
# PART 1 (&2) #
###############
file = open('Inputs/day02input.txt', 'r')
ID_sum, power_sum = 0, 0

for line in file:
    max_red, max_green, max_blue= 0, 0, 0
    game = line.split()
    for i in range(len(game)):
        if "red" in game[i] and int(game[i-1]) > max_red: max_red = int(game[i-1])
        if "green" in game[i] and int(game[i-1]) > max_green: max_green = int(game[i-1])
        if "blue" in game[i] and int(game[i-1]) > max_blue: max_blue = int(game[i-1])
    if (max_red <= 12 and max_green <= 13 and max_blue <= 14): ID_sum += int(game[1].split(":")[0])
    power_sum += max_red * max_green * max_blue
print("Sum of IDs: %d, Sum of powers: %d" % (ID_sum, power_sum))

##########
# PART 2 #
##########
file = open('Inputs/day02input.txt', 'r')
power_sum = 0;

for line in file:
    max_red, max_green, max_blue= 0, 0, 0
    games = line.split()
    for i in range(len(games)):
        if "red" in games[i] and int(games[i-1]) > max_red: max_red = int(games[i-1])
        if "green" in games[i] and int(games[i-1]) > max_green: max_green = int(games[i-1])
        if "blue" in games[i] and int(games[i-1]) > max_blue: max_blue = int(games[i-1])
    power_sum += max_red * max_green * max_blue
#print(power_sum)
