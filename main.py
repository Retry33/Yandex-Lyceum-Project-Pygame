import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing
from menu import MainMenu

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

menu = MainMenu(screen)

current_screen = "menu"

while True:
    if current_screen == "menu":
        menu.draw()
        action = menu.handle_events()
        if action == "play":
            current_screen = "game"
    elif current_screen == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = "menu"
        player.movement()
        screen.fill(BLACK)

        drawing.background(player.angle)
        drawing.world(player.pos, player.angle)
        drawing.fps(clock)

        pygame.display.flip()
        clock.tick(FPS)
