import abc

from tic_tac_toe_3x3.logic.models import GameState


class Renderer(metaclass=abc.ABCMeta):
    """Abstract class for creating specific renderers - that match the chosen usage.
    The renderer is responsible for displaying the game state.
    """
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""