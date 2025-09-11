#!/usr/bin/python3
"""
Module pour diviser une matrice
Contient une fonction pour diviser tous les éléments
d'une matrice par un nombre donné
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not matrix or not all(row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix
               for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
