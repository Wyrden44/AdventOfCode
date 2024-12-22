data = []

with open("day_2/day_2_input.txt", "r") as f:
    content = f.read()
    
    lines = content.split("\n")
    for line in lines:
        l = line.split(" ")
        l = [int(e) for e in l]
        data.append(l)

def check_line_safe(line):
    increment = True
    increase = True
    # increase or decrease
    if line[0] < line[1]:
        increase = True
    elif line[0] > line[1]:
        increase = False
    else:
        return False

    for i in range(len(line)-1):
        incremental_step = line[i+1] - line[i]

        if not 1 <= abs(incremental_step) <= 3:
            increment = False
            break
        elif incremental_step <= 0 and increase:
            increment = False
            break
        elif incremental_step >= 0 and not increase:
            increment = False
            break

    return increment

num_of_safe = 0

for line in data:
    if check_line_safe(line):
        num_of_safe += 1

print(num_of_safe)

num_of_safe = 0

problematic_levels = []
problematic_levels_indexes = []

# nr 2
for line in data:
    increment = True
    increase = True
    # increase or decrease
    if line[0] < line[1]:
        increase = True
    elif line[0] > line[1]:
        increase = False
    else:
        problematic.append(0)
        problematic.append(1)
        if line[0] < line[2]:
            increase = True
        elif line[0] > line[2]:
            increase = False
        else:
            continue

    problematic = []
    for i in range(len(line)-1):
        incremental_step = line[i+1] - line[i]

        if not 1 <= abs(incremental_step) <= 3:
            increment = False
            if i not in problematic:
                problematic.append(i)
            problematic.append(i+1)
            break
        elif incremental_step <= 0 and increase:
            increment = False
            if i not in problematic:
                problematic.append(i)
            problematic.append(i+1)
            break
        elif incremental_step >= 0 and not increase:
            increment = False
            if i not in problematic:
                problematic.append(i)
            problematic.append(i+1)
            break

    if increment:
        num_of_safe += 1
    else:
        problematic_levels.append(line)
        problematic_levels_indexes.append(problematic)

#print(problematic_levels, problematic_levels_indexes)
for i in range(len(problematic_levels)):
    for j in problematic_levels_indexes[i]:
        if check_line_safe([problematic_levels[i][e] for e in range(len(problematic_levels[i])) if e != j]):
            num_of_safe += 1
            break


print(num_of_safe)