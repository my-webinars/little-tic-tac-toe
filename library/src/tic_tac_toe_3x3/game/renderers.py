import abc

from tic_tac_toe_3x3.logic.models import GameState


class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""