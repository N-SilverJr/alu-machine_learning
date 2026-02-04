#!/usr/bin/env python3
"""
Module for calculating the shape of a matrix
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix
    
    Args:
        matrix: A matrix (list of lists) to calculate shape for
        
    Returns:
        list: A list of integers representing the shape
    """
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        if current:
            current = current[0]
        else:
            break
    return shape
