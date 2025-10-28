def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None = None):
    return { 
  "size": int, 
  "ships": list[list[int]], 
  "shots": list[list[bool]], 
  "n_ships": int, 
  "max_shots": int, 
  "shots_used": int 
} 


def shoot(state: dict, x: int, y: int):
    return tuple[bool, str] 
 
def is_won(state: dict):
    return bool 

 
def is_lost(state: dict):
    return shots_used >= max_shots 
 
def shots_left(state: dict):
    return int 
 
def remaining_ships(state: dict): 
    return int