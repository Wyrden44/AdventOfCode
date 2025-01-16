import re
import time

with open("day_14/day_14_input.txt", "r") as f:
    data = f.readlines()

    data = [re.findall("[0-9]+", x.strip()) for x in data]

field = [["." for _ in range(101)] for _ in range(103)]

robots = {(k[1], k[0]): (k[3], k[2]) for k in data}

for robot in robots:
    for bot in robots[robot]:
        x, y = robot
        x += bot[0]
        y += bot[1]

        if x >= 101:
            x -= 101
        elif x < 0:
            x += 101
        if y >= 103:
            y -= 103
        elif y < 0:
            y += 103

        robots[(y, x)] = (robots[robot][0], robots[robot][1])
        del robots[robot]
