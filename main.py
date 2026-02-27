from model import ConnectTacToeModel
from view import ConnectTacToeView
from common_types import Player

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView):
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        while not model.is_game_done:
            #model.start_turn()
            view.show_player(model.current_player)
            if model.current_player == Player.P1:
                view.show_grid(model.grid)
                i, j = view.ask_for_coords() #input what it asls
                model.choose_cell(i, j)
            
            else:
                i, j = model.get_random_coords()
                model.choose_cell(i, j)

        view.show_winner(model.winner)


                
if __name__ == "__main__":
    row_count = 6
    col_count = 7
    view = ConnectTacToeView()
    model = ConnectTacToeModel()
    controller = ConnectTacToeController(model, view)
    controller.start()
