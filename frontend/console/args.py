from tic_tac_toe.game.players import RandomComputerPlayer

from .players import ConsolePlayer

PLAYER_CLASSES = {
    "human": ConsolePlayer,
    "random": RandomComputerPlayer,
}
