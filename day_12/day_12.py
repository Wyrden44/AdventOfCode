import time

start = time.time()


with open("day_12/day_12_input.txt", "r") as f:
    data = f.readlines()

    data = [x.strip() for x in data]

"""data = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]"""

"""data = [
    "EEEEE",
    "EXXXX",
    "EEEEE",
    "EXXXX",
    "EEEEE"
]
"""
"""data = [
    "OOOOO",
    "OXOXO",
    "OXXXO"
]"""

"""data = [
    ".....",
    ".AAA.",
    ".A.A.",
    ".AA..",
    ".A.A.",
    ".AAA.",
    "....."
]"""

"""data = [
    "AAAAAA",
    "AAABBA",
    "AAABBA",
    "ABBAAA",
    "ABBAAA",
    "AAAAAA"
]"""

graphs = []
results = []

for i in range(len(data)):
    for j in range(len(data[i])):
        in_area = False
        for area in graphs:
            if (i, j) in area:
                in_area = True
                break
        if in_area:
            continue
        if (i, j) not in graphs:
            # bfs graphs
            queue = {(i, j)}
            seen = set()

            perimiter = 0

            while len(queue) > 0:
                x, y = queue.pop()
                seen.add((x, y))

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < len(data) and 0 <= new_y < len(data[i]):
                        if data[new_x][new_y] == data[i][j]:
                            if (new_x, new_y) not in seen:
                                queue.add((new_x, new_y))
                        else:
                            perimiter += 1
                    else:
                        perimiter += 1

            graphs.append(seen)
            results.append(perimiter * len(seen))

print(sum(results))
print(f"Time: {time.time() - start}")

start = time.time()

# part 2
graphs = []
results = []

for i in range(len(data)):
    for j in range(len(data[i])):
        in_area = False
        for area in graphs:
            if (i, j) in area:
                in_area = True
                break
        if in_area:
            continue
        # bfs graphs
        if data[i][j] == ".":
            continue
        queue = {(i, j)}
        seen = set()
        corners = set()

        while len(queue) > 0:
            x, y = queue.pop()
            seen.add((x, y))

            neighbors = [[(-1, -1), (0, -1), (1, -1)], [(-1, 0), (0, 0), (1, 0)], [(-1, 1), (0, 1), (1, 1)]]

            neighboring_fields = [[data[x + dx][y + dy] if (0 <= x+dx < len(data) and 0 <= y+dy < len(data[0])) else "?" for dx, dy in row] for row in neighbors]
            # first quadrant
            if neighboring_fields[0][0] != data[x][y]:
                if neighboring_fields[1][0] == neighboring_fields[0][1] or neighboring_fields[1][0] != data[x][y] and neighboring_fields[0][1] != data[x][y]:
                    corners.add((x, y, 0))
            else:
                if neighboring_fields[1][0] != data[x][y] and neighboring_fields[0][1] != data[x][y]:
                    corners.add((x, y, 0))
            # second quadrant
            if neighboring_fields[0][2] != data[x][y]:
                if neighboring_fields[1][2] == neighboring_fields[0][1] or neighboring_fields[1][2] != data[x][y] and neighboring_fields[0][1] != data[x][y]:
                    corners.add((x, y, 1))
            else:
                if neighboring_fields[1][2] != data[x][y] and neighboring_fields[0][1] != data[x][y]:
                    corners.add((x, y, 1))
            # third quadrant
            if neighboring_fields[2][0] != data[x][y]:
                if neighboring_fields[1][0] == neighboring_fields[2][1] or neighboring_fields[1][0] != data[x][y] and neighboring_fields[2][1] != data[x][y]:
                    corners.add((x, y, 2))
            else:
                if neighboring_fields[1][0] != data[x][y] and neighboring_fields[2][1] != data[x][y]:
                    corners.add((x, y, 2))
            # fourth quadrant
            if neighboring_fields[2][2] != data[x][y]:
                if neighboring_fields[1][2] == neighboring_fields[2][1] or neighboring_fields[1][2] != data[x][y] and neighboring_fields[2][1] != data[x][y]:
                    corners.add((x, y, 3))
            else:
                if neighboring_fields[1][2] != data[x][y] and neighboring_fields[2][1] != data[x][y]:
                    corners.add((x, y, 3))
            
                    

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < len(data) and 0 <= new_y < len(data[i]):
                    if data[new_x][new_y] == data[i][j]:
                        if (new_x, new_y) not in seen:
                            queue.add((new_x, new_y))
                


        graphs.append(seen)
        results.append(len(seen) * len(corners))

print(sum(results))
print(time.time() - start)




        