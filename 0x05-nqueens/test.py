#!/bin/python3
from unittest import TestCase, main
from pprint import pprint

n_queen = __import__("0-nqueens")


class TestNQueens(TestCase):
    """Test my nqeens module"""

    def test_build_array(self):
        array = n_queen.build_array(4)
        res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertListEqual(array, res)

    def test_is_safe(self):
        array = n_queen.build_array(4)
        self.assertTrue(n_queen.is_safe(array, 0, 1))
        array[0][1] = 1
        self.assertFalse(n_queen.is_safe(array, 1, 2))
        # self.assertFalse(n_queen.is_safe(array, 1, 1))
        # self.assertTrue(n_queen.is_safe(array, 1, 2))
        # array[1][2] = 1
        # self.assertFalse(n_queen.is_safe(array, 2, 3))

        # self.assertTrue(n_queen.is_safe(array, 1, 3))
        
    def test_check_solution(self):
        # array = n_queen.build_array(6)
        # print(n_queen.check_solution(array, 1, 0))
        # print(n_queen.check_solution(array, 1, 1))
        # print(n_queen.check_solution(array, 1, 2))
        # print(n_queen.check_solution(array, 1, 3))
        # print(n_queen.check_solution(array, 1, 4))
        # array = n_queen.build_array(8)
        # n_queen.check_solution(array, 1, 5)
        pass
    
    def test_search_Nqueens(self):
        array = n_queen.build_array(4)
        n_queen.search_Nqueens(array, 0)

if __name__ == "__main__":
    main()
