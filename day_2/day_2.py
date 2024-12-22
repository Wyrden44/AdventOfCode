data = []

with open("day_2/day_2_input.txt", "r") as f:
    content = f.read()
    
    lines = content.split("\n")
    for line in lines:
        l = line.split(" ")
        l = [int(e) for e in l]
        data.append(l)

num_of_safe = 0

for line in data:
    increment = True
    increase = True
    # increase or decrease
    if line[0] < line[1]:
        increase = True
    elif line[0] > line[1]:
        increase = False
    else:
        continue

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

    if increment:
        num_of_safe += 1

print(num_of_safe)