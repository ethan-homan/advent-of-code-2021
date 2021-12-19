from collections import defaultdict
import numpy as np


def load_data(f):
    with open(f) as infile:
        data = []
        for line in infile:
            data.append(list(line.strip()))
    return np.array(data, dtype=int)


def get_adjacent(point, grid):
    adjacent_indices = []
    if point[0] > 0:
        adjacent_indices.append((point[0] - 1, point[1]))
    if point[0] + 1 < grid.shape[0]:
        adjacent_indices.append((point[0] + 1, point[1]))
    if point[1] > 0:
        adjacent_indices.append((point[0], point[1] - 1))
    if point[1] + 1 < grid.shape[1]:
        adjacent_indices.append((point[0], point[1] + 1))
    return adjacent_indices


def build_bigger_map(base_grid):
    slices = []
    row_base = np.array(base_grid, copy=True)
    for j in range(5):
        row = [row_base]
        next_grid = np.array(row_base, copy=True)
        for i in range(4):
            next_grid += 1
            next_grid[next_grid == 10] = 1
            row.append(next_grid)
            next_grid = np.array(next_grid, copy=True)
        slices.append(np.concatenate(row, axis=1))
        row_base = np.array(row_base, copy=True)
        row_base += 1
        row_base[row_base == 10] = 1
    return np.concatenate(slices, axis=0)


def lowest_cost(node_costs):
    # Needed up pull an algo off the shelf here so using
    # Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
    # using https://github.com/abecus/DS-and-Algorithms/blob/master/graph/dijkstra.py as reference

    # Initialize costs at the maximum
    path_to_node_cost = defaultdict(lambda: float('inf'))

    # Keep track of where we've been and the "frontier" of the search
    visited = set()
    node_queue = []

    # Initialize the queue with the origin and a cost of 0
    starting_node = (0, 0)
    node_costs[starting_node] = 0
    path_to_node_cost[starting_node] = 0
    node_queue.append((0, starting_node))

    while node_queue:
        _, node = node_queue.pop()
        visited.add(node)
        for adj_node in get_adjacent(node, node_costs):
            if adj_node in visited:
                continue

            new_cost = path_to_node_cost[node] + node_costs[adj_node]
            if path_to_node_cost[adj_node] > new_cost:
                path_to_node_cost[adj_node] = new_cost
                node_queue.append((new_cost, adj_node))
                if adj_node == (node_costs.shape[0] - 1, node_costs.shape[1] - 1):
                    return new_cost
        # make sure we can .pop() the lowest cost path off the end of the queue
        node_queue.sort(reverse=True)


if __name__ == "__main__":
    node_costs = load_data("input.txt")
    node_costs_large = build_bigger_map(node_costs)
    print(f"Part 1: {lowest_cost(node_costs)}")
    print(f"Part 2: {lowest_cost(node_costs_large)}")
