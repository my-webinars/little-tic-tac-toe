import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState


class ConsoleRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        clear_screen()
        print_solid(game_state.grid.cells)


def clear_screen() -> None:
    print("\033c", end="")


def blink(text: str) -> str:
    return f"\033[5m{text}\033[0m"


def print_solid(cells: Iterable[str]) -> None:
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
    cells = " XO XOXO "
    print_solid(cells)
