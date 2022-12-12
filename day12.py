def get_unvisited(visited,paths,target=None):
    unvisited = []
    distances = []
    target_distance = []
    for i, _ in enumerate(visited):
        for j, value in enumerate(visited[i]):
            if not value and paths[i][j] < float('inf'):
                unvisited.append((i,j))
                distances.append(paths[i][j])
                if target is not None:
                    target_distance.append(abs(i - target[0]) + abs(j - target[1]))

    if target is None: # Order by tentative distance
        return [x for _, x in sorted(zip(distances, unvisited))]
    else: # Order by distance to target
        return [x for _, x in sorted(zip(target_distance, unvisited))]

def find_paths(start_i, start_j, paths, visited):
    for i in [start_i - 1, start_i + 1]:
        if i >= 0 and i < len(paths) and not visited[i][start_j]:
            dist = ord(map[i][start_j]) - ord(map[start_i][start_j])
            if dist <= 1:
                path = paths[start_i][start_j] + 1
                current_path = paths[i][start_j]
                if path < current_path:
                    paths[i][start_j] = path

    for j in [start_j - 1, start_j + 1]:
        if j >= 0 and j < len(paths[0]) and not visited[start_i][j]:
            dist = ord(map[start_i][j]) - ord(map[start_i][start_j])
            if dist <= 1:
                path = paths[start_i][start_j] + 1
                current_path = paths[start_i][j]
                if path < current_path:
                    paths[start_i][j] = path

    visited[start_i][start_j] = True
    return paths, visited

def find_shortest_path(map,source,target):
    paths = [[float('inf') for _ in map[0]] for _ in map]
    visited = [[False for _ in map[0]] for _ in map]

    paths[source[0]][source[1]] = 0
    unvisited = get_unvisited(visited,paths)

    while not visited[target[0]][target[1]] and len(unvisited) > 0:
        paths, visited = find_paths(*unvisited[0], paths, visited)
        unvisited = get_unvisited(visited, paths)
    
    return paths[target[0]][target[1]],paths

if __name__ == '__main__':
    with open('./data/heightmap.txt') as f:
        data = f.read().splitlines()

    map = [[c for c in line] for line in data]

    for i,line in enumerate(map):
        map[i]=[c for c in line]

    for i,item in enumerate(map):
        for j,item2 in enumerate(item):
            if item2=='S': # Start
                source=(i,j)
                map[i][j]='`' # We use '`' as that immediately precedes 'a' in the ascii table
            if item2=='E': # Target
                target = (i,j)
                map[i][j] = '{' # We use '{' as that immediately follows 'z' in the ascii table

    part1, paths = find_shortest_path(map,source,target)

    print('Part 1:',part1)

    starts = []
    best = float('inf')
    for i,row in enumerate(map):
        for j,_ in enumerate(row):
            if map[i][j] == 'a':
                shortest, _ = find_shortest_path(map, (i,j), target)
                if shortest < best:
                    best = shortest

    print('Part 2:',best)