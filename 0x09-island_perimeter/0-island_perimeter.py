#!/usr/bin/python3
"""
A module that calculates the perimetre of an island
"""


def island_perimeter(grid):
    """
    calculates the total perimeter
    of an Island
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += check_rt_lt(grid, i, j)
                perimeter += check_tp_dn(grid, i, j)
    return perimeter


def check_rt_lt(grid, i, j):
    """
    checks the left and right side of
    the grid
    """
    perimeter = 0
    if (j + 1) > (len(grid[i]) - 1) or grid[i][j + 1] == 0:
        perimeter += 1
    if (j - 1) < 0 or grid[i][j - 1] == 0:
        perimeter += 1
    return perimeter


def check_tp_dn(grid, i, j):
    """
    check the top and bottom side of
    the grid
    """
    perimeter = 0
    if (i - 1) < 0 or grid[i - 1][j] == 0:
        perimeter += 1
    if (i + 1) > (len(grid) - 1) or grid[i + 1][j] == 0:
        perimeter += 1
    return perimeter
