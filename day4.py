def parse_line(line):
    # Split into the two elves' sections
    tasks = line.split(',')

    # Retrieve and return the sections for both elves
    elf_1 = int(tasks[0].split('-')[0]), int(tasks[0].split('-')[1])
    elf_2 = int(tasks[1].split('-')[0]), int(tasks[1].split('-')[1])

    return elf_1, elf_2

def is_contained(elf1, elf2):
    # Check if the first elf's sections are contained in the second elf's sections
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        return True
    # Check if the second elf's sections are contained in the first elf's sections
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        return True
    return False

def any_overlap(elf1, elf2):
    # Check if the first elf's sections overlap with the second elf's sections
    if elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1]:
        return True
    # Check if the second elf's sections overlap with the first elf's sections
    elif elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]:
        return True
    return False

if __name__ == '__main__':
    count_part_one, count_part_two = 0, 0

    # Read input from the rock-paper-scissors.txt file
    with open('./data/cleanup.txt', 'r') as f:
        # Read each line and take the 2 given letters
        for line in f:
            # Parse the line
            elf1, elf2 = parse_line(line)
            if is_contained(elf1, elf2):
                count_part_one += 1
            if any_overlap(elf1, elf2):
                count_part_two += 1

    print('Number of contained is:', count_part_one)
    print('Number of overlapping is:', count_part_two)