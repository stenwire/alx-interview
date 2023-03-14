#!/usr/bin/python3
"""A module that return the pascal triangle of any integer
passed to a function"""


def pascal_triangle(n):
    """Implementation of the pascal triangle"""
    p_traing = []
    for idx in range(n):
        if idx == 0:
            p_traing.append([1])
            continue
        if idx == 1:
            p_traing.append([1, 1])
            continue
        row = []
        row.append(1)
        prev_row = p_traing[idx - 1]
        for i in range(len(prev_row)):
            if i == 0:
                continue
            row.append(prev_row[i] + prev_row[i - 1])
        row.append(1)
        p_traing.append(row)
    return p_traing
