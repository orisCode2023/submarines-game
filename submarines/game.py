import random
from .board import *
def init_game(size: int, n_ships: int, max_shots: int):
    return { 
  "size": size, 
  "ships": list[list[int]], 
  "shots": list[list[bool]], 
  "n_ships": n_ships, 
  "max_shots": max_shots, 
  "shots_used": 0 
} 

def check_validation(state: dict, x: int, y: int):
    boarders = in_bounds(state["size"], x, y)
    return boarders and state["ships"][x][y] != "v"  

def shoot(state: dict, x: int, y: int):
    if check_validation:
        result = []
        if state["ships"][x][y] == 0:
            state["ships"][x][y] = "x"
            result = [False, "maybe next time"]
        else:
            state["ships"][x][y] = "v"
            result = [True, "its a hit"]
    return tuple(result)
 

def is_won(state: dict):
    return state["n_ships"] == state["shots"].count(True)

 
def is_lost(state: dict):
    return state["shots_used"] >= state["max_shots"]
 

def shots_left(state: dict):
    return state["max_shots"] - state["shots_used"]
 

def remaining_ships(state: dict): 
    return state["n_ships"] - count_2d_array(state["shots"], True)


    