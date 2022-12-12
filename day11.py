class Monkey:
    def __init__(self, name, operation_code, operation_value, test, next_true, next_false, items=[]):
        self.name = name
        self.operation_code = operation_code
        self.operation_value = operation_value
        self.test = test
        self.next_true = next_true
        self.next_false = next_false
        self.items = items
        self.counter = 0

    def operate(self, x, PART, product_of_divisors):
        if self.operation_value == "old":
            val = x
        else:
            val = self.operation_value
        
        case = {
            "+": x + val,
            "*": x * val,
        }

        if PART == 1: # For Part 1, we control the worry by dividing by 3
            return case.get(self.operation_code, x) // 3
        else: # For Part 2, we control the worry by dividing by the product of the divisors and using the modulo
            return case.get(self.operation_code, x) % product_of_divisors

    def test_val(self, x):
        return x % self.test == 0

def build_monkey(lines):
    # The monkey's name is the 7th character in the first line
    name = int(lines[0][7])

    # The monkey's items are shown in the 2nd line, starting at the 19th character
    items = lines[1][18:].split(", ")
    items = [int(item) for item in items]

    # The operation code is the 24th character in the 3rd line
    operation_code = lines[2][23]

    # The operation value starts from the 26th character in the 3rd line NOTE: This can be "old" or an integer
    operation_value = lines[2][25:]
    if operation_value != "old":
        operation_value = int(operation_value)

    # The test starts at the 22nd character in the 4th line
    test = int(lines[3][21:])

    # The next monkey if the test is true is identified by the 30th character in the 5th line
    next_true = int(lines[4][29])

    # The next monkey if the test is false is identified by the 31st character in the 6th line
    next_false = int(lines[5][30])

    return Monkey(name, operation_code, operation_value, test, next_true, next_false, items)

def monkey_business(monkeys):
    # Take the 2 highest 'counter' values for the monkeys and return the product
    monkeys.sort(key=lambda x: x.counter, reverse=True)
    return monkeys[0].counter * monkeys[1].counter

if __name__ == "__main__":
    PART = 2

    with open("./data/monkeys.txt", "r") as f:
        data = f.read().splitlines()
    
    monkeys = []
    # We want to pass the lines 6 at a time to build_monkey, 1-6, 8-13, 15-20, etc.
    for i in range(0, len(data), 7):
        monkeys.append(build_monkey(data[i:i+6]))

    product_of_divisors = 1 # For Part 2, we use this as a control variable for the worry.
    if PART == 1:
        x = 20
    else:
        x = 10000
        for monkey in monkeys:
            product_of_divisors *= monkey.test # Used for modulo, so it does not grow too large

    # We repeat the following for 5 iterations
    for i in range(x):
        # For each monkey, we perform the operation on each item
        for monkey in monkeys:
            while len(monkey.items) > 0:
                temp = monkey.items[0]
                temp = monkey.operate(temp, PART, product_of_divisors)

                # If the test is true, the item is given to the next_true monkey
                if monkey.test_val(temp):
                    monkeys[monkey.next_true].items.append(temp)
                # If the test is false, the item is given to the next_false monkey
                else:
                    monkeys[monkey.next_false].items.append(temp)

                # We remove the item at j from the current monkey
                monkey.items.pop(0)
                monkey.counter += 1

        if PART == 2 and (i + 1) % 1000 == 0:
            print("\nAfter iteration", i + 1, " the monkeys have: ")
            for monkey in monkeys:
                print('Monkey', monkey.name, ':', monkey.items)
        elif PART == 1:
            print("\nAfter iteration", i + 1, " the monkeys have: ")
            for monkey in monkeys:
                print('Monkey', monkey.name, ':', monkey.items)

    # Print how many items each monkey has inspected
    print()
    for monkey in monkeys:
        print("Monkey", monkey.name, "has inspected", monkey.counter, "items")

    # Check counter for each monkey. Multiply the highest two together
    business = monkey_business(monkeys)
    print("\nThe business is", business)