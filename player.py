import math
from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = player_speed
        self.sensitivity = 0.004

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.angle %= DOUBLE_PI

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        current_speed = self.speed * 2 if shift_pressed else self.speed

        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            self.x += current_speed * cos_a
            self.y += current_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -current_speed * cos_a
            self.y += -current_speed * sin_a
        if keys[pygame.K_a]:
            self.x += current_speed * sin_a
            self.y += -current_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -current_speed * sin_a
            self.y += current_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity