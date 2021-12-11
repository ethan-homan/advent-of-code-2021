import numpy as np

relative_coords = [
    (1, 1),
    (0, 1),
    (-1, 1),
    (1, -1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (-1, -1),
]


def get_data(file):
    data = []
    with open(file) as infile:
        for line in infile:
            line = [int(i) for i in list(line.strip())]
            data.append(line)
    return np.pad(data, 1, 'constant', constant_values=(-1))


if __name__ == "__main__":

    flashes = 0
    data = get_data("input.txt")
    for _ in range(100):
        data[data > -1] += 1
        flash_coords = np.argwhere(data > 9)
        while len(flash_coords) > 0:
            flashes += len(flash_coords)
            for x, y in flash_coords:
                data[x, y] = -2
                for x_diff, y_diff in relative_coords:
                    if data[x + x_diff, y + y_diff] >= 0:
                        data[x + x_diff, y + y_diff] += 1
            flash_coords = np.argwhere(data > 9)
        data[data == -2] = 0
    print(f"Part 1: {flashes} flashes.")

    data = get_data("input.txt")
    iters = 0
    while True:
        data[data > -1] += 1
        flash_coords = np.argwhere(data > 9)
        while len(flash_coords) > 0:
            for x, y in flash_coords:
                data[x, y] = -2
                for x_diff, y_diff in relative_coords:
                    if data[x + x_diff, y + y_diff] >= 0:
                        data[x + x_diff, y + y_diff] += 1
            flash_coords = np.argwhere(data > 9)
        data[data == -2] = 0
        iters += 1
        if data[data == 0].size == 100:
            break
    print(f"Part 2: {iters} iterations until all flash at once.")
