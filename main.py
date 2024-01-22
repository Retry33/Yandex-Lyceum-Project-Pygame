import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing
from menu import MainMenu

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.mouse.set_visible(False)

sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
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
        walls = ray_casting(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        drawing.fps(clock)

        pygame.display.flip()
        clock.tick(FPS)
