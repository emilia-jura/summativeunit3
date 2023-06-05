import pygame
from bullet import Bullet
from settings import *

life = 100


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        global life
        super().__init__()
        '''
        # size of player
        self.image = pygame.Surface((32, 64))
        # color of player
        self.image.fill("orange")
        '''
        self.image = pygame.image.load("graphics/player/ddcritbcharacter-1.png (4).png")
        self.rect = self.image.get_rect(topleft=pos)
        # x and y axis
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        # shooting
        self.bullets = pygame.sprite.Group()
        self.firing = False

        self.life = life

        self.score = 0

        self.last_direct = 0

        self.shoot = pygame.mixer.Sound("sounds/zapsplat_foley_rubber_tube_swish_whoosh_through_air_002_96127.mp3")

        self.hit = pygame.mixer.Sound("sounds/zapsplat_multimedia_beep_digital_soft_click_delayed_ascending_87487.mp3")

    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed
        keys = pygame.key.get_pressed()
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                    if keys[pygame.K_LSHIFT]:
                        tile.kill()
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left
                    if keys[pygame.K_LSHIFT]:
                        tile.kill()

    def vertical_movement_collision(self, tiles):
        self.rect.y += self.direction.y * self.speed
        keys = pygame.key.get_pressed()
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                    if keys[pygame.K_LSHIFT]:
                        tile.kill()
                elif self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    if keys[pygame.K_LSHIFT]:
                        tile.kill()

    def get_input(self, tiles):

        keys = pygame.key.get_pressed()
        # going left and right
        # player coordinate9s are (self.rect.x, self.rect.y)
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.last_direct = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.last_direct = -1
        # going up and down
        elif keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        # not moving
        else:
            self.direction.x = 0
            self.direction.y = 0
        if keys[pygame.K_SPACE] and not self.firing:
            self.fire()
            self.firing = True
        elif not keys[pygame.K_SPACE] and self.firing:
            self.firing = False

    def fire(self):
        # we need to send it x and y coordinates
        # center x means it fires from the center of the player
        bullet = Bullet((self.rect.centerx, self.rect.centery), self.last_direct)
        self.bullets.add(bullet)
        pygame.mixer.Sound.play(self.shoot)


    def draw_bullets(self, surface):
        self.bullets.draw(surface)

    def removelife(self):
        self.life -= 1

    def getlife(self):
        return self.life

    def editscore(self):
        pygame.mixer.Sound.play(self.hit)
        if self.life < 50:
            self.score += 10
        else:
            self.score += 15

    def update(self, tiles, enemies):
        self.get_input(tiles)
        self.enemies = enemies
        collided2 = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if len(collided2) > 0:
            self.editscore()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
        self.bullets.update(tiles)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
