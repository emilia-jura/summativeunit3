'''
This is a code by Emilia Juraszek
This game is inspired by the arcade game 'Dig Dug' and follows
the same ideas but with a different execution. In this
version, the main charcter is called Baxter and the context is that
he has stolen gold from the king, and is trying to run away
but the king has let out the 'Burrow Beasts'. The aim of the game
is to shoot all the Burrow Beasts without running out of gold.
'''
import pygame
import sys
from settings import *
from level import Level
from guizero import App, PushButton, Box, Text, Window, Picture


app = App(title="BURROW BLAST: Gold Heist", bg="#B5D6B2", width=1200, height=704)

print(screen_width)
print(screen_height)

play = True
score = 0

# main game loop
def game():
    global play, score
    app.hide()
    play = True
    # pygame setup

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    level = Level(level_map, screen)

    while play:
        pygame.init()
        # if someone clicks the x to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # if player dies or kills all enemies
        if level.end:
            score = level.hs
            play = False
            gameover()

        if play:
            # background color of window
            screen.fill("black")
            level.run()

            pygame.display.update()
            clock.tick(fps)
        else:
            pass

        if level.xlife != 100:
            level.xlife = 100
        else:
            pass


def gameover():
    global play_button, score
    pygame.quit()
    app.show()
    play_button.text = "PLAY AGAIN"
    # shows the players final score
    notif = Window(app, width=600, height=352, title="Gameover")
    notif.bg = "#B5D6B2"
    note = Text(notif, text="Gameover")
    note.text_color = "#5A464C"
    note.text_size = 34
    note.font = "freesansbold.ttf"
    msg = Text(notif, text="Your score: " + str(score) + " points!")
    msg.text_color = "#5A464C"
    msg.text_size = 24
    msg.font = "freesansbold.ttf"

# guizero layout
block1 = Box(app, height=352, width="fill", align="top")

block2 = Box(app, height=352, width="fill", align="top")

block3 = Box(block2, width="fill", height=70, align="bottom")

block4 = Box(block2, width=450, height="fill", align="left")


block5 = Box(block2, width=300, height="fill", align="left")


block6 = Box(block5, width=300, height=80)

play_button = PushButton(block6, text="PLAY", width="fill", height="fill", command=game)
play_button.text_size = 24
play_button.text_color = "#5A464C"
play_button.font = "freesansbold.ttf"

block7 = Box(block5, width="fill", height=15, align="top")

block8 = Box(block5, width="fill", height=80, align="top")

story_button = PushButton(block8, text="STORYLINE", width="fill", height=80)
story_button.text_size = 24
story_button.text_color = "#5A464C"
story_button.font = "freesansbold.ttf"

block9 = Box(block5, width="fill", height=15, align="top")

block10 = Box(block5, width="fill", height=80, align="top")

setting_button = PushButton(block10, text="SETTINGS", width="fill", height="fill")
setting_button.text_size = 24
setting_button.text_color = "#5A464C"
setting_button.font = "freesansbold.ttf"

block11 = Box(block1, width="fill", height=70, align="top")

title = Text(block1, text="BURROW BLAST", color="#5A464C", font="freesansbold.ttf", size=64, align="top")

block12 = Box(block1, width="fill", height=50, align="top")

subtitle = Text(block1, text="Gold Heist Version!", color="#5A464C", font="freesansbold.ttf", size=36, align="top")

character = Picture(block4, image="graphics/player/character0.png", align="left")

block13 = Box(block2, width=450, height="fill", align="right")

beast = Picture(block13, image="graphics/enemy/enemy0.png", align="right")

app.display()
