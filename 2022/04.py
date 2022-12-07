fully_overlap = 0
partially_overlap = 0

with open("04.txt", "r") as f:
    for line in f.readlines():
        ass1, ass2 = line.strip().split(",")
        ass1start, ass1end = map(int, ass1.split("-"))
        ass2start, ass2end = map(int, ass2.split("-"))

        ass1nums = set(range(ass1start, ass1end + 1))
        ass2nums = set(range(ass2start, ass2end + 1))

        if ass1nums.issuperset(ass2nums) or ass2nums.issuperset(ass1nums):
           fully_overlap += 1

        if ass1nums.intersection(ass2nums):
            partially_overlap += 1

print("Part 1", fully_overlap)
print("Part 2", partially_overlap)
