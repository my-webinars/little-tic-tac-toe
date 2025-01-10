from console.players import ConsolePlayer
from console.renderers import ConsoleRenderer
from tic_tac_toe_3x3.game.engine import TicTacToe
from tic_tac_toe_3x3.game.players import RandomComputerPlayer
from tic_tac_toe_3x3.logic.models import Mark

# player1 = RandomComputerPlayer(Mark("X"))
player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
