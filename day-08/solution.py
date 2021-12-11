
def sort_string(s):
    return "".join(sorted(s))


def get_sequence_map(s):

    m = {i: None for i in range(10)}

    # Fix 1, 7, 4, 8 since we know what those values are based on their length
    for i in s:
        i = sort_string(i)
        if len(i) == 2:
            m[1] = i
        elif len(i) == 3:
            m[7] = i
        elif len(i) == 4:
            m[4] = i
        elif len(i) == 7:
            m[8] = i

    # Use the initial mapping to infer the other digits
    for i in s:
        i = sort_string(i)
        if len(i) == 6:
            if len(set(i).intersection(set(m[1]))) == 1:
                m[6] = i
            elif len(set(i).intersection(set(m[4]))) == 3:
                m[0] = i
            elif len(set(i).intersection(set(m[4]))) == 4:
                m[9] = i
            else:
                raise Exception("Length 6 case not accounted for")
        elif len(i) == 5:
            if len(set(i).intersection(set(m[7]))) == 2 and len(set(i).intersection(set(m[4]))) != 2:
                m[5] = i
            elif len(set(i).intersection(set(m[4]))) == 2:
                m[2] = i
            elif len(set(i).intersection(set(m[4]))) == 3:
                m[3] = i
            else:
                raise Exception("Length 5 case not accounted for")
        elif len(i) in [2, 3, 4, 7]:
            pass
        else:
            raise Exception("Sequence invalid")

    return {k: v for v, k in m.items()}


if __name__ == "__main__":
    data = []
    with open("input.txt") as infile:
        for line in infile:
            sequence, output = line.split("|")
            output = output.split()
            sequence = sequence.split()
            data.append([sequence, output])

    count = 0
    for sequence, output in data:
        for i in output:
            if len(i) in [2, 3, 4, 7]:
                count += 1
    print(f"Part 1: {count}")

    count = 0
    for sequence, output in data:
        mapping = get_sequence_map(sequence)
        int_value_str = ''
        for i in output:
            i = sort_string(i)
            int_value_str += str(mapping[i])
        count += int(int_value_str)
    print(f"Part 2: {count}")
