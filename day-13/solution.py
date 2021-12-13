import numpy as np


def read_data(file):
    data = []
    instructions = []
    with open(file) as infile:
        for line in infile:
            if "," in line:
                x, y = line.strip().split(",")
                data.append((int(x), int(y)))
            elif "fold along " in line:
                axis, coord = line.strip().replace("fold along ", "").split("=")
                instructions.append((axis, int(coord)))

    max_x = max((x for x, _ in data))
    max_y = max((y for _, y in data))

    grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for x, y in data:
        grid[x, y] = 1

    return grid, instructions


if __name__ == "__main__":
    grid, instructions = read_data("input.txt")

    # Fold the grid onto itself, making sure to print the solution to Part 1 on the first iteration
    for i, (axis, coord) in enumerate(instructions):
        if axis == 'y':
            base = grid[:, :coord]
            fold = np.flip(grid[:, coord + 1:], axis=1)
            grid = base + fold
        elif axis == 'x':
            base = grid[:coord, :]
            fold = np.flip(grid[coord + 1:, :], axis=0)
            grid = base + fold

        if i == 0:
            print(f"Part 1: {grid[grid >= 1].size}")

    # Part 2 has been "solved" above, this just prints the output in a human readable way
    x, y = grid.shape
    d = []
    for i in range(y):
        s = ["."] * x
        for j in range(x):
            if grid[j, i] > 0:
                s[j] = "#"
        d.append("".join(s))

    print("\nPart 2:")
    print("\n".join(d))
