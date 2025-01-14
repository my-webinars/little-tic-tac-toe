import textwrap
from typing import Iterable

from tic_tac_toe_3x3.game.renderers import Renderer
from tic_tac_toe_3x3.logic.models import GameState


class ConsoleRenderer(Renderer):
    """Extends the abstract Renderer class to display the current
    game state in the console.
    """
    def render(self, game_state: GameState) -> None:
        clear_screen()
        if game_state.winner:
            print_blinking(game_state.grid.cells, game_state.winning_cells)
            print(f"{game_state.winner} wins!\N{PARTY POPPER}")
        else:
            print_solid(game_state.grid.cells)
            if game_state.tie:
                print("No one wins this time \N{neutral face}")


def clear_screen() -> None:
    """Clears the console screen."""
    print("\033c", end="")


def blink(text: str) -> str:
    """Returns the text with the blinking effect."""
    return f"\033[5m{text}\033[0m"


def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    """Prints the game grid with blinking cells with indexes in positions."""
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)


def print_solid(cells: Iterable[str]) -> None:
    """Prints a game grid with cells filled according to the cells state."""
    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}
            """
        ).format(*cells)
    )

if __name__ == "__main__":
    cells = " X0 X0X0    "
    print_solid(cells)
