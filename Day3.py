directions = open("resources/day3.txt").read()

directionVector = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0)
}


def get_houses_for_directions(dirs):
    position = (0, 0)
    present_locations = {position}
    for v in [directionVector.get(d) for d in dirs]:
        position = (position[0]+v[0], position[1]+v[1])
        present_locations.add(position)
    return present_locations


print(len(get_houses_for_directions(directions)))
all_houses = get_houses_for_directions(directions[::2]).union(get_houses_for_directions(directions[1::2]))
print(len(all_houses))


# 2361 too high
