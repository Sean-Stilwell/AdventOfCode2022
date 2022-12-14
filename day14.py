def pour_sand(sand):
    stopped = False
    R,C = 0,500
    dr,dc = [1,1,1],[0,-1,1]

    while R < maxR + 2 and not stopped:
        falling = False
        for i in range(3):
            rr, cc = R + dr[i], C + dc[i]
            if (rr,cc) not in rocks and rr < maxR + 2 :
                R,C = rr,cc
                falling = True
                break
            
        if not falling:
            stopped = True
            sand.add((R,C))
            rocks.add((R,C))
    return R,C

if __name__ == '__main__':
    # Read data from the input file
    with open('./data/rocks.txt') as f:
        data = [[[int(r) for r in x.split(',')] for x in lines.split(' -> ')] for lines in f.readlines()]
        
    rocks = set()
    minC, minR, maxC, maxR = 10000, 0, 0, 0

    for line in data: # One line from the raw data, which is a series of coordinates that make up a line
        xC,xR = line[0] # We take the first coordinate as the starting point
        for yC,yR in line[1:]: # We iterate through the rest of the coordinates
            tmp = [yC,yR]

            if xR == yR: # If the height is the same, we add all the rocks in between on the row
                if yC<xC:
                    xC,yC = yC,xC
                for c in range(xC,yC+1):
                    rocks.add((xR,c))
            if xC == yC: # If the width is the same, we add all the rocks in between on the column
                if yR<xR:
                    xR,yR = yR,xR
                for r in range(xR,yR+1):
                    rocks.add((r,xC))

            xC,xR = tmp # We set the next starting point to the previous ending point

            # Grid boundaries
            if minC > xC: 
                minC = xC
            if maxC < xC: 
                maxC = xC
            if maxR < xR: 
                maxR = xR

    sand = set()
    count = 0
    part1 = True
    R, C = 0, 0

    while (R,C) != (0,500): # While we haven't reached the top (0,500)
        R, C = pour_sand(sand)
        if R>maxR and part1:
            print('Part 1:', count)
            part1 = False
        count += 1
    print('Part 2:', count)