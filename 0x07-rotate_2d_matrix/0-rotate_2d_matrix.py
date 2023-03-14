#!/usr/bin/python3
"""
A module that rotates a 2D nxn Matrix
"""


def rotate_column(matrix, i: int, j: int, box_indexes) -> None:
    """
    Moves the column value in a circle pattern around the box.

    Args ->
        matrix: Any NxN matrix
        i: starting index(row) of the present box.
        j: starting index(column) of the present box.
        box_indexes: holds the index of the row and column
                     which makes up the box where index 0 is the row
                     and index 1 is the column.

    Description: We all know that a box has 4 sides so if we want to
        rotate a COLUMN 90 degrees, we have to move around the box four
        times and place the value of each column in the right spots.
        Let's say we have a matrix [1, 2, 3
                                    4, 5, 6
                                    7, 8, 9]
        if we called this function with i=0, j=0 and box_indexes=[0, 1]
        our matrix after this call would be [7, 2, 1
                                             4, 5, 6
                                             9, 8, 3]
        so we can see that value at index[0,0] is being rotated 90 degrees
        which is index[0,2] and the value at index[0, 2] is being taken
        to index[1,0] and the value at index[1,0] is being taken to index
        [0, 0]. With this we can see that it rotates it in a circular pattern
    """
    len_mat = len(matrix) - 1
    current_row = matrix[i][j]
    tmp_i, tmp_j = i, j

    for rot in range(4):
        if rot == 0:
            i = j
            next_row = matrix[i][box_indexes[1]]
            matrix[i][box_indexes[1]] = current_row
        elif rot == 1:
            j = len_mat - box_indexes[0] - (j - box_indexes[0])
            next_row = matrix[box_indexes[1]][j]
            matrix[box_indexes[1]][j] = current_row
        elif rot == 2:
            i = len_mat - box_indexes[0] - (box_indexes[1] - j)
            next_row = matrix[i][box_indexes[0]]
            matrix[i][box_indexes[0]] = current_row
        else:
            matrix[tmp_i][tmp_j] = current_row
        current_row = next_row


def get_number_of_iterations(mat_len: int, i: int):
    """
    Calculates the number of iterations required for a given box

    Args ->
        mat_len: length of the matrix
        i: Index of diagonal of a box

    Description: Considered this matrix  [x, x, x, x, x, x
                                          x, 5, 6, 3, 2, x
                                          x, 8, x, x, 4, x
                                          x, 1, x, x, 7, x
                                          x, 5, 2, 7, 1, x
                                          x, x, x, x, x, x]

        To get the number of iterations for this box
        (columns with numbers) we need to take into account
        the index at which the box starts from.
        I know it not that obvious to see at first but we
        can notice that as we go diagonally in to each box the
        width and the length of the box decreases and from critical
        thinking i found out that it depended on the length of the
        matrix, and my current diagonal index; Taking the form

        `len_of_matrix -  diag_index *
            2(because it reduces in both length and width) -
                1(because index starts from zero)`

    Return: The number of iterations for a given diagonal i
    """
    return mat_len - i * 2 - 1


def rotate_full_row(matrix, i: int, j: int, box_indexes) -> None:
    """
    Pick a box and rotates it

    Args ->
        matrix: Any NxN matrix
        i: starting index(row) of the present box.
        j: starting index(column) of the present box.
        box_indexes: holds the index of the row and column
                     which makes up the box.

    Description: This function iterates only over the top of a box
        i.e over the column that makes up the top of the box. It picks the
        index of each column, calls the rotate_column function which rotates
        around the box placing each value in the right spot(More info in
        rotate_column function).
        Imagine we have a matrix [1, 2, 3, 4
                                  2, x, x, 5
                                  1, x, x, 6
                                  0, 9, 8, 7]
        Ignoring the the slots with 'x' as value we can see that we have
        a box that contains 1, 2, 3 ... and in order to rotate the box
        90 degrees we only need to make a certain number of iterations on
        the top of the box. For this example we would need only 3 iteration
        because the value at index [0][0] which is 1 would end up at
        index [0][1] which is its right spot. so we would have to iterate
        till index [0][3] which makes it 3 iterations.

        Ofcourse this could easily get complicated(getting the number
        of iterations) when we have a larger matrix like a 6x6 matrix or
        above and where our inner boxes will be dependant on which diagonal
        we are in. This is why we have the 'get_number_of_iterations'
        function that calculates this for us. More info in the function.
    """
    iteration = get_number_of_iterations(len(matrix), i)
    for row in range(iteration):
        rotate_column(matrix, i, j, box_indexes)
        j += 1


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D nxn Matrix in Place

    Args -> matrix : Any NxN matrix

    Description: This funtion sees a matrix as a set of concentric
        square e.g [1, 1, 1, 1
                    1, 2, 2, 1
                    1, 2, 2, 1
                    1, 1, 1, 1]
        So in the matrix above we can assume that the 1's is box
        and the 2's is another box and we would like to rotate the
        matrix on a box to box level.
        Meaning we rotate the 1's box by 90 degrees the we
        rotate the 2's box by 90 degrees.

        The for loop here lets us move from one box to another
        using diagonals from 0,0 to 1,1(which is our next box) and
        so on until the least possible box is
        reached.
        For each box the rotate_full_row is called. check out docs of
        this function for more info.

    Returns:
        None
    """
    i = j = 0
    n = len(matrix)
    for diag in range(int(len(matrix) / 2)):
        rotate_full_row(matrix, i, j, [i, n - 1 - i])
        i += 1
        j += 1
