with open("day_8/day_8_input.txt", "r") as f:
    content = f.readlines()

    content = [line.strip() for line in content]

antenna_positions = {}
antenna_locations = {}

antenna_locations = set()

# get antenna positions
for i, line in enumerate(content):
    for j, char in enumerate(line):
        if char != ".":
            if char in list(antenna_positions):
                antenna_positions[char].append((i, j))
            else:
                antenna_positions[char] = [(i, j)]
        
for antenna in list(antenna_positions):
    if len(antenna_positions[antenna]) > 1:
        for a in antenna_positions[antenna]:
            antenna_locations.add(a)
    while len(antenna_positions[antenna]) > 1:
        x, y = antenna_positions[antenna][0]

        # distance to other pos
        for x2, y2 in antenna_positions[antenna][1:]:
            x_dis = x2 - x
            y_dis = y2 - y

            i = 1
            r1 = False
            r2 = False
            while not r1 or not r2:
                new_x = x - i * x_dis
                new_y = y - i * y_dis

                new_x2 = x + i * x_dis
                new_y2 = y + i * y_dis

                if 0 <= new_x < len(content) and 0 <= new_y < len(content[0]):
                    antenna_locations.add((new_x, new_y))
                else:
                    r1 = True
                if 0 <= new_x2 < len(content) and 0 <= new_y2 < len(content[0]):
                    antenna_locations.add((new_x2, new_y2))
                else:
                    r2 = True

                i += 1

        antenna_positions[antenna] = antenna_positions[antenna][1:]

print(len(antenna_locations))