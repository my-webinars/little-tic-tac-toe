from dataclasses import dataclass

from tic_tac_toe.game.players import Player
from tic_tac_toe.game.renderers import Renderer

@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    renderer: Renderer