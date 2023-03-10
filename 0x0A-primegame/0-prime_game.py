#!/usr/bin/python3
"""
Contains prime_game function
"""
from typing import List


def isWinner(x: int, nums: List) -> str:
    """
    A two players Prime game
    args:
      x: number of rounds
      nums: is an array of n numbers
    Returns:
      A string representing the player
    """
    for r in range(1, x + 1):
        rounds = r
        max_picks = max(nums)
        prime_no_from_picks = []
        for m in range(2, max_picks + 1):
            for j in range(2, int(m ** 0.5) + 1):
                if m % j == 0:
                    break
            else:
                prime_no_from_picks.append(m)
        count = 0
        count_list = []
        for i in range(len(prime_no_from_picks)):
            picker = prime_no_from_picks[i]
            count_list.append(picker)
            count += 1
            for p in nums:
                if p % picker == 0:
                    nums.remove(p)
        if len(count_list) % 2 == 0:
            return "Maria"
        else:
            return "Ben"
