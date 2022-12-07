def rock_paper_scissors(moveA, moveB):
    score = 0

    if moveB == 'X': # Rock by B
        score += 1
        if moveA == 'A': # Rock by A
            score += 3
        elif moveA == 'B': # Paper by A
            score += 0
        elif moveA == 'C': # Scissors by A
            score += 6
    elif moveB == 'Y': # Paper
        score += 2
        if moveA == 'A': # Rock by A
            score += 6
        elif moveA == 'B': # Paper by A
            score += 3
        elif moveA == 'C': # Scissors by A
            score += 0
    elif moveB == 'Z': # Scissors
        score += 3
        if moveA == 'A': # Rock by A
            score += 0
        elif moveA == 'B': # Paper by A
            score += 6
        elif moveA == 'C': # Scissors by A
            score += 3

    return score

def solver(moveA, result):
    score = 0
    if result == 'X': # Loss needed
        score += 0
        if moveA == 'A': # Rock, scissors loses
            score += 3
        elif moveA == 'B': # Paper, rock loses
            score += 1
        elif moveA == 'C': # Scissors, paper loses
            score += 2
    elif result == 'Y': # Draw needed
        score += 3
        if moveA == 'A': # Rock, rock needed
            score += 1
        elif moveA == 'B': # Paper, paper needed
            score += 2
        elif moveA == 'C': # Scissors, scissors needed
            score += 3
    elif result == 'Z': # Win needed
        score += 6
        if moveA == 'A': # Rock, paper wins
            score += 2
        elif moveA == 'B': # Paper, scissors wins
            score += 3
        elif moveA == 'C': # Scissors, rock wins
            score += 1
    return score

if __name__ == '__main__':
    total_score = 0
    secret_score = 0

    # Read input from the rock-paper-scissors.txt file
    with open('./data/rock-paper-scissors.txt', 'r') as f:
        # Read each line and take the 2 given letters
        for line in f:
            moveA = line[0]
            moveB = line[2]
            
            total_score += rock_paper_scissors(moveA, moveB)
            secret_score += solver(moveA, moveB)

    print('Part A:', total_score)
    print('Part B:', secret_score)