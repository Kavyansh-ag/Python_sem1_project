E = 0
B = 1   #player 1(starts first) 
W = 2   #player 2

## MOCK DATA - Static Starting Board for Logic Testing
# (0=Empty, 1=Black, 2=White)
desk = [
    [E, E, E, E, E, E, E, E],
    [E, E, E, E, E, E, E, E],
    [E, E, E, E, E, E, E, E],
    [E, E, E, W, B, E, E, E],
    [E, E, E, B, W, E, E, E],
    [E, E, E, E, E, E, E, E],
    [E, E, E, E, E, E, E, E],
    [E, E, E, E, E, E, E, E]
]

DIRECTIONS = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right
    (-1, -1), # Up-Left
    (1, -1),  # Down-Left
    (-1, 1)   # Up-Right
]

def is_on_board(r, c):
    if(0<= r <= 7) and (0<= c <= 7):
        return True
    else:
        return False
    
    
for i in desk:
    print(*i)


def check_direc(desk, r, c, player, dr, dc): #board --> state of board
                                              #r, c -->  co-ord of proposed new move
                                              #player --> current player
                                              #dr, dc --> DIRECn vector
    pieces_to_flip = []
    curr_r = r + dr
    curr_c = c + dc
    while (is_on_board(curr_r, curr_c) is True):
        if desk[curr_r][curr_c] == 0:
            return []
        if desk[curr_r][curr_c] == player:
            return pieces_to_flip
        elif desk[curr_r][curr_c] != player and desk[curr_r][curr_c] != 0:
            pieces_to_flip.append(tuple(curr_r, curr_c))

    return []

def get_flips(desk, r, c, player):
    if desk[r][c] != 0:
        return []
    all_flips = []

    for i, j in  DIRECTIONS:
        check_direc(desk, i, j, player, dr, dc )


