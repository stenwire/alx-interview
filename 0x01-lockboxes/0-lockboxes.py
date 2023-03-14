#!/usr/bin/python3
"""A module that solves the lockboxes problem"""


def canUnlockAll(boxes):
    """Solves the lockboxes problem"""
    index_checker = {0}  # A set to keep track of boxes opened
    check_list = boxes[0].copy()  # A list of keys to check (queue)
    len_boxes = len(boxes)

    for key in check_list:
        if key < len_boxes and key not in index_checker:
            index_checker.add(key)  # add the keys to the set
            check_list.extend(boxes[key])  # append keys to current keys(queue)
            if len(index_checker) == len_boxes:
                return True
    return True if len_boxes == 1 else False
