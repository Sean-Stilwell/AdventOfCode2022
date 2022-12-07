import sys

def machine(s, count):
    for i in range(len(s) - count):
        if len(set(s[i:i+count])) == count: # Check if all characters are unique
            return i + count

# Main function
if __name__ == "__main__":
    # Read input from command line
    input = sys.argv[1]

    # Convert input to list of characters
    input = list(input)

    # Call machine function for part one
    res1 = machine(input, 4)
    print("Result: " + str(res1))

    # Call machine function for part two
    res2 = machine(input, 14)
    print("Result: " + str(res2))

    print("Done")