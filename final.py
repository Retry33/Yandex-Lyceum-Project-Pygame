import pygame
from settings import WINDOW_SIZE, FPS, BLACK
from menu import FinalMenu
from map import matrix_map

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

final_menu = FinalMenu(screen)


def show_final_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(BLACK)
        final_menu.draw()
        pygame.display.flip()
        clock.tick(FPS)


# Используется для переключения на финальный экран
def check_final_position(player):
    player_tile_x = int(player.x // 100)
    player_tile_y = int(player.y // 100)

    if (player_tile_x, player_tile_y) == (47, 23):
        show_final_menu()
