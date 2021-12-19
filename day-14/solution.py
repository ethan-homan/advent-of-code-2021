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


def mutate_str(s, char_map):
    new_str = ""
    for i in range(1, len(s)):
        new_str += s[i - 1]
        new_str += char_map[s[i - 1: i + 1]]
    new_str += s[-1]
    return new_str


if __name__ == "__main__":
    s, char_map = load_data("input.txt")
    for i in range(10):
        s = mutate_str(s, char_map)
    counts = Counter(s)
    _, lowest = counts.most_common()[-1]
    _, greatest = counts.most_common()[0]
    print(greatest - lowest)
