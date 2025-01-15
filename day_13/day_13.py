import re
import time

start = time.time()

with open("day_13/day_13_input.txt", "r") as f:
    content = f.readlines()

    content = [x.strip() for x in content if x != "\n"]

"""content = [
    "Button A: X+94, Y+34",
    "Button B: X+22, Y+67",
    "Prize: X=8400, Y=5400",
    "Button A: X+17, Y+86",
    "Button B: X+84, Y+37",
    "Prize: X=7870, Y=6450",
    "Button A: X+69, Y+23",
    "Button B: X+27, Y+71",
    "Prize: X=18641, Y=10279"
]"""


def find_path(a_steps, b_steps, prize):
    a_steps = [int(x) for x in a_steps]
    b_steps = [int(x) for x in b_steps]
    prize = [int(x) for x in prize]

    open_nodes = {(0, 0): 0}
    closed_nodes = {}

    while len(open_nodes) > 0:
        current_f = 999
        current = None
        for node in list(open_nodes):
            if open_nodes[node] < current_f:
                current_f = open_nodes[node]
                current = node
        del open_nodes[current]
        closed_nodes[current] = current_f

        if current[0] * a_steps[0] + current[1] * b_steps[0] == prize[0] and current[0] * a_steps[1] + current[1] * b_steps[1] == prize[1]:
            return current

        if (current[0]+1, current[1]) not in closed_nodes and (current[0]+1, current[1]) not in open_nodes and current[0] < 100:
            open_nodes[(current[0]+1, current[1])] = closed_nodes[current] + 3
        if (current[0], current[1]+1) not in closed_nodes and (current[0], current[1]+1) not in open_nodes and current[1] < 100:
            open_nodes[(current[0], current[1]+1)] = closed_nodes[current] + 1

    return [0, 0]
    

"""# part 1
total = 0
for i in range(0, len(content), 3):
    a_steps = re.findall(r"[0-9]+", content[i])
    b_steps = re.findall(r"[0-9]+", content[i + 1])
    prize = re.findall(r"[0-9]+", content[i + 2])

    sol = find_path(a_steps, b_steps, prize)
    total += sol[0] * 3
    total += sol[1]

print(total)
print(time.time() - start)"""

start = time.time()

# part 2 (fuck those mathematics - never would have solved it on my own)
def solve(p_x, b_y, p_y, a_x, a_y, b_x):
    A = (p_x*b_y - p_y*b_x) / (a_x*b_y - a_y*b_x)
    B = (a_x*p_y - a_y*p_x) / (a_x*b_y - a_y*b_x)

    if A == int(A) and B == int(B):
        return int(A), int(B)
    return 0, 0

total = 0
for i in range(0, len(content), 3):
    a_steps = [int(x) for x in re.findall(r"[0-9]+", content[i])]
    b_steps = [int(x) for x in re.findall(r"[0-9]+", content[i + 1])]
    prize = [int(x) + 10000000000000 for x in re.findall(r"[0-9]+", content[i + 2])]

    sol = solve(prize[0], b_steps[1], prize[1], a_steps[0], a_steps[1], b_steps[0])
    total += sol[0] * 3
    total += sol[1]

print(total)
print(time.time() - start)