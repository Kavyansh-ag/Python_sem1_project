import board
import game_logic as logic
import file_manager   
from GUI import myGUI

class Game:
    def __init__(self):
        self.board = board.Board()
        self.gui =myGUI(self)

    def handle_move(self, row, col):
        print("Controller got:", row, col)

    def save(self):
        file_manager.save_game(self.board.grid, self.board.player)

    def load(self):
        board_state, current_player = file_manager.load_game()
        if board_state is not None:
            self.board.grid = board_state
            self.board.player = current_player

controller = Game()
