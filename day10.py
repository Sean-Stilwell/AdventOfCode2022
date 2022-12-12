def part2_splitter(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == '__main__':
    cycles = 1
    register = 1
    amounts = []
    # Read the cpu-instructions.txt file
    with open('./data/cpu-instructions-test.txt', 'r') as f:
        for line in f:
            instructions = line.split(' ')
            instruction = instructions[0]

            if instruction.find('addx') == 0:
                quantity = int(instructions[1])
                amounts.append(register)
                amounts.append(register)
                register += quantity # after 2nd cycle, we change it.
            else:
                amounts.append(register)

    # Sum the amounts of 20, 60, 100, 140, etc...
    sum = 0
    for i in range(19, len(amounts), 40):
        sum += amounts[i] * (i + 1)
    print("(Part 1) The total signal is", sum)

    print("(Part 2) The screen looks like this:")
    screen = ['.' for _ in range(240)]
    
    for location,number in enumerate(amounts):
        column = location % 40
        window = [column - 1, column, column + 1]
        if number in window:
            screen[location] = '#'

    for line in part2_splitter(screen,40):
        print(' '.join(line))
    