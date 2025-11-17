
'''We will recieve x,y,player,board. this file will only check wheter the move selcted by player is valid or not.'''

Directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
            #   N    N-E    E     S-E     S     S-W      W     N-W 

def is_on_board(r, c):
    if(0<= r <= 7) and (0<= c <= 7):
        return True
    return False

def switch_player(player):
    if player == 1: return 2
    else: return 1

def get_opponent(current_player):
    return switch_player(current_player)

def get_flips_in_direction(b,r,c,player,vector):
    pieces_to_flip = []
    opponent = get_opponent(player)
    curr_r = r + vector[0]
    curr_c = c + vector[1]
    if not is_on_board(curr_r, curr_c) or b[curr_r][curr_c] != opponent:
        return []
    while is_on_board(curr_r,curr_c):
        
        if b[curr_r][curr_c] == 0 : return []
        elif b[curr_r][curr_c] == player: return pieces_to_flip
        else: 
            pieces_to_flip.append([curr_r,curr_c])
            curr_r += vector[0]
            curr_c += vector[1]
    return []

def get_all_flips(b,r,c,player):
    all_flips = []
    if b[r][c] != 0: return []

    for vector in Directions:
        all_flips.extend(get_flips_in_direction(b,r,c,player,vector))
    return all_flips
# The return from this will be used to create next state board


def has_legal_moves(b,player):
    for r in range(8):
        for c in range(8):
            if b[r][c] == 0:
                if get_all_flips(b, r, c, player):
                    return True
    return False

def determine_next_player_id(b, last_player):
    opponent = get_opponent(last_player)

    if has_legal_moves(b, opponent):
        return opponent

    elif has_legal_moves(b, last_player):
        return last_player 
     

def next_state(b,r,c,player):
    board_cpy = [row[:] for row in b]
    all_flips = get_all_flips(b,r,c,player)
    if not all_flips:
        return (b, player) 
            
    board_cpy[r][c] = player

    for coordinate in all_flips:
        board_cpy[coordinate[0]][coordinate[1]] = player

    opponent = get_opponent(player)
    if has_legal_moves(board_cpy,opponent):
        next_player = opponent
    elif has_legal_moves(board_cpy, player):
        next_player = player 
    else:
        next_player = None

    return (board_cpy, next_player)