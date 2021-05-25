directions = {
    'UP': [-1, 0],
    'DOWN': [1, 0],
    'LEFT': [0, -1],
    'RIGHT': [0, 1],
}

material = {
    's': 'stone',
    'w': 'wood',
}


def move_item(grid, old_pos_x, old_pos_y, new_pos_x, new_pos_y, item_type):
    grid.grid[old_pos_x][old_pos_y] = 0
    if item_type == '3':
        grid.player_pos = [new_pos_x, new_pos_y]
    grid.grid[new_pos_x][new_pos_y] = int(item_type)

    return grid


def move_player(grid, direction):
    if direction == 'PICKUP' or direction == 'DISEMBARK':
        grid.add_move()
        grid = change_cargo(grid, direction)
        return grid

    else:
        plyr_pos = grid.player_pos
        temp_dir = directions[direction]
        new_pos_x = plyr_pos[0] + temp_dir[0]
        new_pos_y = plyr_pos[1] + temp_dir[1]

        if grid.grid[new_pos_x][new_pos_y] == 0:
            grid.add_move()
            grid = move_item(grid, plyr_pos[0], plyr_pos[1], new_pos_x, new_pos_y, '3')
            grid.move_id += 1

        elif grid.grid[new_pos_x][new_pos_y] == 1:
            new_box_pos_x = new_pos_x + temp_dir[0]
            new_box_pos_y = new_pos_y + temp_dir[1]
            if grid.grid[new_box_pos_x][new_box_pos_y] == 0:
                grid.add_move()
                grid = move_item(grid, new_pos_x, new_pos_y, new_box_pos_x, new_box_pos_y, '1')
                grid = move_item(grid, plyr_pos[0], plyr_pos[1], new_pos_x, new_pos_y, '3')
                grid.move_id += 1

        elif grid.grid[new_pos_x][new_pos_y] == 4 and grid.construct == 1.0:
            grid.add_move()
            grid.win_state = True
            grid = move_item(grid, plyr_pos[0], plyr_pos[1], new_pos_x, new_pos_y, '3')
            grid.move_id += 1

        return grid


def change_cargo(grid, direction):
    plyr_pos = grid.player_pos
    mat = search_range(grid, plyr_pos)

    if mat == 'construct' and direction == 'DISEMBARK':
        if grid.cargo == '3w':
            if grid.construct_wood < grid.construct_wood_need:
                grid.construct_wood += 1
                grid.move_id += 1
        elif grid.cargo == '3s':
            if grid.construct_stone < grid.construct_stone_need:
                grid.construct_stone += 1
                grid.move_id += 1
        grid.cargo = '3'
    elif direction == 'DISEMBARK' and grid.cargo != '3':
        grid.move_id += 1
        grid.cargo = '3'
    elif direction == 'PICKUP' and grid.cargo == '3':
        if mat == 'wood':
            grid.cargo = '3w'
            grid.move_id += 1
        elif mat == 'stone':
            grid.cargo = '3s'
            grid.move_id += 1

    return grid


def search_range(grid, player_pos):
    for i in range(player_pos[0]-1, player_pos[0]+2):
        try:
            if str(grid.grid[i][player_pos[1]]) == '2':
                return 'construct'
            elif material[str(grid.grid[i][player_pos[1]])]:
                return material[grid.grid[i][player_pos[1]]]
        except:
            pass
    for i in range(player_pos[1]-1, player_pos[1]+2):
        try:
            if str(grid.grid[player_pos[0]][i]) == '2':
                return 'construct'
            elif material[str(grid.grid[player_pos[0]][i])]:
                return material[grid.grid[player_pos[0]][i]]
        except:
            pass
    return None
