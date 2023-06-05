import pygame


class Tile(pygame.sprite.Sprite):
    # tile data, size color, etc
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("#FFEFBD")
        self.rect = self.image.get_rect(topleft=pos)
