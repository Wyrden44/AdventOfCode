import time
start_time = time.time()

with open("day_11/day_11_input.txt", "r") as f:
    data = f.read().strip()

stones = [int(stone) for stone in data.split(" ")]

# stones = [125, 17]

"""# brute force
for i in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        if stone == 0:
            stone = 1
            stones[i] = stone
        # even
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            stone = [stone[:(len(stone) // 2)], stone[(len(stone) // 2):]]
            stones[i] = int(stone[0])
            if i + 1 < len(stones):
                stones.insert(i+1, int(stone[1]))
            else:
                stones.append(int(stone[1]))
            i += 1
        else:
            stone *= 2024
            stones[i] = stone

        i += 1

print("--- %s seconds ---" % (time.time() - start_time))"""

start_time = time.time()

stones = [int(stone) for stone in data.split(" ")]
# with dict
numbers = {int(stone): 1 for stone in stones}

for i in range(75):
    new_numbers = {0: 0, 1: 0}
    for stone in list(numbers):
            if stone == 0:
                stone = 1
                new_numbers[stone] += numbers[0]
                # even
            elif len(str(stone)) % 2 == 0:
                old_stone = stone
                stone = str(stone)
                stone = [stone[:(len(stone) // 2)], stone[(len(stone) // 2):]]
                if int(stone[0]) in new_numbers:
                    new_numbers[int(stone[0])] += numbers[old_stone]
                else:
                    new_numbers[int(stone[0])] = numbers[old_stone]
                if int(stone[1]) in new_numbers: 
                    new_numbers[int(stone[1])] += numbers[old_stone]
                else:
                    new_numbers[int(stone[1])] = numbers[old_stone]
            else:
                old_stone = stone
                stone *= 2024
                if stone in new_numbers:
                    new_numbers[stone] += numbers[old_stone]
                else:
                    new_numbers[stone] = numbers[old_stone]
    
    numbers = new_numbers

print("--- %s seconds ---" % (time.time() - start_time))
print(sum(new_numbers.values()))