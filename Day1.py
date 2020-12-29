input_string = open("resources/day1.txt").read()

ups = input_string.count('(')
downs = input_string.count(')')
print('part1: {0}'.format(ups-downs))


def find_position_for_first_basement():
    level = 0
    for i, char in enumerate(input_string):
        if char == "(":
            level += 1
        else:
            level -= 1
            if level == -1:
                return i+1


print('part2: {0}'.format(find_position_for_first_basement()))

