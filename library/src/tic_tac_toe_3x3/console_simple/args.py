"""Implementation of a command line interface for launching the game with a
simple console rendering option.
"""

import argparse
from typing import NamedTuple

from tic_tac_toe_3x3.game.players import (MinimaxComputerPlayer, Player,
                                          RandomComputerPlayer)
from tic_tac_toe_3x3.logic.models import Mark

from .players import ConsolePlayer

PLAYER_CLASSES = {
    "human": ConsolePlayer,
    "random": RandomComputerPlayer,
    "minimax": MinimaxComputerPlayer,
}


class Args(NamedTuple):
    player1: Player
    player2: Player
    starting_mark: Mark


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="player_x",
        choices=PLAYER_CLASSES.keys(),
        default="human",
    )
    parser.add_argument(
        "-0",
        dest="player_o",
        choices=PLAYER_CLASSES.keys(),
        default="minimax",
    )
    parser.add_argument(
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES[args.player_x](Mark("X"))
    player2 = PLAYER_CLASSES[args.player_o](Mark("0"))

    if args.starting_mark == "0":
        player1, player2 = player2, player1

    return Args(player1, player2, args.starting_mark)
