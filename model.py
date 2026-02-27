# pyright: strict
from common_types import Player

class ConnectTacToeModel:
    def __init__(self):
        ...
    @property
    def current_player(self)->Player:
        ...
    @property
    def winner(self) ->Player|None:
        ...
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