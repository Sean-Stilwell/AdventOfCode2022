def is_touching(head_position, tail_position):
    # Check if the head is touching the tail
    if (abs(head_position[0] - tail_position[0]) <= 1) and (abs(head_position[1] - tail_position[1]) <= 1):
        return True
    else:
        return False

def move_tail(head_position, tail_position):
    # If the head and the tail are in the same column
    if head_position[0] == tail_position[0]:
        # If the head is 2 units up, move the tail up
        if head_position[1] - tail_position[1] == 2:
            tail_position = (tail_position[0], tail_position[1] + 1)
        # If the head is 2 units down, move the tail down
        if head_position[1] - tail_position[1] == -2:
            tail_position = (tail_position[0], tail_position[1] - 1)

    # If the head and the tail are in the same row
    if head_position[1] == tail_position[1]:
        # If the head is 2 units right, move the tail right
        if head_position[0] - tail_position[0] == 2:
            tail_position = (tail_position[0] + 1, tail_position[1])
        # If the head is 2 units left, move the tail left
        if head_position[0] - tail_position[0] == -2:
            tail_position = (tail_position[0] - 1, tail_position[1])

    # If they are not in the same row or column, move the tail diagonally
    if head_position[0] != tail_position[0] and head_position[1] != tail_position[1]:
        # If the head is 2 or more units up and 1 or more unit right OR 2 or more units right and 1 or more unit up, move the tail up and right
        if (head_position[1] - tail_position[1] >= 1 and head_position[0] - tail_position[0] >= 1) or (head_position[0] - tail_position[0] >= 1 and head_position[1] - tail_position[1] >= 1):
            tail_position = (tail_position[0] + 1, tail_position[1] + 1)
        # If the head is 2 or more units up and 1 or more unit left OR 2 or more units left and 1 or more unit up, move the tail up and left
        if (head_position[1] - tail_position[1] >= 1 and head_position[0] - tail_position[0] <= -1) or (head_position[0] - tail_position[0] <= -1 and head_position[1] - tail_position[1] >= 1):
            tail_position = (tail_position[0] - 1, tail_position[1] + 1)
        # If the head is 2 or more units down and 1 or more unit right OR 2 or more units right and 1 or more unit down, move the tail down and right
        if (head_position[1] - tail_position[1] <= -1 and head_position[0] - tail_position[0] >= 1) or (head_position[0] - tail_position[0] >= 1 and head_position[1] - tail_position[1] <= -1):
            tail_position = (tail_position[0] + 1, tail_position[1] - 1)
        # If the head is 2 or more units down and 1 or more unit left OR 2 or more units left and 1 or more unit down, move the tail down and left
        if (head_position[1] - tail_position[1] <= -1 and head_position[0] - tail_position[0] <= -1) or (head_position[0] - tail_position[0] <= -1 and head_position[1] - tail_position[1] <= -1):
            tail_position = (tail_position[0] - 1, tail_position[1] - 1)

    return tail_position

def move(head_position, tails_positions, direction, steps, first_tail_visited, final_tail_visited):
    # Move the head and tail in the given direction
    for _ in range(steps):
        if direction == 'U':
            head_position = (head_position[0], head_position[1] + 1)
        elif direction == 'D':
            head_position = (head_position[0], head_position[1] - 1)
        elif direction == 'R':
            head_position = (head_position[0] + 1, head_position[1])
        elif direction == 'L':
            head_position = (head_position[0] - 1, head_position[1])

        # If the head is not touching the tail, move the tail
        for i in range(9):
            if i == 0:
                if not is_touching(head_position, tails_positions[i]):
                    tails_positions[i] = move_tail(head_position, tails_positions[i])
            else:
                if not is_touching(tails_positions[i-1], tails_positions[i]):
                    tails_positions[i] = move_tail(tails_positions[i-1], tails_positions[i])

        if tails_positions[0] not in first_tail_visited:
            first_tail_visited.append(tails_positions[0])
        if tails_positions[8] not in final_tail_visited:
            final_tail_visited.append(tails_positions[8])

    return head_position, tails_positions

if __name__ == '__main__':
    directions = [] # List of directions
    distances = [] # List of distances for each direction

    head_position = (0, 0) # Initial head position
    tails_positions = [] # Initial tail position
    for i in range(9):
        tails_positions.append((0, 0))

    first_tail_visited = [] # List of tail positions visited
    first_tail_visited.append(tails_positions[0]) # Add the initial tail position to the list

    final_tail_visited = [] # List of tail positions visited
    final_tail_visited.append(tails_positions[8]) # Add the initial tail position to the list

    # Read the input file rope.txt
    with open('./data/rope.txt', 'r') as f:
        # Iterate over each line
        for line in f:
            # Split the line into direction and distance
            direction, distance = line.split()
            # Append the direction and distance to the list
            directions.append(direction)
            distances.append(int(distance))
    
    # Iterate over each direction and distance
    for direction, distance in zip(directions, distances):
        head_position, tail_position = move(head_position, tails_positions, direction, distance, first_tail_visited, final_tail_visited)

    print('PART 1: The first tail has visited', len(first_tail_visited), 'squares.')
    print('PART 2: The last tail has visited', len(final_tail_visited), 'squares.')