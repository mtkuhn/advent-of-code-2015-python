# Day 1: Not Quite Lisp
## Part 1
Given an input string of parenthesis, where `(` means up and `)` means down, interpret
the string as instructions for moving up and down floors in a building.
Which floor do the instructions eventually take you to?
### Solution
I simply count the occurences of each character and subtract the downs from the ups.
```
input_string = open("resources/day1.txt").read()

ups = input_string.count('(')
downs = input_string.count(')')
print('part1: {0}'.format(ups-downs))
```
## Part 2
In the same instruction set, which character index (starting from `1`) firsts
drops into the basement (`-1`)?
### Solution
This time I needed to actually iterate over elements, adding as we go
and returning once we hit `-1`.
```
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
```
## What did I learn?
I'm starting at zero for Python, so a lot of very basic things are new to me.
1. Getting familiar with syntax. I was prepared for the way Python does
its indentation, but the IDE helped me a lot with handling newlines properly.
2. Basic file operations. `open()` and `read()` are going to be how a lot
of these challenges start.
3. How to iterate over a collection (using `for x in y:`), and how to use `enumerate()` to get
indexes for that collection.
4. String formatting. Using `+` to append a number to a string wasn't working
how I'm used to in Java, but formatting is probably a better practice anyway.