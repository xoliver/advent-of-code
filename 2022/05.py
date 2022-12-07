order_time = False
stacks = []

with open("05.txt", "r") as f:
    for line in f.readlines():
        if not line.strip():
            order_time = True
            continue

        if not order_time:
            # Read stack
            if line.strip()[0] == "1":
                continue

            if not stacks:
                stacks = [
                        []
                        for _ in range((len(line) + 1) // 4)
                 ]

            for idx, i in enumerate(range(0, len(line), 4)):
                item = line[i:i+4].strip()
                if not item:
                    continue
                stacks[idx].insert(0, item)

        else:
            # read commands
            _, quantity, _, source, _, destination = line.strip().split(" ")
            for _ in range(int(quantity)):
                stacks[int(destination)-1].append(stacks[int(source)-1].pop())

top_items = "".join(stack[-1][1:-1] for stack in stacks)
print("Part 1", top_items)


stacks = []
order_time = False

with open("05.txt", "r") as f:
    for line in f.readlines():
        if not line.strip():
            order_time = True
            continue

        if not order_time:
            # Read stack
            if line.strip()[0] == "1":
                continue

            if not stacks:
                stacks = [
                        []
                        for _ in range((len(line) + 1) // 4)
                 ]

            for idx, i in enumerate(range(0, len(line), 4)):
                item = line[i:i+4].strip()
                if not item:
                    continue
                stacks[idx].insert(0, item)

        else:
            # read commands
            _, quantity, _, source, _, destination = line.strip().split(" ")
            source = int(source) - 1
            destination = int(destination) - 1
            quantity = int(quantity)

            move = stacks[source][-quantity:]
            stacks[destination].extend(move)

            for _ in range(quantity):
                stacks[source].pop()

top_items = "".join(stack[-1][1:-1] for stack in stacks)
print("Part 2", top_items)
