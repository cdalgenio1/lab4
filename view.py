from common_types import Player
from collections.abc import Sequence

class ConnectTacToeView:
    def __init__(self):
        self.taken = [(-1,1)]

    def show_player(self, player: Player):
        if player == Player.P1:
            print("It is currently Player 1's turn")
        elif player == Player.P2:
            print("It is currently Player 2's turn")
        else:
            pass 
        print()

    def show_grid(self, grid: Sequence[Sequence[str]]):
        for row in grid:
            print("".join(row))
        print()

    def ask_for_coords(self) -> Sequence[int] | None :
        i = -1
        j = -1
        while (i,j) not in self.taken:
            while not 0 <= i < 6:
                try:
                    i = int(input(f"Choose a row    [0-6]: "))
                except KeyboardInterrupt:
                    exit()
                except:
                    ...

            while not 0 <= j < 7:
                try:
                    j = int(input(f"Choose a column [0-7]: "))
                except KeyboardInterrupt:
                    exit()
                except:
                    ...

            print()
            return [i, j]


    def show_winner(self, winner: Player | None, i: int, j: int):
        if winner == Player.P1:
            print("Congratulations, Player 1!, You have officially won!")
        elif winner == Player.P2:
            print("Congratulations, Player 2!, You have officially won!")
        elif not winner:
            print("Looks like we have a draw here...")
        else:
            pass 
        print()
