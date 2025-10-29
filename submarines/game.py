import random
from .board import *
from .placement import place_random_ships as prs
def init_game(size: int, n_ships: int, max_shots: int):
    ships = prs(create_matrix(size), n_ships)
    bool_board = create_bool_matrix(size)



    return { 
  "size": size, 
  "ships": ships, 
  "shots": bool_board, 
  "n_ships": n_ships, 
  "max_shots": max_shots, 
  "shots_used": 0 
} 


def one_shoot(state: dict):
    x = random.randint(0, state["size"] -1)
    y = random.randint(0, state["size"] -1)
    return x , y


def check_validation(state: dict, x: int, y: int):
    boarders = in_bounds(state["size"], x, y)
    return boarders and state["ships"][x][y] != "v"  


def update_shoot(state: dict):
    state["shots_used"] += 1
    return state["shots_used"]


def shoot(state: dict, x: int, y: int):
    result = False
    if check_validation(state, x, y):
        if state["ships"][x][y] == 0:
            state["ships"][x][y] = "x"
            result = False
        else:
            state["ships"][x][y] = "v"
            state["shots"][x][y] = True
            result = True
        print(f"you shot {update_shoot(state)} times")

    return result
 

def is_won(state: dict):
    return state["n_ships"] == count_2d_array(state["shots"], True)

 
def is_lost(state: dict):
    return state["shots_used"] >= state["max_shots"]
 

def shots_left(state: dict):
    return state["max_shots"] - state["shots_used"]
 

def remaining_ships(state: dict): 
    return state["n_ships"] - count_2d_array(state["shots"], True)


