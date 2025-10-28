import random
from submarines.board import create_matrix


def place_random_ships(ships: list[list[int]], number_of_ships: int):
    while number_of_ships > 0:
        x = random.randint(0, len(ships) - 1)
        y = random.randint(0, len(ships) - 1)
        if ships[x][y] == 1:
            continue
        else:
            ships[x][y] = 1
            number_of_ships -= 1
    print(ships)

        

place_random_ships(create_matrix(5), 3)




