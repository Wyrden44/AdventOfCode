with open("day_5/day_5_input.txt", "r") as f:
    lines = f.readlines()

d = {}
sequences = []
correct_sequences = []

# nr 1 

for line in lines:
    line = line.strip()
    if "|" in line:
        line = line.split("|")
        line = [int(line[0]), int(line[1])]

        if line[0] in list(d):
            d[line[0]].append(line[1])
        else:
            d[line[0]] = [line[1]]
    elif "," in line:
        sequences.append([int(e) for e in line.split(",")])

wrong_sequences = []
for sequence in sequences:
    wrong = False
    for i in range(len(sequence)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if sequence[j] in d[sequence[i]]:
                wrong = True
                break

    if wrong:
        wrong_sequences.append(sequence)
    else:
        correct_sequences.append(sequence)

total = 0
for sequence in correct_sequences:
    #print(sequence)
    #print(len(sequence))
    #print(int(len(sequence) / 2), sequence[int(len(sequence) / 2)])
    total += sequence[int(len(sequence) / 2)]
print(total)

total = 0
# nr 2
for sequence in wrong_sequences:
    # bubblesort
    for i in range(len(sequence)):
        if i == len(sequence) - i:
            break
        for j in range(len(sequence)-(i+1)):
            if sequence[j] in d[sequence[j+1]]:
                # swap
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
            elif sequence[j+1] in d[sequence[j]]:
                # do nothing
                continue

    total += sequence[int(len(sequence) / 2)]
            

print(total)