import pandas as pd
def create_matrix(size: int, fill: int = 0):
    matrix = []
    for i in range(size):
        vector = []
        for j in range(size):
            vector.append(fill)
        matrix.append(vector)
    return matrix
 

def create_bool_matrix(size: int, fill: bool = False):
    return create_matrix(size, fill)


def count_2d_array(arr : list[list], value):
    counter = 0
    for row in arr:
        counter += row.count(value)
    return counter

# print(count_2d_array([[True, True, False],[True, True, False]], True))


def in_bounds(size: int, x: int, y: int):
    return x <= size >= y


def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]):     
    return count_2d_array(ships, 1) - count_2d_array(shots, True)


def render_public(ships: list[list[int]], shots: list[list[bool]]):
    return str 


def render_reveal(ships: list[list[int]], shots: list[list[bool]]):
    return str 
