import numpy as np

if __name__ == "__main__":
    data = np.array([int(i) for i in open("input.txt").read().split(",")])
    costs = []

    smallest, largest = data.min(), data.max()

    for i in range(smallest, largest):
        costs.append(np.abs(data - i).sum())

    print(f"Part 1: fuel costs are {min(costs)}")

    counts = np.zeros(largest + 1, dtype=int)
    for i in range(1, len(counts)):
        counts[i] = (i + counts[i - 1])

    costs = []
    for i in range(smallest, largest):
        cost = 0
        for j in np.abs(data - i):
            cost += counts[j]
        costs.append(cost)

    print(f"Part 2: fuel costs are {min(costs)}")
