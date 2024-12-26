with open("day_6/day_6_input.txt") as f:
    content = f.readlines()

    content = [list(line) for line in content]

guard = None
direction = "up"
# guard pos
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == "^":
            guard = (i, j)
            content[i][j] = "X"
            break
    if guard is not None:
        break

# move the guard
unique_squares = [guard]
reached_end = False
directions = ["up", "right", "down", "left"]

def turn(direction):
    if directions.index(direction)+1 < len(directions):
        return directions[directions.index(direction)+1]
    else:
        return directions[0]

while not reached_end:
    match direction:
        case "up":
            for i in range(guard[0]-1, -2, -1):
                if i == -1:
                    reached_end = True
                    break
                if content[i][guard[1]] == "#":
                    guard = (i+1, guard[1])
                    direction = turn(direction)
                    break
                elif content[i][guard[1]] != "X":
                    content[i][guard[1]] = "X"
                    unique_squares.append((i, guard[1]))
        case "down":
            for i in range(guard[0]+1, len(content)+1):
                if i == len(content):
                    reached_end = True
                    break
                if content[i][guard[1]] == "#":
                    guard = (i-1, guard[1])
                    direction = turn(direction)
                    break
                elif content[i][guard[1]] != "X":
                    content[i][guard[1]] = "X"
                    unique_squares.append((i, guard[1]))
        case "right":
            for i in range(guard[1]+1, len(content[0])+1):
                if i == len(content[0]):
                    reached_end = True
                    break
                if content[guard[0]][i] == "#":
                    guard = (guard[0], i-1)
                    direction = turn(direction)
                    break
                elif content[guard[0]][i] != "X":
                    content[guard[0]][i] = "X"
                    unique_squares.append((guard[0], i))
        case "left":
            for i in range(guard[1]-1, -2, -1):
                if i == -1:
                    reached_end = True
                    break
                if content[guard[0]][i] == "#":
                    guard = (guard[0], i+1)
                    direction = turn(direction)
                    break
                elif content[guard[0]][i] != "X":
                    content[guard[0]][i] = "X"
                    unique_squares.append((guard[0], i))

print(unique_squares)

# nr 2
for pos in unique_squares:
    content[pos[0]][pos[1]] = "#"
        