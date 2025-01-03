# measure program execution time
import time
start_time = time.time()

with open("day_10/day_10_input.txt", "r") as f:
    data = f.readlines()

    data = [line.strip() for line in data]

# data = ["89010123",
#         "78121874",
#         "87430965",
#         "96549874",
#         "45678903",
#         "32019012",
#         "01329801",
#         "10456732"
# ]

# data = [
#     "...0...",
#     "...1...",
#     "...2...",
#     "6543456",
#     "7.....7",
#     "8.....8",
#     "9.....9"
# ]

for i in range(len(data)):
    line = data[i].replace(".", "20")
    data[i] = line

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# bfs
data_points = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "0":
            data_points.append((i, j))

total_trailheads = 0
for x, y in data_points:
    trailheads = set()
    queue = [(x, y)]
    visited = set()
    while queue:
        x, y = queue.pop(0)
        for direction in directions:
            if 0 <= x+direction[0] < len(data) and 0 <= y+direction[1] < len(data[0]):
                if int(data[x+direction[0]][y+direction[1]]) == int(data[x][y]) + 1:
                    if int(data[x][y]) == 8:
                        trailheads.add((x+direction[0], y+direction[1]))
                    elif (x+direction[0], y+direction[1]) not in visited:
                        queue.append((x+direction[0], y+direction[1]))
                        visited.add((x+direction[0], y+direction[1]))

    total_trailheads += len(trailheads)

print("--- %s seconds ---" % (time.time() - start_time))

print(total_trailheads)

# nr 2
total_trailheads = 0
for x, y in data_points:
    trailheads = []
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for direction in directions:
            if 0 <= x+direction[0] < len(data) and 0 <= y+direction[1] < len(data[0]):
                if int(data[x+direction[0]][y+direction[1]]) == int(data[x][y]) + 1:
                    if int(data[x][y]) == 8:
                        trailheads.append((x+direction[0], y+direction[1]))
                    else:    
                        queue.append((x+direction[0], y+direction[1]))

    total_trailheads += len(trailheads)

print("--- %s seconds ---" % (time.time() - start_time))
print(total_trailheads)