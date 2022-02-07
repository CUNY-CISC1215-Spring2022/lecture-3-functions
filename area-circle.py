import math

def area_circle(r):
    """Calculate and print the area of a circle given a radius"""
    a = math.pi * (r ** 2)
    print(a)

area_circle(3)      # Given radius 3 from lecture slides
area_circle(5)      # Given radius 5 from lecture slides
area_circle(14/2)   # Given diameter 14 from lecture slides, calculate radius here