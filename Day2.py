def dimensions_to_area(dimensions):
    areas = dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]
    return sum(areas)*2 + min(areas)


def dimensions_to_perimeter(dimensions):
    perimeters = dimensions[0] + dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[2]
    return min(perimeters)*2 + (dimensions[0]*dimensions[1]*dimensions[2])


input_dimensions = [[int(i) for i in d.split('x')] for d in open("resources/day2.txt").read().splitlines()]
dim_list = [dimensions_to_area(d) for d in input_dimensions]
print(sum(dim_list))

ribbon = [dimensions_to_perimeter(d) for d in input_dimensions]
print(sum(ribbon))
