import numpy as np
from collections import Counter

relative_coords = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def get_data(file):
    data = []
    with open(file) as infile:
        for line in infile:
            line = [int(i) for i in list(line.strip())]
            data.append(line)
    return np.pad(data, 1, 'constant', constant_values=9)


if __name__ == "__main__":

    data = get_data("input.txt")

    # Iterate through all points and check adjacent points to see if it is a low point.
    low_points = []
    for x in range(1, data.shape[0] - 1):
        for y in range(1, data.shape[1] - 1):
            is_low_point = True
            for xdiff, ydiff in relative_coords:
                if data[x, y] >= data[x + xdiff, y + ydiff]:
                    is_low_point = False
                    break
            if is_low_point:
                low_points.append((x, y))

    low_point_score = sum((data[x, y] + 1 for x, y in low_points))
    print(f"Part 1: {low_point_score}")

    # Iterate through all points and increment the low points associated with the "basin"
    # that the points are part of.
    low_point_counts = Counter()
    for x_start in range(1, data.shape[0] - 1):
        for y_start in range(1, data.shape[1] - 1):
            x, y = x_start, y_start
            while True:
                # When we arrive at a low point, increment the low point since we started at point in its basin
                if (x, y) in low_points:
                    low_point_counts[(x, y)] += 1
                    break
                # 9's are not part of basins
                elif data[x, y] == 9:
                    break
                # Crawl the lowest adjacent point, we will eventually arrive at a low point if we do this.
                else:
                    lowest_direction_idx = 0
                    lowest_direction_val = data[x + relative_coords[0][0], y + relative_coords[0][1]]
                    for i, (xdiff, ydiff) in enumerate(relative_coords):
                        if data[x + xdiff, y + ydiff] < lowest_direction_val:
                            lowest_direction_idx = i
                            lowest_direction_val = data[
                                x + relative_coords[lowest_direction_idx][0],
                                y + relative_coords[lowest_direction_idx][1],
                            ]
                    x += relative_coords[lowest_direction_idx][0]
                    y += relative_coords[lowest_direction_idx][1]
    # Compute final score
    largest_three_basin_sizes = [val for _, val in low_point_counts.most_common(3)]
    answer = 1
    for i in largest_three_basin_sizes:
        answer *= i
    print(f"Part 2: {answer}")
