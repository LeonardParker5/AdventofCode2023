#######################
# Advent of Code 2023 #
# DAY 2               #
#######################

##########
# PART 1 #
##########
MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
file = open('Inputs/day02input.txt', 'r')
ID_sum = 0

for line in file:
    reds, greens, blues, valid = 0, 0, 0, True
    games = line.split()
    for i in range(len(games)):
        if "red" in games[i]: reds += int(games[i-1])
        if "green" in games[i]: greens += int(games[i-1])
        if "blue" in games[i]: blues += int(games[i-1])
        if ";" in games[i] or i == (len(games)-1):
            if  (reds <= MAX_RED and greens <= MAX_GREEN and blues <= MAX_BLUE): reds, greens, blues = 0, 0, 0
            if (reds > MAX_RED or greens > MAX_GREEN or blues > MAX_BLUE): valid = False
    if valid: ID_sum += int(games[1].split(":")[0])

print(ID_sum)

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
        if "green" in games[i]and int(games[i-1]) > max_green: max_green = int(games[i-1])
        if "blue" in games[i]and int(games[i-1]) > max_blue: max_blue = int(games[i-1])
    power_sum += max_red * max_green * max_blue
print(power_sum)