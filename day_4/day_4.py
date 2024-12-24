with open("day_4/day_4_input.txt", "r") as f:
    lines = f.readlines()

def check_x_mas(line, pos1, pos2, pos3):
    return line[pos1] == "M" and line[pos2] == "A" and line[pos3] == "S"

def check_x_mas_vertical(lines, pos1, pos2, pos3):
    return lines[pos1[0]][pos1[1]] == "M" and lines[pos2[0]][pos2[1]] == "A" and lines[pos3[0]][pos3[1]] == "S"

total = 0
for j, line in enumerate(lines):
    for i in range(len(line)):
        if line[i] == "X":
            # horizontal
            if i <= len(line) - 4: 
                total += check_x_mas(line, i+1, i+2, i+3)
            if i >= 3:
                total += check_x_mas(line, i-1, i-2, i-3)
            
            # vertical
            if j <= len(lines) - 4:
                total += check_x_mas_vertical(lines, (j+1, i), (j+2, i), (j+3,i))
            if j >= 3:
                total += check_x_mas_vertical(lines, (j-1, i), (j-2, i), (j-3,i))

            # diagonal
            if j <= len(lines) - 4 and i < len(line) - 3:
                total += check_x_mas_vertical(lines, (j+1, i+1), (j+2, i+2), (j+3,i+3))
            if j <= len(lines) - 4 and i >= 3:
                total += check_x_mas_vertical(lines, (j+1, i-1), (j+2, i-2), (j+3,i-3))
            if j >= 3 and i < len(line) - 3:
                total += check_x_mas_vertical(lines, (j-1, i+1), (j-2, i+2), (j-3,i+3))
            if j >= 3 and i >= 3:
                total += check_x_mas_vertical(lines, (j-1, i-1), (j-2, i-2), (j-3,i-3))
            
print(total)


total = 0
# nr 2
for j in range(len(lines)):
    for i in range(len(lines[j])):
        if lines[j][i] == "A":
            if 1 <= j <= len(lines)-2 and 1 <= i <= len(lines[j]) - 2:
                if lines[j-1][i-1] == "M":
                    if lines[j+1][i+1] == "S":
                        if lines[j-1][i+1] == "M":
                            if lines[j+1][i-1] == "S":
                                total += 1
                        elif lines[j-1][i+1] == "S":
                            if lines[j+1][i-1] == "M":
                                total += 1
                
                elif lines[j-1][i-1] == "S":
                    if lines[j+1][i+1] == "M":
                        if lines[j-1][i+1] == "M":
                            if lines[j+1][i-1] == "S":
                                total += 1
                        elif lines[j-1][i+1] == "S":
                            if lines[j+1][i-1] == "M":
                                total += 1

print(total)


