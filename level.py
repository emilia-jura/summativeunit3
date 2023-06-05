import pygame
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
import random

text = ""
life = 100
font = ()

text1 = ""
score = 0


class Level:
    global score, life
    end = False
    hs = score
    xlife = life

    def __init__(self, level_data, surface):
        global text, life, font, text1, score
        # any kind of objects we add to the game we want to keep in a group
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)
        life = self.player.sprite.life
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(" Gold Left: " + str(life), True, "#5A464C", "#FFFACC")
        text1 = font.render(" Score: " + str(score) + " ", True, "#5A464C", "#FFFACC")

        pygame.mixer.music.load("sounds/music_zapsplat_game_music_action_breakbeat_fast_electronic_busy_arpeggios_017.mp3")
        pygame.mixer.music.play(-1)

    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                # where in the layout the player 'spawns'
                elif cell == "p":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                    print(x/tile_size, y/tile_size)

        for i in range(5):
            enemy = Enemy((random.randint(300, screen_width), random.randint(0, screen_height)))
            self.enemies.add(enemy)


    def run(self):
        global life, text, font, text1, score
        self.tiles.draw(self.display_surface)
        self.player.update(self.tiles, self.enemies)
        # add this back for them to move randomly
        self.enemies.update()
        self.player.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        self.enemies.draw(self.display_surface)

        collide = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)

        self.display_surface.blit(text, (0, 0))

        score = self.player.sprite.score
        text1 = font.render(" Score: " + str(score) + " ", True, "#5A464C", "#FFFACC")
        self.display_surface.blit(text1, (550, 0))

        if len(collide) > 0:
            self.player.sprite.removelife()
            life = self.player.sprite.life
            text = font.render(" Gold Left: " + str(life), True, "#5A464C", "#FFFACC")
            self.display_surface.blit(text, (0, 0))
        if self.player.sprite.life == 0:
            self.gameover1()
        if len(self.enemies) == 0:
            self.gameover1()

    def gameover1(self):
        self.end = True
        self.hs = score
        self.xlife = life
