#!/usr/bin/python3
"""A module that solves the N-queens Problem"""

from copy import deepcopy
import sys


def build_array(n: int):
    """Builds an array from a given number"""
    array = []
    if n >= 4:
        row = []
        for _ in range(n):
            row.append(0)

        for _ in range(n):
            array.append(row.copy())
    return array


def is_safe(array, row: int, col: int) -> bool:
    """Checks if a spot on the chessboard is safe"""

    # check if the current column doesn't contain any queens
    vert_row = row
    while vert_row >= 0:
        if array[vert_row][col]:
            return False
        vert_row -= 1

    # check if the diagonal to the left contains any queens
    diag_row = row
    diag_col = col
    while diag_row >= 0 and diag_col >= 0:
        if array[diag_row][diag_col]:
            return False
        diag_row -= 1
        diag_col -= 1

    # check if the diagonal to the right contains any queen
    diag_row = row
    diag_col = col
    while diag_row >= 0 and diag_col >= 0 and diag_col <= len(array) - 1:
        if array[diag_row][diag_col]:
            return False
        diag_row -= 1
        diag_col += 1

    return True


def check_solution(array, row, col):
    """Tries to place the queens where they won't conflict"""
    if row < len(array):
        if not array[0][col]:
            array[0][col] = 1  # sets the first row with a queen

        for e_col in range(len(array)):
            if is_safe(array, row, e_col):
                array[row][e_col] = 1  # set a queen on a row if safe
                check_solution(deepcopy(array), row + 1, col)
                if row == len(array) - 1:
                    print_solution(array)
                else:
                    # if solution is not feasible, remove queen
                    array[row][e_col] = 0


def search_Nqueens(array, col: int) -> None:
    """search for solutions starting from the first column"""
    if col < len(array):
        check_solution(deepcopy(array), 1, col)
        search_Nqueens(array, col + 1)


def print_solution(array):
    """Print the solution in the right format"""
    sol_set = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]:
                sol_set.append([i, j])
    print(sol_set)


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) < 1:
        print("Usage: nqueens N")
        exit(1)
    try:
        queens = int(arg[0])
        if queens < 4:
            print("N must be at least 4")
            exit(1)
        chessboard = build_array(queens)
        search_Nqueens(chessboard, 0)

    except ValueError:
        print("N must be a number")
        exit(1)
