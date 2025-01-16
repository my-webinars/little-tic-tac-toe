from tic_tac_toe_3x3.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer


def main() -> None:
    """Implements a command line interface: parses parameters, creates a
    game instance, and runs the main game loop with the appropriate parameters.
    """
    player1, player2, starting_mark = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play(starting_mark)