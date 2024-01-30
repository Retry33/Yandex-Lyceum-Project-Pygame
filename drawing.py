import pygame
from settings import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: pygame.image.load('img/wall1.jpg').convert(),
                         'S': pygame.image.load('img/MoonSky.png').convert()
                         }

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WINDOW_WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WINDOW_WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WINDOW_WIDTH, 0))
        pygame.draw.rect(self.screen, DARK_GRAY, (0, HALF_HEIGHT, WINDOW_WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, FPS_POS)
