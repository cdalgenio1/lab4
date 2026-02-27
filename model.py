# pyright: strict
from common_types import Player

class ConnectTacToeModel:
    def __init__(self):
        self._current_player:int = 0
        self.grid:list[list[str]] = [["."]*7 for _ in range(6)]
        self.tokens: list = ("A","B")
    @property
    def current_player(self)->Player:
        if self._current_player == 0:
            return Player.P1
        else:
            return Player.P2
    @property
    def winner(self) ->Player|None:
        for token in self.tokens:
            check = token*3
            for r in self.grid:
                to_check_row = "".join(r)
                if check in to_check_row:
                    return self._current_player
            check_columns = ["".join([self.grid[_r][c] for _r in range(6)]) for c in range(7)]
            if check in check_columns:
                return self._current_player
        return None
    @property
    def is_game_done(self)->bool:
        if self.winner:
            return True
        return False
    def choose_cell(self,row:int,col:int)->bool:
        if not is_game_done:
            if self.grid[row][col] == ".":
                self.grid[row][col] = self.tokens[self._current_player]
                self._current_player = (self._current_player+1)//2
                return True
            return False
    @property
    def row_count(self) -> int:
        return 6
    @property
    def col_count(self)->int:
        return 7
    def get_owner(self,row:int,col:int)->Player|None:
        cell = self.grid[row][col]
        if cell == "A":
            return Player.P1
        elif cell == "B":
            return Player.P2
        else:
            return None

ConnectTacToeModel().winner