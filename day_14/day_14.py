import re
import time

with open("day_14/day_14_input.txt", "r") as f:
    data = f.readlines()

    data = [[int(y) for y in re.findall("-?[0-9]+", x.strip())] for x in data]

#data = [(2, 4, 2, -3)]

field_size_x = 101
field_size_y = 103

def get_score(data):
    quadrants = {k: 0 for k in range(4)}
    for robot in data:
        # first quadrant
        x, y, _, _ = robot
        if 0 <= x <= field_size_x // 2 - 1 and 0 <= y <= field_size_y // 2 - 1:
            quadrants[0] += 1
        elif field_size_x // 2 + 1 <= x <= field_size_x - 1 and 0 <= y <= field_size_y // 2 - 1:
            quadrants[1] += 1
        elif 0 <= x <= field_size_x // 2 - 1 and field_size_y // 2 + 1 <= y <= field_size_y - 1:
            quadrants[2] += 1
        elif field_size_x // 2 + 1 <= x <= field_size_x - 1 and field_size_y // 2 + 1 <= y <= field_size_y - 1:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


best_score = 0
best_data = data
for i in range(1000):
    for i in range(len(data)):
        x, y, velx, vely = data[i]
        x += velx
        y += vely

        if x >= field_size_x:
            x -= field_size_x
        elif x < 0:
            x += field_size_x
        if y >= field_size_y:
            y -= field_size_y
        elif y < 0:
            y += field_size_y

        score = get_score(data)
        if score > best_score:
            best_score = score
            best_data = data


print(best_score)
data = best_data
        

field = [["." for i in range(field_size_y)] for j in range(field_size_x)]

for robot in data:
    field[robot[0]][robot[1]] = "1" if field[robot[0]][robot[1]] == "." else "2"

for line in list(zip(*field)):
    print(" ".join(line))


quadrants = {k: 0 for k in range(4)}
for robot in data:
    # first quadrant
    x, y, _, _ = robot
    if 0 <= x <= field_size_x // 2 - 1 and 0 <= y <= field_size_y // 2 - 1:
        quadrants[0] += 1
    elif field_size_x // 2 + 1 <= x <= field_size_x - 1 and 0 <= y <= field_size_y // 2 - 1:
        quadrants[1] += 1
    elif 0 <= x <= field_size_x // 2 - 1 and field_size_y // 2 + 1 <= y <= field_size_y - 1:
        quadrants[2] += 1
    elif field_size_x // 2 + 1 <= x <= field_size_x - 1 and field_size_y // 2 + 1 <= y <= field_size_y - 1:
        quadrants[3] += 1


print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])#
print(quadrants)


