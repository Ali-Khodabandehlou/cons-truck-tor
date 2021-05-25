import pygame

from . import config


def change_screen_color(screen):
    screen.fill(config.colors['BLACK'])
    pygame.display.update()


# load new map for level
def new_map(screen, grid, level, x, y):
    level_map = grid.Grid(screen, level)
    level_map.drawBoard(x, y)
    return level_map


def info_bar(screen, level, moves, construct=None):
    border_weight = config.info_marg
    rect_start_x = config.margins['left'] + border_weight
    rect_start_y = config.margins['top'] + border_weight
    rect_x = config.info_dim[1] - config.margins['left'] - 2 * border_weight
    rect_y = config.info_dim[0] - 2 * border_weight
    pygame.draw.rect(screen, config.colors['GRAY'],
                     (rect_start_x, rect_start_y, rect_x, rect_y))
    pygame.draw.rect(screen, config.colors['DARK_GRAY'],
                     (rect_start_x, rect_start_y, rect_x, rect_y), 2 * border_weight)
    show_welcome(screen, level)
    show_info(screen, level, moves)
    show_controls(screen)
    if level != 0:
        show_construction(screen, construct=construct if construct else config.levels[str(level)]['construct'])


def show_welcome(screen, level):
    font1 = pygame.font.Font(config.files['font_prstart'], 15)
    text1 = font1.render('Welcome to', True, config.colors["BLUE"])
    text1_rect = text1.get_rect()
    rect_x1 = config.info_welcome[0]
    rect_y1 = config.info_welcome[1]
    text1_rect.center = (rect_x1, rect_y1)
    if level == 0:
        screen.blit(text1, text1_rect)
    font2 = pygame.font.Font(config.files['font_prstart'], 20)
    game_name = ['cons', '-TRUCK-', 'tor']
    for i in range(3):
        text2 = font2.render(game_name[i], True, config.colors["BLUE"])
        text2_rect = text2.get_rect()
        rect_x2 = config.info_welcome[0]
        rect_y2 = config.info_welcome[1] + (i + 1) * 20 + 10
        text2_rect.center = (rect_x2, rect_y2)
        screen.blit(text2, text2_rect)


def show_info(screen, level, moves):
    font1 = pygame.font.Font(config.files['font_prstart'], 15)
    level_txt = "Level: " + str(level)
    text1 = font1.render(level_txt, True, config.colors["RED"])
    text1_rect = text1.get_rect()
    rect_x1 = config.info_level[0]
    rect_y1 = config.info_level[1]
    text1_rect.center = (rect_x1, rect_y1)
    screen.blit(text1, text1_rect)

    font2 = pygame.font.Font(config.files['font_prstart'], 15)
    moves_txt = "moves: " + str(moves)
    text2 = font2.render(moves_txt, True, config.colors["RED"])
    text2_rect = text2.get_rect()
    rect_x2 = config.info_level[0]
    rect_y2 = config.info_level[1] + 50
    text2_rect.center = (rect_x2, rect_y2)
    screen.blit(text2, text2_rect)


def show_controls(screen):
    controls = [
        'Up:         W',
        'Down:       S',
        'Left:       A',
        'Right:      D',
        '',
        'Pickup:     O',
        'Disembark:  P',
        'Undo:       Z',
        'Quit:       Q',
    ]

    font = pygame.font.Font(config.files['font_prstart'], 15)
    text = font.render('Controls', True, config.colors["RED"])
    text_rect = text.get_rect()
    rect_x = config.info_controls[0]
    rect_y = config.info_controls[1]
    text_rect.center = (rect_x, rect_y)
    screen.blit(text, text_rect)

    for i in range(len(controls)):
        font = pygame.font.Font(config.files['font_prstart'], 10)
        text = font.render(controls[i].center(13, ' '), True, config.colors["RED"])
        text_rect = text.get_rect()
        rect_x = config.info_controls[0]
        rect_y = config.info_controls[1] + i * 25 + 30
        text_rect.center = (rect_x, rect_y)
        screen.blit(text, text_rect)


def show_construction(screen, construct):
    construction = [
        'Construction',
        'completed:{:.2f}'.format(construct),
    ]
    for i in range(len(construction)):
        font = pygame.font.Font(config.files['font_prstart'], 12)
        text = font.render(construction[i].ljust(13, ' '), True, config.colors["DARK-GREEN"])
        text_rect = text.get_rect()
        rect_x = config.info_construct[0]
        rect_y = config.info_construct[1] + i * 20
        text_rect.center = (rect_x, rect_y)
        screen.blit(text, text_rect)
