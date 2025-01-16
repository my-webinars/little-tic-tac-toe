import abc
import time

from tic_tac_toe_3x3.logic.exceptions import InvalidMove
from tic_tac_toe_3x3.logic.minimax import find_best_move
from tic_tac_toe_3x3.logic.models import GameState, Mark, Move


class Player(metaclass=abc.ABCMeta):
    """An abstract class for creating players that defines an interface
    for creating specific players.
    """
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        """Checks the possibility of the proposed move (from the point of view of
        the players' order) and provides a reaction to the next move: if it is
        possible - returns a new state, if further moves are impossible - generates
        an exception with an appropriate message.
        """
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other player's turn")

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """The abstract method is mandatory for implementation in specific
        player classes: it must return the move chosen by the player from among
        the permissible ones or None if further moves are impossible.
        """


class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    """Extends the abstract Player class for a computer player.
    Adds a delay when generating the result.
    """
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the computer's move in the given game state."""


class RandomComputerPlayer(ComputerPlayer):
    """A computer player who chooses a random move from among the possible ones."""
    def get_computer_move(self, game_state: GameState) -> Move | None:
        return game_state.make_random_move()


class MinimaxComputerPlayer(ComputerPlayer):
    """A computer player who uses the minimax algorithm to find the best move."""
    def get_computer_move(self, game_state: GameState) -> Move | None:
        if game_state.game_not_started:
            return game_state.make_random_move()
        return find_best_move(game_state)
