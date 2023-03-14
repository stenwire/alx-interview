#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number and
its multiples from the set. The player that cannot make
a move loses the game.

They play x rounds of the game, where n may be
different for each round. Assuming Maria always goes first
and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
"""


def isWinner(x: int, nums: list):
    """
    Calculates the winner after a sets of rounds played
    """
    cached_multiples = set()
    cached_prime = cache_prime(max(nums))
    players = {"Maria": 0, "Ben": 0}

    for num in range(x):
        flag = Maria = Ben = 0
        for i in range(2, nums[num] + 1):
            if (i not in cached_multiples) and ((i in cached_prime)):
                if flag == 0:
                    find_mutiples(i, nums[num], cached_multiples)
                    Maria += 1
                    flag = 1

                elif flag == 1:
                    find_mutiples(i, nums[num], cached_multiples)
                    Ben += 1
                    flag = 0
                cached_prime.add(i)
        winner = "Ben" if Ben >= Maria else "Maria"
        find_round_winner(players, winner)
    return find_winner(players)


def cache_prime(max_num):
    cache = set()
    for i in range(2, max_num + 1):
        if isPrime(i, cache):
            cache.add(i)
    return cache


def find_winner(players):
    if players["Ben"] > players["Maria"]:
        return "Ben"
    elif players["Ben"] < players["Maria"]:
        return "Maria"
    else:
        return None


def find_round_winner(players: dict, winner: str):
    players[winner] += 1


def find_mutiples(i: int, num: int, cached_multiples: set):
    multiple = i
    while (
        i <= num and (i + multiple < num) and
            (i + multiple) not in cached_multiples):
        i += multiple
        cached_multiples.add(i)


def isPrime(n, cache):
    # Corner cases
    if n <= 1 or n in cache:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True
