def priority(thing):
    if thing.isupper():
        return ord(thing) - 65 + 27
    else:
        return ord(thing) - 97 + 1

total_priorities = 0

with open("03.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        first, second = line[:len(line)//2], line[len(line)//2:]
        common_items = set(first).intersection(set(second))
        total_priorities += sum(priority(item) for item in common_items)

print("Part 1", total_priorities)


grouped_priorities = 0

with open("03.txt", "r") as f:
    for first, second, third in zip(*[iter(f.readlines())]*3):
        common_items = set(first.strip()).intersection(set(second.strip())).intersection(set(third.strip()))
        grouped_priorities += sum(priority(item) for item in common_items)

print("Part 1", grouped_priorities)
