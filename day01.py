#######################
# Advent of Code 2023 #
# DAY 1               #
#######################

##########
# PART 1 #
##########
file = open('Inputs/day01input.txt', 'r')
calibration_sum = 0;

for line in file:
    calibration = ""
    for i in line:
        if i.isdigit():
            calibration += i
            break
    for i in reversed(line):
        if i.isdigit():
            calibration += i
            break
    calibration_sum += int(calibration)
print(calibration_sum)

##########
# PART 2 #
##########
file = open('Inputs/day01input.txt', 'r')
calibration_sum = 0;
numbers = {"one":"o1e","two":"t2o","three":"t3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}

for line in file:
    calibration = ""
    for key in numbers: line = line.replace(key, numbers.get(key))
    for i in line:
        if i.isdigit():
            calibration += i
            break
    for i in reversed(line):
        if i.isdigit():
            calibration += i
            break
    calibration_sum += int(calibration)
print(calibration_sum)