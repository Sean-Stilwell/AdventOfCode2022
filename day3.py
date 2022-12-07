def split_line(line):
    half = len(line) // 2
    return line[:half], line[half:]

def get_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def get_score_1(line):
    first_half, second_half = split_line(line)
    # Find the letter that appears in both halves
    for letter in first_half:
        if letter in second_half:
            return get_priority(letter)
    return 0

def get_score_2(lines):
    # Find the letter that appears in every set of 3 lines
    for letter in lines[0]:
        if letter in lines[1] and letter in lines[2]:
            return get_priority(letter)
    return 0

if __name__ == '__main__':
    score_1, score_2 = 0, 0
    
    # PART 1 - Find the letter that appears in both halves for each line
    with open('./data/rucksack.txt', 'r') as f:
        for line in f:
            score_1 += get_score_1(line)

    print('Part 1:', score_1)

    # PART 2 - Find the letter that appears in every set of 3 lines
    with open('./data/rucksack.txt', 'r') as f:
        # Read the first 3 lines
        lines = [f.readline(), f.readline(), f.readline()]
        while lines[0]:
            # Find the letter that appears in all 3 lines
            score_2 += get_score_2(lines)
            # Read the next 3 lines
            lines = [f.readline(), f.readline(), f.readline()]

    print('Part 2:', score_2)