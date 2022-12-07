import sys

if __name__ == "__main__":
    elves = {}
    counter = 0

    # Read the input file elves.txt
    with open("./data/elves.txt", "r") as f:
        # Initialize the current elf
        elves[counter] = 0

        # Read each line. A blank line indicates a new elf.
        for line in f:
            if line == "\n":
                counter += 1
                elves[counter] = 0
            else:
                # Add the line to the current elf
                elves[counter] += int(line)

    # Find the elf with the most calories
    max_calories = 0
    for elf in elves:
        if elves[elf] > max_calories:
            max_calories = elves[elf]
    print("Max calories: " + str(max_calories))

    # Find the top 3 elves by calories
    top_elves = []
    for elf in elves:
        if len(top_elves) < 3:
            top_elves.append(elves[elf])
        else:
            # Find the elf with the least calories
            min_calories = min(top_elves)
            if elves[elf] > min_calories:
                top_elves.remove(min_calories)
                top_elves.append(elves[elf])
    # Find the total calories of the top 3 elves
    total_calories = 0
    for elf in top_elves:
        total_calories += elf
    print("Total calories: " + str(total_calories))