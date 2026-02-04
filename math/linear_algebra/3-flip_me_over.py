#!/usr/bin/env python3
"""
Module for transposing a 2D matrix
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix
    
    Args:
        matrix: 2D matrix to transpose
        
    Returns:
        list: New transposed matrix
    """
    # Get dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty transposed matrix
    transpose = []
    
    # For each column in original matrix, create a new row in transpose
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transpose.append(new_row)
    
    return transpose
