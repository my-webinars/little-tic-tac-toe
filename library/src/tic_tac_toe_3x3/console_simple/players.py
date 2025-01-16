import re

from tic_tac_toe_3x3.game.players import Player
from tic_tac_toe_3x3.logic.exceptions import InvalidMove
from tic_tac_toe_3x3.logic.models import GameState, Move


class ConsolePlayer(Player):
    """Implementation of a player who uses the console to enter the next move.
    Extends the abstract class Player. Implements the abstract method get_move()
    which implements interaction with the console to select the player's move.
    """
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None


def grid_to_index(grid: str) -> int:
    """Converts the grid coordinates to the index of the cell in the game grid."""
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))
