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

controller = Game()
