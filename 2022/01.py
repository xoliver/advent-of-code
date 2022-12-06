# Part 1
calories = []

with open("1.txt", "r") as f:
    current = 0
    for line in f.readlines():
        line = line.strip()
        if not line:
            calories.append(current)
            current = 0
        else:
            count = int(line)
            current += count

sorted_calories = sorted(calories, reverse=True)

print("Part 1", sorted_calories[0])

print("Part 2", sum(sorted_calories[0:3]))
