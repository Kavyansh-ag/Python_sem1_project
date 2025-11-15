EMPTY = 'e' #Means cell is empty
WHITE = 'w' #Means cell is filled with white
BLACK = 'b' #Means cell is filled with black 
class Board:

    def __init__(self):
        self.grid = [['e' for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = 'w'
        self.grid[4][4] = 'w'
        self.grid[3][4] = 'b'
        self.grid[4][3] = 'b'

    def print_board(self):
        for row in self.grid:
            print(*row)
        
    def get_score(self):
        white_count = 0
        black_count = 0
        for row in self.grid:
            for element in row:
                if element == 'w': white_count += 1
                if element == 'b' : black_count += 1
        return white_count, black_count
    
    def is_full(self):
        for row in self.grid:
            for element in row:
                if element == 'e': return False
        return True

b = Board()
b.print_board()
print(b.get_score())
print(b.is_full())