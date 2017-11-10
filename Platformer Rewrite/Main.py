#game version
VERSION = "A_0.20"

#import stuff
import pygame
from Settings import *
from Player import *
from MapObjects import *
from PIL import Image
import math

#Init pygame/mixer
pygame.init()
pygame.mixer.init()

#Create Window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer:" + VERSION)
clock = pygame.time.Clock()

#create sprite groups to store sprites
allSprites = pygame.sprite.Group()
plats = pygame.sprite.Group()

#init player object
sprPlayer = Player()

#build blocks on screen
platforms =[]

#horizontal blocks
for i in range(0,20):
    platforms.append(Block(i*20,460))
    plats.add(platforms[-1])
    allSprites.add(platforms[-1])

#vertical blocks
for i in range(0,20):
    platforms.append(Block(60, 100+(i*20)))
    plats.add(platforms[-1])
    allSprites.add(platforms[-1])

#add player sprite last
allSprites.add(sprPlayer)


# Game loop
def gameLoop():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in CONTROLS:
                    #send player control to player object
                    sprPlayer.control(CONTROLS[event.key], 1)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key in CONTROLS:
                    sprPlayer.control(CONTROLS[event.key], -1)

        allSprites.update(plats)

        SCREEN.fill(GREY)
        allSprites.draw(SCREEN)

        clock.tick(FPS)
        pygame.display.flip()


gameLoop()
pygame.quit()
exit()
