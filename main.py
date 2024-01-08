import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill(BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)