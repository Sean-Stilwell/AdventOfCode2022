def visible_up(forest, row, col):
    # Check if the tree is visible from above
    for r in range(row - 1, -1, -1):
        if forest[r][col] >= forest[row][col]:
            return False, row - r
    return True, row

def visible_down(forest, row, col):
    # Check if the tree is visible from below
    for r in range(row + 1, len(forest), 1):
        if forest[r][col] >= forest[row][col]:
            return False, r - row
    return True, len(forest) - row - 1

def visible_left(forest, row, col):
    # Check if the tree is visible from above
    for c in range(col - 1, -1, -1):
        if forest[row][c] >= forest[row][col]:
            return False, col - c
    return True, col

def visible_right(forest, row, col):
    # Check if the tree is visible from above
    for c in range(col + 1, len(forest[row]), 1):
        if forest[row][c] >= forest[row][col]:
            return False, c - col
    return True, len(forest[row]) - col - 1

if __name__ == '__main__':
    forest = []
    # Read the input file trees.txt
    with open('./data/trees.txt', 'r') as f:
        # Iterate over the lines in the file
        for line in f:
            row = []
            # Strip the newline character from the line
            line = line.strip()
            # Iterate over the characters in the line
            for char in line:
                # Append the character to the row
                row.append(char)
            # Append the row to the forest
            forest.append(row)

    counter = 0
    max_scenic_score = -1
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            down = visible_down(forest, row, col)
            up = visible_up(forest, row, col)
            left = visible_left(forest, row, col)
            right = visible_right(forest, row, col)

            if down[0] or up[0] or left[0] or right[0]:
                counter += 1

            scenic_score = down[1] * up[1] * left[1] * right[1]
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print('The number of visible trees is:', counter)
    print('The maximum scenic score is:', max_scenic_score)