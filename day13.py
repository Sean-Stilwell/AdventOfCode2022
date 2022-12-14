from ast import literal_eval

def parse_data(data):
    left_packets = []
    right_packets = []

    i = 0
    while i < len(data):
        left_packets.append(literal_eval(data[i]))
        right_packets.append(literal_eval(data[i+1]))
        i += 3

    return zip(left_packets, right_packets)

def compare_pair(left, right):
    match left, right:
        case int(), int(): 
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                if diff := compare_pair(l, r):
                    return diff
            return len(left) - len(right)
        case int(), list():
            return compare_pair([left], right)
        case list(), int():
            return compare_pair(left, [right])

def divider_index(packets, target):
    return sum(compare_pair(p, target) <= 0 for p in packets)

if __name__ == '__main__':
    with open('./data/packets.txt') as f:
        data = f.read().splitlines()

    packets = parse_data(data)
    print(sum(i for i, (l, r) in enumerate(packets, 1) if compare_pair(l, r) < 0))

    two, six = [[2]], [[6]]
    packets += [two, six]
    print(divider_index(packets, two) * divider_index(packets, six))