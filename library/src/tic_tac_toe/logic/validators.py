from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import Grid

import re


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")