

def create_matrix(size: int, fill: int = 0):
    matrix = []
    for i in range(size):
        vector = []
        for j in range(size):
            vector.append(fill)
        matrix.append(vector)
    return matrix


# print(pd.DataFrame(create_matrix(5)))
 

def create_bool_matrix(size: int, fill: bool = False):
    return create_matrix(size, fill)


# print(pd.DataFrame(create_bool_matrix(5)))


def count_2d_array(arr : list, value):
    counter = 0
    for row in arr:
        for col in row:
            if col == value:
                counter += 1
    return counter


def in_bounds(size: int, x: int, y: int):
    return x <= size >= y

# print(in_bounds(5, 3 ,6))

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]):     
    return count_2d_array(ships, 1) - count_2d_array(shots, True)

# print(count_remaining_ships(create_matrix(5), create_bool_matrix(5)))


def render_public(ships: list[list[int]], shots: list[list[bool]]):
    return str 


def render_reveal(ships: list[list[int]], shots: list[list[bool]]):
    return str 
