open_close_mapping = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

part_1_cost_mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

part_2_cost_mapping = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

if __name__ == "__main__":

    data = []
    with open("input.txt") as infile:
        for line in infile:
            data.append(line.strip())

    # Part 1
    cost = 0
    incorrect_lines = []
    for i, line in enumerate(data):
        stack = []
        for c in line:
            if c in open_close_mapping.keys():
                stack.append(open_close_mapping[c])
            else:
                expected = stack.pop()
                if expected != c:
                    incorrect_lines.append(i)
                    cost += part_1_cost_mapping[c]
                    break
    print(cost)
    # Part 2
    # Start by getting the lines that didn't have incorrect characters
    data = [line for (i, line) in enumerate(data) if i not in incorrect_lines]

    costs = []
    for line in data:
        stack = []
        cost = 0
        for c in line:
            if c in open_close_mapping.keys():
                stack.append(open_close_mapping[c])
            else:
                stack.pop()
        for remaining_char in reversed(stack):
            cost *= 5
            cost += part_2_cost_mapping[remaining_char]
        costs.append(cost)
    costs = sorted(costs)
    print(costs[len(costs)//2])
