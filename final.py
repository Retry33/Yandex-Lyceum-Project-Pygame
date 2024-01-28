import time
import pygame
from datetime import datetime
from settings import WINDOW_SIZE, FPS, BLACK
from menu import FinalMenu
from map import matrix_map

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

final_menu = FinalMenu(screen)


def find_time_difference(time1, time2):
    format_str = '%H:%M:%S'
    datetime_time1 = datetime.strptime(time1, format_str)
    datetime_time2 = datetime.strptime(time2, format_str)
    time_difference = datetime_time2 - datetime_time1
    return time_difference.seconds


def show_final_menu(start, finish):
    score = find_time_difference(start, finish)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(BLACK)
        final_menu.draw(score)
        pygame.display.flip()
        clock.tick(FPS)


# Используется для переключения на финальный экран
def check_final_position(player, start):
    player_tile_x = int(player.x // 100)
    player_tile_y = int(player.y // 100)

    if (player_tile_x, player_tile_y) == (47, 23):
        finish = time.ctime(time.time()).split()[3]
        show_final_menu(start, finish)
