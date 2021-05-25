import sys
import pygame

from bin.utils import config, ui, handler
from bin.maps import grid

start_x, start_y = 0, 0
_isRunning = True
_level = 0
_moves = 0
basicFont = None

keys = {
    '119': 'UP',
    '115': 'DOWN',
    '97': 'LEFT',
    '100': 'RIGHT',
    '122': 'UNDO',
    '111': 'PICKUP',
    '112': 'DISEMBARK',
    '113': 'QUIT',
}


# engine function: sets up the screen and runs pygame
def engine():
    global start_x, start_y
    start_y = config.margins['left'] + config.info_dim[1]
    start_x = config.margins['top']

    pygame.display.set_caption('cons-truck-tor')
    logo_icon = pygame.image.load(config.files["logo"])
    pygame.display.set_icon(logo_icon)

    # run pygame engine
    pygame.init()
    screen_y = config.screen_y + start_y + config.margins['right']
    screen_x = config.screen_x + start_x + config.margins['bottom']
    screen = pygame.display.set_mode((screen_y, screen_x))

    return screen


# exit function
def app_exit():
    pygame.quit()
    sys.exit()


# to handle events
def event_handler(screen, level_map):
    global _isRunning, _level, _moves
    while _isRunning:
        if level_map.win_state:
            _level += 1
            _moves = 0
            ui.change_screen_color(screen)
            if _level >= len(config.levels):
                _isRunning = False
                break
            ui.info_bar(screen, _level, _moves)
            level_map = ui.new_map(screen, grid, _level, start_x, start_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _isRunning = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    _isRunning = False
                elif str(event.key) in keys.keys():
                    if keys[str(event.key)] == 'UNDO':
                        if len(level_map.moves) > 0:
                            level_map.undo_move()
                            level_map.move_id += 1
                    elif keys[str(event.key)] == 'QUIT':
                        _isRunning = False
                        break
                    else:
                        move_dir = keys[str(event.key)]
                        level_map = handler.move_player(level_map, move_dir)
                    level_map.calculateConstruct()
                    level_map.drawBoard(start_x, start_y)
                    _moves = level_map.move_id
                    ui.info_bar(screen, _level, _moves, construct=level_map.construct)
                    pygame.display.update()
        ui.info_bar(screen, _level, _moves, construct=level_map.construct)

        if not _isRunning:
            app_exit()


def main():
    global _isRunning, _level
    screen = engine()
    ui.change_screen_color(screen)
    level_map = ui.new_map(screen, grid, _level, start_x, start_y)
    ui.info_bar(screen, _level, _moves, construct=level_map.construct)

    # run the game
    pygame.display.update()
    event_handler(screen, level_map)


if __name__ == '__main__':
    main()
