import numpy as np
from typing import List, Tuple


def read_input(filename: str) -> List[List[Tuple[int, int]]]:
    data = []
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            point_1, point_2 = line.split(" -> ")
            point_1, point_2 = point_1.split(","), point_2.split(",")
            data.append(
                [
                    (int(point_1[0]), int(point_1[1])),
                    (int(point_2[0]), int(point_2[1])),
                ]
            )
    return data


def part_1(data: List[List[Tuple[int, int]]]) -> int:
    dim = np.array(data).max()
    grid = np.zeros((dim + 1, dim + 1))
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            grid[x1, min(y1, y2): max(y1, y2) + 1] += 1
        elif y1 == y2:
            grid[min(x1, x2): max(x1, x2) + 1, y1] += 1
    return grid[grid >= 2].size


def part_2(data: List[List[Tuple[int, int]]]) -> int:
    dim = np.array(data).max()
    grid = np.zeros((dim + 1, dim + 1))
    for (x1, y1), (x2, y2) in data:
        x, y = x1, y1
        grid[x, y] += 1
        while x != x2 or y != y2:
            if x != x2:
                x += (1 if x < x2 else -1)
            if y != y2:
                y += (1 if y < y2 else -1)
            grid[x, y] += 1
    return grid[grid >= 2].size


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1: {part_1(data)} points where lines overlap")
    print(f"Part 2: {part_2(data)} points where lines overlap")
