# Day 3: Perfectly Spherical Houses in a Vacuum
## Part 1
Given a list of directions to a grid of houses,  listed as `>`, `<`, `v`, or `^`,
find the number of houses given presents (all in the path given by the directions).
### Solution
First I defined a `dictionary` for the directions, so that I can quickly
map them to a vector(represented as a `tuple`) in 2-D space.
```
directionVector = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0)
}
```
Then I created a function to iterate over the directions, adding
passed coordinates to a `set`.
```
def get_houses_for_directions(dirs):
    position = (0, 0)
    present_locations = {position}
    for v in [directionVector.get(d) for d in dirs]:
        position = (position[0]+v[0], position[1]+v[1])
        present_locations.add(position)
    return present_locations

directions = open("resources/day3.txt").read()
print(len(get_houses_for_directions(directions)))
```
## Part 2
Now there are two Santas delivering presents, the same instructions
should be alternated between Santa and Robo-Santa.
### Solution
I can re-use my code by splitting the input between two function calls
and performing a union on the results. The slicing functions in Python
have an interesting 3rd arg that comes in handy.
```
all_houses = get_houses_for_directions(directions[::2]).union(get_houses_for_directions(directions[1::2]))
print(len(all_houses))
```
## What did I learn?
1. Python's slicing function has a 3rd arg for 'step'. By specifying `some_collection[::2]` I can
iterate every 2nd item. By specifying `some_collection[1::2]` I can chop off the first character, thus offsetting it by one.
2. A function of `set(elements)` can be used to create a set, but be careful! I first tried to pass a tuple of (0, 0)
into this and it interpreted it as a list of `0, 0`. I found alternative way to list element by element using curly braces: `{(0, 1)}`.
3. Dictionaries are a map (data structure) used by Python. I don't know why they use a different term.