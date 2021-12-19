from collections import Counter


def load_data(file):
    with open(file) as infile:
        init_str = ""
        char_map = {}
        for i, line in enumerate(infile):
            if i == 0:
                init_str = line.strip()
            elif line == "\n":
                pass
            else:
                chars, new_char = line.strip().split(" -> ")
                char_map[chars] = new_char
    return init_str, char_map


def iterate_n(n, s, char_map):
    pair_counts = {i: 0 for i in char_map.keys()}
    char_counts = Counter(s)

    for i in range(1, len(s)):
        pair_counts[s[i - 1: i + 1]] += 1

    for i in range(n):
        new_counts = {i: 0 for i in char_map.keys()}
        for pair in pair_counts:
            first, second = pair
            new_char = char_map[pair]
            first = first + new_char
            second = new_char + second
            new_counts[first] += pair_counts[pair]
            new_counts[second] += pair_counts[pair]
            char_counts[new_char] += pair_counts[pair]
        pair_counts = new_counts
    counts = sorted(char_counts.values())
    return counts[-1] - counts[0]


if __name__ == "__main__":
    s, char_map = load_data("input.txt")
    print(f"Part 1: {iterate_n(10, s, char_map)}")
    print(f"Part 2: {iterate_n(40, s, char_map)}")
