import re

with open("day_3/day_3_input.txt", "r") as f:
    content = f.read()

split_r = re.split(r"do\(\)|don't\(\)", content)
r = re.findall(r"mul\(\d+,\d+\)", content)
r_specific = re.findall(r".*?(do\(\)|don't\(\))", content)

print(len(split_r), len(r_specific))
# nr 2
total = 0
for i in range(len(split_r)):
    if i > 0:
        if r_specific[i-1] == "don't()":
            continue
    r = re.findall(r"mul\(\d+,\d+\)", split_r[i])
    for e in r:
        e = e.replace("mul(", "").replace(")", "").split(",")

        total += int(e[0]) * int(e[1])
    

print(total)

    

exit()

# nr 1
total = 0
for e in r:
    e = e.replace("mul(", "").replace(")", "").split(",")

    total += int(e[0]) * int(e[1])


print(total)