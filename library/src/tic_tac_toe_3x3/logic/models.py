import enum
import random
import re
from dataclasses import dataclass
from functools import cached_property

from .exceptions import InvalidMove, UnknownGameScore
from .validators import validate_game_state, validate_grid

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)


class Mark(enum.StrEnum):
    """Acceptable player symbols."""
    CROSS = "X"
    NAUGHT = "0"

    @property
    def other(self) -> "Mark":
        """Returns the 'other' player character."""
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT


@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        """Checks whether the initiated instance complies with existing constraints."""
        validate_grid(self)

    @cached_property
    def x_count(self) -> int:
        """Returns the number of player 'X's marks on the grid."""
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        """Returns the number of player 'O's marks on the grid."""
        return self.cells.count("0")

    @cached_property
    def empty_count(self) -> int:
        """Returns the number of empty cells in the grid."""
        return self.cells.count(" ")


@dataclass(frozen=True)
class Move:
    """Describes a player's move.

    mark: player symbol
    cell_index: position on the grid
    before_state: state of the game before the player's move
    after_state: state of the game after the move
    """
    mark: Mark
    cell_index: int
    before_state: 'GameState'
    after_state: 'GameState'


@dataclass(frozen=True)
class GameState:
    """Describes the current state of the game.

    Based on the analysis of the current state of the grid and the player who made
    the first move, it determines one of the following game states:
    1. The game has not yet started.
    2. The game is still in progress.
    3. The game ended in a draw.
    4. The game ended with player X winning.
    5. The game ended with player O winning.
    """
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self):
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        """Returns the player who should make the next move."""
        return self.starting_mark if self.grid.x_count == self.grid.o_count else self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        """Returns True if no moves were made in the game, False otherwise."""
        return self.grid.cells == " " * 9

    @cached_property
    def tie(self) -> bool:
        """Returns True if the game ended in a tie, False otherwise."""
        return self.grid.empty_count == 0 and self.winner is None

    @cached_property
    def game_over(self) -> bool:
        """Returns True if the game is over, False otherwise."""
        return self.winner is not None or self.tie

    @cached_property
    def winner(self) -> Mark | str | None:
        """Returns the player (Mark or str) who won the game, or None if the game is not over for current GameState"""
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:

        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [i for i, c in enumerate(pattern) if c == "?"]
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        """Returns a list of possible moves (Move) for the current game state."""
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves

    def make_random_move(self) -> Move | None:
        """Returns a random move for current game state."""
        try:
            return random.choice(self.possible_moves)
        except IndexError:
            return None

    def make_move_to(self, index: int) -> Move:
        """Returns a move (Move) for the current game state with the specified index."""
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1:]
                ),
                self.starting_mark,
            ),
        )

    def evaluate_score(self, mark: Mark) -> int:
        """Returns the move score for weighting the minimax algorithm graph:
        -1 - if the move leads to a loss,
        0 - if it leads to a draw,
        1 - if it leads to a win.
        """
        if self.game_over:
            if self.tie:
                return 0
            if self.winner is mark:
                return 1
            else:
                return -1
        raise UnknownGameScore("Game is not over yet")
