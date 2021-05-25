import pygame
import copy

from ..utils import config


class Grid:
    types = {
        '-1': 'wall',
        '0': 'tile',
        '1': 'box',
        '20': 'construct_0',
        '21': 'construct_1',
        '22': 'construct_2',
        '23': 'construct_3',
        'win': 'pl-pl',
        '3': 'player',
        '3w': 'cargo_wood',
        '3s': 'cargo_stone',
        '4': 'platform',
        'w': 'wood',
        's': 'stone',
    }

    win_state = False
    moves = {}

    pygame.init()

    def __init__(self, screen, level):
        self.pygame_screen = screen
        level_data = config.levels[str(level)]
        self.grid = level_data['grid']
        self.player_pos = level_data['player']
        self.win_pos = level_data['platform']
        self.cargo = level_data['cargo']
        self.construct = level_data['construct']
        self.construct_wood = level_data['construct_wood']
        self.construct_wood_need = int(level_data['construct_wood_need'])
        self.construct_stone = int(level_data['construct_stone'])
        self.construct_stone_need = int(level_data['construct_stone_need'])
        self.move_id = 0
        self.moves.clear()

    @property
    def construct_type(self):
        _item_type = ''
        if self.construct == 0.0:
            _item_type = "20"
        elif self.construct < 0.66:
            _item_type = "21"
        elif self.construct < 1.0:
            _item_type = "22"
        else:
            _item_type = "23"
        return _item_type

    def calculateConstruct(self):
        total_material_need = self.construct_wood_need + self.construct_stone_need
        total_material = self.construct_wood + self.construct_stone
        self.construct = total_material / total_material_need

    def checkWin(self):
        if self.player_pos == self.win_pos:
            self.win_state = True

    def drawBoard(self, x, y):
        for i in range(config.board_size):
            for j in range(config.board_size):
                _item_type = self.grid[i][j]
                if _item_type == 3:
                    _item_type = self.cargo
                elif _item_type == 2:
                    _item_type = self.construct_type
                self.drawTile(x + i * config.tile_size, y + j * config.tile_size, config.tile_size, _item_type)
        pygame.display.update()

    def drawTile(self, ypos, xpos, size, item_type):
        self.checkWin()

        tile = pygame.Rect(xpos, ypos, size, size)
        if not self.win_state:
            tile_file = pygame.image.load(config.files[self.types[str(item_type)]])
        else:
            tile_file = pygame.image.load(config.files[self.types['win']])
        tile_image = pygame.transform.scale(tile_file, (config.tile_size, config.tile_size))
        self.pygame_screen.blit(tile_image, tile)

    def add_move(self):
        self.moves.update({str(self.move_id): [copy.deepcopy(self.grid),
                                               copy.deepcopy(self.player_pos),
                                               copy.deepcopy(self.cargo),
                                               copy.deepcopy(self.construct_wood),
                                               copy.deepcopy(self.construct_stone),
                                               ]})

    def undo_move(self):
        if len(self.moves) > 0:
            key = list(self.moves.keys())[-1]
            old_grid = self.moves[key]
            self.grid = copy.deepcopy(old_grid[0])
            self.player_pos = copy.deepcopy(old_grid[1])
            self.cargo = copy.deepcopy(old_grid[2])
            self.construct_wood = copy.deepcopy(old_grid[3])
            self.construct_stone = copy.deepcopy(old_grid[4])
            self.moves.popitem()
