import pygame.sprite

from settings import *
from random import choice
from timer import Timer

class Tooth(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, collision_sprites):
        super().__init__(groups)
        self.frames, self.frame_index = frames, 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(topleft = pos)
        self.z = Z_LAYERS['main']

        self.direction = choice((-1,1))
        self.collision_rects = [sprite.rect for sprite in collision_sprites]
        self.speed = 200


    def update(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]
        if self.direction < 0:
            self.image = pygame.transform.flip(self.image, True, False) if self.direction < 0 else self.image

        self.rect.x += self.direction * self.speed * dt

        # reverse direction

        floor_rect_right = pygame.FRect(self.rect.bottomright, (1,1))
        floor_rect_left = pygame.FRect(self.rect.bottomleft, (-1, 1))

        if floor_rect_right.collidelist(self.collision_rects) < 0 and self.direction > 0 or\
        floor_rect_left.collidelist(self.collision_rects) < 0 and self.direction < 0:
            self.direction *= -1

class Shell(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        