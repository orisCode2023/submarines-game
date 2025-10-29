import random

def place_random_ships(ships: list[list[int]], number_of_ships: int):
    while number_of_ships > 0:
        x = random.randint(0, len(ships) - 1)
        y = random.randint(0, len(ships) - 1)
        if ships[x][y] == 1:
            continue
        else:
            ships[x][y] = 1
            number_of_ships -= 1
    return ships


        





