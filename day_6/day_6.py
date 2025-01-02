with open("day_6/day_6_input.txt") as f:
    content = f.readlines()

    content = [list(line.strip()) for line in content]

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
unique_squares = [(guard[0], guard[1], "up")]
reached_end = False
directions = ["up", "right", "down", "left"]

def turn(direction):
    if directions.index(direction)+1 < len(directions):
        return directions[directions.index(direction)+1]
    else:
        return directions[0]

# nr 1
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
                # elif content[i][guard[1]] != "X":
                content[i][guard[1]] = "X"
                unique_squares.append((i, guard[1], direction))
        case "down":
            for i in range(guard[0]+1, len(content)+1):
                if i == len(content):
                    reached_end = True
                    break
                if content[i][guard[1]] == "#":
                    guard = (i-1, guard[1])
                    direction = turn(direction)
                    break
                # elif content[i][guard[1]] != "X":
                content[i][guard[1]] = "X"
                unique_squares.append((i, guard[1], direction))
        case "right":
            for i in range(guard[1]+1, len(content[0])+1):
                if i == len(content[0]):
                    reached_end = True
                    break
                if content[guard[0]][i] == "#":
                    guard = (guard[0], i-1)
                    direction = turn(direction)
                    break
                # elif content[guard[0]][i] != "X":
                content[guard[0]][i] = "X"
                unique_squares.append((guard[0], i, direction))
        case "left":
            for i in range(guard[1]-1, -2, -1):
                if i == -1:
                    reached_end = True
                    break
                if content[guard[0]][i] == "#":
                    guard = (guard[0], i+1)
                    direction = turn(direction)
                    break
                # elif content[guard[0]][i] != "X":
                content[guard[0]][i] = "X"
                unique_squares.append((guard[0], i, direction))

# #print(unique_squares)
# import pygame

# pygame.init()

# TILE = 50
# screen = pygame.display.set_mode((TILE * len(content), TILE * len(content[0])))

# clock = pygame.time.Clock()

# current_square = 0
# reached_end = False
# loop = False
# direction = "up"

# content[unique_squares[current_square+1][0]][unique_squares[current_square+1][1]] = "#"
# guard = [unique_squares[current_square][0], unique_squares[current_square][1]]

# while True:
#     clock.tick(10)

#     # display
#     screen.fill((10, 10, 10))

#     for i, line in enumerate(content):
#         for j, tile in enumerate(line):
#             if tile == "." or tile == "X":
#                 pygame.draw.rect(screen, (100, 100, 100), (j*TILE, i*TILE, TILE, TILE))
#             if tile == "#":
#                 pygame.draw.rect(screen, (0, 255, 0), (j*TILE, i*TILE, TILE, TILE))
#             if i == guard[0] and j == guard[1]:
#                 pygame.draw.rect(screen, (255, 0, 0), (j*TILE, i*TILE, TILE, TILE))

#     pygame.display.update()

    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             loop = True

#     # logic
#     match direction:
#         case "up":
#             if guard[0] > 0:
#                 if content[guard[0]-1][guard[1]] != "#":
#                     guard[0] -= 1
#                 else:
#                     direction = turn(direction)
#             else:
#                 reached_end = True

#         case "down":
#             if guard[0] < len(content) - 1:
#                 if content[guard[0]+1][guard[1]] != "#":
#                     guard[0] += 1
#                 else:
#                     direction = turn(direction)
#             else:
#                 reached_end = True
#         case "right":
#             if guard[1] < len(content[0]) - 1:
#                 if content[guard[0]][guard[1]+1] != "#":
#                     guard[1] += 1
#                 else:
#                     direction = turn(direction)
#             else:
#                 reached_end = True
#         case "left":
#             if guard[1] > 0:
#                 if content[guard[0]][guard[1]-1] != "#":
#                     guard[1] -= 1
#                 else:
#                     direction = turn(direction)
#             else:
#                 reached_end = True

#     if reached_end or loop:
#         # reset
#         content[unique_squares[current_square+1][0]][unique_squares[current_square+1][1]] = "."
#         reached_end = False
#         loop = False
#         direction = unique_squares[current_square+1][2]
#         if current_square < len(unique_squares) - 1:
#             current_square += 1
#         else:
#             pygame.quit()
#             exit()
        
#         guard = [unique_squares[current_square][0], unique_squares[current_square][1]]
#         # new obstacle
#         content[unique_squares[current_square+1][0]][unique_squares[current_square+1][1]] = "#"
        

def run_simulation(guard, direction):
    reached_end = False
    loop = False

    visited = {}
    
    while not reached_end and not loop:
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
                    else:
                        if (i, guard[1]) in visited:
                            visited[(i, guard[1])] += 1
                        else:
                            visited[(i, guard[1])] = 1

                        if visited[(i, guard[1])] > 4:
                            loop = True
            case "down":
                for i in range(guard[0]+1, len(content)+1):
                    if i == len(content):
                        reached_end = True
                        break
                    if content[i][guard[1]] == "#":
                        guard = (i-1, guard[1])
                        direction = turn(direction)
                        break
                    else:
                        if (i, guard[1]) in visited:
                            visited[(i, guard[1])] += 1
                        else:
                            visited[(i, guard[1])] = 1

                        if visited[(i, guard[1])] > 4:
                            loop = True
            case "right":
                for i in range(guard[1]+1, len(content[0])+1):
                    if i == len(content[0]):
                        reached_end = True
                        break
                    if content[guard[0]][i] == "#":
                        guard = (guard[0], i-1)
                        direction = turn(direction)
                        break
                    else:
                        if (guard[0], i) in visited:
                            visited[(guard[0], i)] += 1
                        else:
                            visited[(guard[0], i)] = 1

                        if visited[(guard[0], i)] > 4:
                            loop = True
            case "left":
                for i in range(guard[1]-1, -2, -1):
                    if i == -1:
                        reached_end = True
                        break
                    if content[guard[0]][i] == "#":
                        guard = (guard[0], i+1)
                        direction = turn(direction)
                        break
                    else:
                        if (guard[0], i) in visited:
                            visited[(guard[0], i)] += 1
                        else:
                            visited[(guard[0], i)] = 1

                        if visited[(guard[0], i)] > 4:
                            loop = True
                
    return loop

obstacle_positions = []
working = 0
# nr 2
for i in range(len(unique_squares)-1):
    # set obstacle
    if (unique_squares[i+1][0], unique_squares[i+1][1]) not in obstacle_positions:
        content[unique_squares[i+1][0]][unique_squares[i+1][1]] = "#"

        # run simulation
        if run_simulation((unique_squares[i][0], unique_squares[i][1]), unique_squares[i][2]):
            working += 1

        obstacle_positions.append((unique_squares[i+1][0], unique_squares[i+1][1]))

        content[unique_squares[i+1][0]][unique_squares[i+1][1]] = "."


print(working)