# I use a tree for this problem, where each node is a directory.
class Tree:
    def __init__(self, data, parent=None):
        self.children = [] # Directories in the directory
        self.files = {} # Files in the directory, with the name of the file as the key and the size as the value
        self.data = data # Name of the directory
        self.parent = parent # Parent directory

    def isEmpty(self):
        return self.children == [] and self.files == {}

# Calculates the size of a directory and all its children
def calculate_size(tree):
    if tree.isEmpty():
        return 0
    size = 0
    for file in tree.files:
        size += tree.files[file]
    for child in tree.children:
        size += calculate_size(child)
    return size

# Finds all directories under a given size
def find_directories_of_max_size(tree, size = 100000):
    directories = []
    if calculate_size(tree) <= size:
        directories.append(tree)
    for child in tree.children:
        directories += find_directories_of_max_size(child, size)
    return directories

# Finds all directories of at least a certain size (For Part 2)
def find_directories_of_min_size(tree, size = 100000):
    directories = []
    if calculate_size(tree) >= size:
        directories.append(tree)
    for child in tree.children:
        directories += find_directories_of_min_size(child, size)
    return directories

if __name__ == '__main__':
    tree = None

    # Read the input file commands.txt
    with open('./data/commands.txt', 'r') as f:
        for line in f:
            if line[0] == '$': # Indicates line is a command. We look at character 2 and 3 for what type.
                flag = False
                if line[2] == 'c' and line[3] == 'd': # Create a new node
                    # Get the name of the new node
                    name = line[5:-1]
                    if name == '/': # If the new node is the root, we need to create a new tree
                        tree = Tree(name)
                        current = tree
                    elif name == '..': # If the new node is the parent of the current node, we need to go up a level 
                        current = current.parent
                    elif name in [child.data for child in current.children]: # If the new node is a child of the current node, we need to go down a level
                        current = current.children[[child.data for child in current.children].index(name)]
                    else:
                        new = Tree(name, current)
                        current.children.append(new)
                        current = new
                if line[2] == 'l' and line[3] == 's': # Indicates the next lines are going to be a list of files
                    flag = True
            elif flag:
                text = line.split()
                if text[0] == 'dir':
                    # If the directory doesn't exist, we need to create it, even if it's empty.
                    if text[1] not in [child.data for child in current.children]:
                        new = Tree(text[1], current)
                        current.children.append(new)
                else:
                    # If the file doesn't exist, we need to create it.
                    if text[1] not in current.files:
                        current.files[text[1]] = int(text[0])
    
    # For Part 1, we find all directories under 100000 and add up their sizes
    res = 0
    directories = find_directories_of_max_size(tree, 100000)
    for folder in directories:
        res += calculate_size(folder)
    print("PART 1: Total size of all dirs under 100000", res)

    # For Part 2, we find all directories that can free up 30000000 bytes.
    total_space = 70000000
    space_used = calculate_size(tree)
    space_available = total_space - space_used
    needed_space = 30000000 - space_available # Size needed to run the update

    # Find smallest directory of that size to delete
    to_delete = find_directories_of_min_size(tree, needed_space)
    to_delete.sort(key=lambda x: calculate_size(x))
    print("PART 2: Smallest directory to delete", to_delete[0].data, calculate_size(to_delete[0]))