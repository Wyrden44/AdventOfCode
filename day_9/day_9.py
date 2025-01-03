with open("day_9/day_9_input.txt", "r") as f:
    content = f.read()

# test
#content = "12345"
#content = "2333133121414131402"

current_id = 0
extracted_str = []
free_spaces = 0

for i in range(len(content)):
    if i % 2 == 0:
        for i in range(int(content[i])):
            extracted_str.append(str(current_id))
        current_id += 1
        
    else:
        for i in range(int(content[i])):
            extracted_str.append(".")
        free_spaces += int(content[i])

print(extracted_str)

# nr 1
"""i = 0
swaps = 0
shifted = 1
while i < len(extracted_str):
    if extracted_str[i] == ".":
        if extracted_str[-1] == ".":
            extracted_str = extracted_str[:-1]
            continue
        extracted_str = extracted_str[:i] + [extracted_str[-1]] + extracted_str[i+1:-1]
        swaps += 1

    i += 1

print(extracted_str)"""

# nr 2
r = len(extracted_str) - 1
first_dot = 0
for i in range(len(extracted_str)):
    if extracted_str[i] == ".":
        first_dot = i
        break

current_id = None
while first_dot < r:
    while extracted_str[r] == str(current_id) or extracted_str[r] ==".":
        r -= 1
    current_id = int(extracted_str[r])
    # extract id block
    id_r = r
    id_l = r
    while extracted_str[id_l] == extracted_str[id_r]:
        id_l -= 1
    id_l += 1
    len_free_space = 0
    for i in range(first_dot, id_l):
        if extracted_str[i] == ".":
            len_free_space += 1
            if len_free_space > id_r - id_l:
                extracted_str = extracted_str[:i-len_free_space+1] + extracted_str[id_l:id_r+1] + extracted_str[i+1:id_l] + ["."] * (id_r - id_l + 1) + extracted_str[id_r+1:]
                len_free_spaces = 0
                break
        else:
            if len_free_space > 0:
                len_free_space = 0


print("".join(extracted_str))
solution = 0
for i in range(len(extracted_str)):
    if extracted_str[i] != ".":
        solution += int(extracted_str[i]) * i

print(solution)