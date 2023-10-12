#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for i, row in enumerate(new_matrix):
        for idx, col in enumerate(new_matrix):
            new_matrix[i][idx] = row[idx] ** 2
    return new_matrix
