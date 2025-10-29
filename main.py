from submarines.game import *
from submarines.io import *

def play(size: int = 6, n_ships: int = 6, max_shots: int = 20, *, one_based: bool = True):
        game = init_game(size, n_ships, max_shots )
        print(game)
        while not is_won(game) and not is_lost(game):
              cordinate_x, cordinate_y = one_shoot(game)
              print(f"cordinate_x, {cordinate_x}")
              print(f"cordinate_y, {cordinate_y} ")
              round = shoot(game, cordinate_x, cordinate_y)
              print(round)
        print_end(is_won(game))
        
if __name__ == "__main__": 
    play()