### A file for storing some simple utilties that I have been using the hackerrank botclean problems



def find_tiles(board, tile_type):
    target_tiles = []
    for row_index, row in enumerate(board):
        for col_index, tile in enumerate(row):
            if tile == tile_type: target_tiles.append([row_index, col_index])
    return target_tiles

def find_closest_tile_from_tilelist(posr, posc, tiles):
    distances = []
    for tile in tiles:
        distance = abs(tile[0] - posr) + abs(tile[1] - posc)
        distances.append(distance)
    min_distance = min(distances)
    closest_tile = tiles[distances.index(min_distance)]
    return(closest_tile)

def next_move_for_target_tile(posr, posc, target_tile):
    if target_tile == [posr,posc]: 
        return('CLEAN')
    disp_row = target_tile[0]-posr
    disp_col = target_tile[1]-posc
    if abs(disp_row) >= abs(disp_col):
        if disp_row >0 :
            return('DOWN')
        elif disp_row < 0:
            return('UP')
    else:
        if disp_col >0 :
            return('RIGHT')
        elif disp_col < 0:
            return('LEFT')

def next_move(posr, posc, board):
    dirty_tiles = find_dirty_tiles(board)
    target_tile = find_closest_tile_from_tilelist(posr, posc, dirty_tiles)
    next_action = next_move_from_target_tile(posr, posc, target_tile)
    print(next_action)


    
