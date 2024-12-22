row_1 = []
row_2 = []

with open("day_1/day_1_1_input.txt", "r") as f:
    content = f.read()
    
    lines = content.split("\n")
    for line in lines:
        l = line.split("   ")
        row_1.append(int(l[0]))
        row_2.append(int(l[1]))


# task 1

"""row_1.sort()
row_2.sort()


total_difference = 0
for i in range(len(row_1)):
    total_difference += abs(row_1[i] - row_2[i])

print(total_difference)"""


# task 2
similarity_score = 0
for e in row_1:
    increment_by = 0
    for b in row_2:
        if b == e:
            increment_by += e

    similarity_score += increment_by

print(similarity_score)

