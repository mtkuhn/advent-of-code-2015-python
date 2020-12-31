# Day 2: I Was Told There Would Be No Math
## Part 1
Given an input of line-separated lists of numbers, which represent dimensions
of a cube/rectangular prisms, determine the amount of wrapping paper needed to wrap gifts of those
sizes. We need paper to cover the whole surface area, plus extra that is equal
to the area of the smallest side.
### Solution
```
def dimensions_to_area(dimensions):
    areas = dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]
    return sum(areas)*2 + min(areas)
    
    
input_dimensions = [[int(i) for i in d.split('x')] for d in open("resources/day2.txt").read().splitlines()]
dim_list = [dimensions_to_area(d) for d in input_dimensions]
print(sum(dim_list))
```

## Part 2
With the same input, now calculate the amount of ribbon needed. This is
equal to the size of the smallest perimeter, plus an amount equal to the 
volume to use for the bow.

```
def dimensions_to_perimeter(dimensions):
    perimeters = dimensions[0] + dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[2]
    return min(perimeters)*2 + (dimensions[0]*dimensions[1]*dimensions[2])
   
    
ribbon = [dimensions_to_perimeter(d) for d in input_dimensions]
print(sum(ribbon))
```

## What did I learn?
Python has a `map` function, but it's very ugly in comparison to Kotlin collections
or Java 8 streams. Even more so when you want to string multiple of them together. I opted to use a `comprehension` instead, which is just a fancy kind of `for loop`.
Here's a comparison of them: 
```
    map(lamba x: x+1, some_list)
    
    [x+1 for x in some_list]
```
I imagine the choice between them is a matter of personal preference, but we'll
see if I change my mind as I go along.