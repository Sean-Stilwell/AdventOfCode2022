PART = 2 # Change this to 1 or 2 to run the corresponding part of the challenge

def read_file():
    with open('./data/crane.txt', 'r') as f:
        stacks = {}
        instructions = []
        flag = False

        for line in f: # Iterating through each line of the file
            i, pos = 1,1

            while i < len(line) and not flag: # Iterating through every 4 characters in the line, where crates are located
                if line[i] != ' ':
                    if line[i].isnumeric(): # This means we've reached the end of the crate stacks.
                        flag = True
                        break
                    if pos in stacks: # If the stack already exists, append the crate to the stack.
                        stacks[pos].append(line[i])
                    else: # If the stack doesn't exist, create it and append the crate to it.
                        stacks[pos] = [line[i]]
                i += 4
                pos += 1
            
            # If the flag is toggled, we're in the instructions. We log them.
            if flag:
                instructions.append(line)

    # Remove the 1st and 2nd elements of the instructions list, as they are not needed.
    instructions.pop(0)
    instructions.pop(0)

    return stacks, instructions
        

if __name__ == "__main__":
    stacks, instructions = read_file()

    # We then need to reverse the stacks so that the top of the stack is the last element in the list.
    for stack in stacks:
        stacks[stack].reverse()

    # We split the instructions so we can pull specific parts of the instructions.
    for i in range(len(instructions)):
        instructions[i] = instructions[i].split()

    # Follow the instructions for all the movements to be made.
    if PART == 1:
        for instruction in instructions:
            number_to_move = int(instruction[1])
            from_stack = int(instruction[3])
            to_stack = int(instruction[5])

            for i in range(number_to_move):
                stacks[to_stack].append(stacks[from_stack].pop())
    else:
        # We can now move multiple creates at once rather than just one.
        for instruction in instructions:
            number_to_move = int(instruction[1])
            from_stack = int(instruction[3])
            to_stack = int(instruction[5])

            moving = []
            for i in range(number_to_move):
                moving.append(stacks[from_stack].pop())
            while len(moving) > 0:
                stacks[to_stack].append(moving.pop())

    # Find the top of each stack in order of key (lowest - highest) and print the result.
    for stack in sorted(stacks):
        print(stacks[stack][-1], end='')