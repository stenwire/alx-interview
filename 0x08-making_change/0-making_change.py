#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins: list, total: int) -> int:
    """
    Determine the fewest number of coins
    needed to meet a given amount total

    Args ->
        coins: list of coins to meet a given amount total
        total: maximum amount to reach

    Returns ->
        fewest number of coins needed
    """

    """
    Determine the amount"""

    new_coins = sorted(coins, reverse=True)
    if total > 0:
        for i in range(len(coins)):
            current_total = 0
            num_of_coins = 0
            while new_coins:
                max_coin = new_coins[0]
                min_coin = new_coins[-1]
                if current_total == total:
                    return num_of_coins
                elif (max_coin + current_total > total) and (
                    min_coin + current_total > total
                ):
                    num_of_coins += 1
                    break
                elif max_coin + current_total > total:
                    new_coins.pop(new_coins.index(max_coin))
                else:
                    num_of_coins += 1
                    current_total += max_coin
            new_coins = sorted(coins, reverse=True)[i + 1:]
        if not coins or num_of_coins > 0:
            return -1
    return 0
