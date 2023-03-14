#!/usr/bin/python3
"""A module that checks if a unicode is valid"""


def validUTF8(data: list) -> bool:
    """return true if a unicode is valid else false"""
    # keep track if we are at the beginning of a character
    checks = 0
    flag = True
    for byte in data:
        # return the number of ones the beginning of the byte
        ones = binary_eq(byte)
        # cheacks if the byte is ascii and its not in
        # the middle of a character that has multiple bytes
        if ones == 0 and checks != 0:
            flag = False
            break

        # check if the byte is acii and its valid
        elif ones == 0 and checks == 0:
            continue

        # checks if the pecedding number of ones is less than 4 OR
        # is a valid character if the ones is greater than one OR
        # is a valid character if ones is equal to one
        elif ones > 4 or\
            (ones > 1 and checks != 0) or\
                (ones == 1 and checks == 0):
            flag = False
            break

        elif ones > 1 and checks == 0:
            checks = ones - 1

        else:
            # keeps track of the number of bytes remaining
            # if we are in a character
            checks -= 1

    # if we hava an uncompleted character than fail
    if checks:
        flag = False
    return flag


def binary_eq(num: int) -> int:
    """return a binary equivalent of the number"""
    ones = 0
    bin_val = bin(num)[2:]
    if len(bin_val) >= 8 and bin_val[-8:].startswith('1'):
        ones = len(bin_val[-8:].partition('0')[0])
    # print("here is the bin: ", bin_val, ones)
    return ones
