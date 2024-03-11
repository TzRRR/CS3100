from gameplayer import *
from gameboard import *

boardsize = int(input())
gb = GameBoard(boardsize)

trench = playgame_dc(gb, 0, gb.size-1)
print(gb)
print(trench)
gb.final_answer(trench)
