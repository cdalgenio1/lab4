# pyright: strict
from common_types import Player

class ConnectTacToeModel:
    def __init__(self):
        self._current_player:Player = Player.P1
        self.grid:list[list[str]] = [["."]*7 for _ in range(6)]
        self.tokens: list = ("1","2")
    @property
    def current_player(self)->Player:
        return self._current_player
    @property
    def winner(self) ->Player|None:
        for token in self.tokens:
            check = token*3
            for r in self.grid:
                to_check = "".join(r)
                if check in to_check:
                    return self._current_player
    @property
    def is_game_done(self)->bool:
        ...
    def choose_cell(self,row:int,col:int)->bool:
        ...
    @property
    def row_count(self) -> int:
        return 6
    @property
    def col_count(self)->int:
        return 7
    def get_owner(self,row:int,col:int)->Player|None:
        ...

print(ConnectTacToeModel().winner)