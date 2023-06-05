import pygame
import random
from settings import *


class Enemy(pygame.sprite.Sprite):

    # a constructor that takes a position
    def __init__(self, pos):
        # below is done to make the sprite
        super().__init__()
        '''
        # a general image that is colored blue
        self.image = pygame.Surface((32, 32))
        self.image.fill("purple")
        '''
        self.image = pygame.image.load("graphics/enemy/ddcritbenemy-1.png (1).png")
        # collision rectangle around the image
        self.rect = self.image.get_rect(topleft=pos)

    # and update so that the enemy's x and y coordinates change randomly
    def update(self):
        # constantly changing location
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)
        # stops them from leaving the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
