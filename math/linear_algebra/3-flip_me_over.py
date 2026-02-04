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
    # Using list comprehension
    return [[matrix[row][col] for row in range(len(matrix))] 
            for col in range(len(matrix[0]))]
