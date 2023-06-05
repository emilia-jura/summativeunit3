import pygame
from settings import *
from tile import Tile


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, direction):
        super().__init__()
        # x,y width height
        self.image = pygame.Surface((30, 10))
        self.image.fill("red")
        # position of the rectangle
        self.rect = self.image.get_rect(topleft=pos)
        # if the player is not moving
        self.speed = 10
        # 1 if going to the right, -1 if going ot the left
        # vector 2 is just an x and y coordinate
        # direction is given from the player
        # y is 0 because the bullet isn't going to be changing in height
        self.direction = pygame.math.Vector2(direction * self.speed, 0)

    def horizontal_movement_collision1(self, tiles):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                    self.kill()
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left
                    self.kill()

    def update(self, tiles):
        self.horizontal_movement_collision1(tiles)
        self.rect.x += self.direction.x
        # making the bullet disappear if it goes outside the screen
        if self.rect.x > screen_width or self.rect.x < 0:
            self.kill()
