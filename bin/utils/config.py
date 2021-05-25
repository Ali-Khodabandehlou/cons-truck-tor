import json
import os

directory = 'bin/'
sub_dir = {
    'thumbnails': directory + 'thumb/',
    'maps': directory + 'maps/',
    'fonts': directory + 'fonts/',
}
files = {
    'logo': sub_dir['thumbnails'] + 'icon.ico',
    'wall': sub_dir['thumbnails'] + 'wall.png',
    'tile': sub_dir['thumbnails'] + 'groundtile.png',
    'box': sub_dir['thumbnails'] + 'box.png',
    'platform': sub_dir['thumbnails'] + 'platform.png',
    'construct_0': sub_dir['thumbnails'] + 'construct_0.png',
    'construct_1': sub_dir['thumbnails'] + 'construct_1.png',
    'construct_2': sub_dir['thumbnails'] + 'construct_2.png',
    'construct_3': sub_dir['thumbnails'] + 'construct_3.png',
    'player': sub_dir['thumbnails'] + 'player.png',
    'pl-pl': sub_dir['thumbnails'] + 'plwin.png',
    'cargo_wood': sub_dir['thumbnails'] + 'cargo_wood.png',
    'cargo_stone': sub_dir['thumbnails'] + 'cargo_stone.png',
    'wood': sub_dir['thumbnails'] + 'wood.png',
    'stone': sub_dir['thumbnails'] + 'stone.png',
    'maps': sub_dir['maps'] + 'levels.json',
    'font_times_italic': sub_dir['fonts'] + 'timesi.ttf',
    'font_prstart': sub_dir['fonts'] + 'prstartk.ttf',
}

levelMapFile = files['maps']
if os.path.exists(levelMapFile):
    with open(levelMapFile, 'r') as f:
        data = json.loads(f.read())

        margins = data['screen_margin']
        info_dim = data['info_dim']
        info_marg = data['info_marg']
        info_welcome = data['info_welcome']
        info_level = data['info_level']
        info_controls = data['info_controls']
        info_construct = data['info_construct']

        screen_x = data['screen_size_x']
        screen_y = data['screen_size_y']

        tile_size = data['tile_size']
        board_size = data['board_size']

        colors = {
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255),
            "CYAN": (0, 255, 255),
            "VIOLET": (255, 0, 255),
            "YELLOW": (255, 255, 0),
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GRAY": (190, 190, 190),
            "DARK_GRAY": (120, 120, 120),
            "DARK-GREEN": (50, 180, 50),
        }

        levels = data['levels']
else:
    print('Error: file (bin/maps/levels.json) does not exist.')
