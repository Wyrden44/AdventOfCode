data = []

with open("day_7/day_7_input.txt", "r") as f:
    content = f.readlines()

    for line in content:
        solution, nums = line.strip().split(":")
        nums = [int(n) for n in nums.split(" ")[1:]]

        data.append([int(solution)] + nums)


solution = []

def sum_mul(a, b, line, i, target, operators=""):
    if i >= len(line) - 1:
        if a + b == target:
            solution = operators + "+"
            return True, solution
        if a * b == target:
            solution = operators + "*"
            return True, solution
        if int(str(a)+str(b)) == target:
            solution = operators + "||"
            return True, solution
        return False, None

    found, solution = sum_mul(a + b, line[i+1], line, i+1, target, operators+"+")
    
    if found:
        return found, solution
    
    found, solution = sum_mul(int(str(a)+str(b)), line[i+1], line, i+1, target, operators+"||")

    if found:
        return found, solution

    return sum_mul(a * b, line[i+1], line, i+1, target, operators+"*")

total = 0
for line in data:
    found, _ = sum_mul(line[1], line[2], line, 2, line[0])

    if found:
        total += line[0]

print(total)




