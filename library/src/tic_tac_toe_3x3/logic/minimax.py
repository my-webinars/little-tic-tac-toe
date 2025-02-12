"""The module includes tools for implementing the minimax algorithm
for finding the optimal move for the game of tic-tac-toe.
"""

from functools import partial

from tic_tac_toe_3x3.logic.models import GameState, Mark, Move


def find_best_move(game_state: GameState) -> Move | None:
    """Returns the best move (Move) for the current game state."""
    maximizer: Mark = game_state.current_mark
    bound_minimax = partial(minimax, maximizer=maximizer)
    return max(game_state.possible_moves, key=bound_minimax)


def minimax(
        move: Move, maximizer: Mark, choose_highest_score: bool = False
) -> int:
    """For the selected move (move: Move) from the point of view of
    the active player (maximizer: Mark), it recursively builds a weighted
    graph (for evaluation it uses the GameState.evaluate_score method)
    and evaluates each step.
    """
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    return (max if choose_highest_score else min)(
        minimax(next_move, maximizer, not choose_highest_score)
        for next_move in move.after_state.possible_moves
    )
