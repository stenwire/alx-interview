#!/usr/bin/python3
"""
Contains pascal_triangle function
"""


def pascal_triangle(n):
    """Creates a pascal triangle"""
    triangle = []
    if (n <= 0):
        return []
    for row in range(n):
        curr = [None] * (row + 1)
        curr[0], curr[-1] = 1, 1
        for col in range(1, row):
            above_to_left_elt = triangle[row - 1][col-1]
            above_to_right_elt = triangle[row - 1][col]
            curr[col] = above_to_left_elt + above_to_right_elt
        triangle.append(curr)
    return triangle
