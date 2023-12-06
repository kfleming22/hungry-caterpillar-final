import pygame
from parameters import *
import random
from poison import *
import time


# makes static background for the whole game
def draw_background(surf,score = 0):
    # convert images for background
    blue = pygame.image.load("assests/sprites/water.png").convert()
    dirt = pygame.image.load("assests/sprites/dirt.png").convert()
    grass = pygame.image.load("assests/sprites/grass.png").convert()
    caterpillar = pygame.image.load("assests/sprites/caterpillar.png").convert()
    watermelon = pygame.image.load("assests/sprites/watermelon.png").convert()
    poison = pygame.image.load("assests/sprites/poison.png").convert()
    butterfly = pygame.image.load("assests/sprites/butterfly.png").convert()

    #transparent black background
    grass.set_colorkey((0,0,0))
    caterpillar.set_colorkey((0,0,0))
    watermelon.set_colorkey((0,0,0))
    poison.set_colorkey((0,0,0))
    butterfly.set_colorkey((0,0,0))


    # puts correct background pieces in the right places
    for x in range(0, SCREEN_WIDTH, blue.get_width()):
        for y in range(0, SCREEN_HEIGHT, blue.get_height()):
            surf.blit(blue, (x,y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT-(2*dirt.get_height()), SCREEN_HEIGHT, dirt.get_height()):
            surf.blit(dirt, (x,y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT-grass.get_height()-(2*dirt.get_height()), SCREEN_HEIGHT-(2*dirt.get_height()), dirt.get_height()):
            surf.blit(grass, (x,y))
    if score > 0: # makes score count appear on screen
        custom_font = pygame.font.Font('assests/fonts/Brainfish_Rush.ttf', 35)
        text = custom_font.render(f'Score: {score}', True, (0, 0, 0))
        surf.blit(surf, (0, 0))
        surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))


# makes a home screen with direction
def home(surf, scr):
    # title
    custom_font = pygame.font.Font('assests/fonts/Brainfish_Rush.ttf', 105)
    text = custom_font.render('Hungry Caterpillar', True, (0, 0, 0))
    scr.blit(surf, (0, 0))
    scr.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT/4))

    # directions
    custom_font2 = pygame.font.Font("assests/fonts/Brainfish_Rush.ttf", 25)
    text2 = custom_font2.render("-eat ten watermelons to win", True, (0, 0, 0))
    scr.blit(text2, (SCREEN_WIDTH / 2 - text2.get_width() / 2, SCREEN_HEIGHT / 2-text2.get_height()))

    # directions
    custom_font3 = pygame.font.Font("assests/fonts/Brainfish_Rush.ttf", 25)
    text3 = custom_font3.render("-but don't eat poison or you die! (poison falls faster the longer you play)", True, (0, 0, 0))
    scr.blit(text3, (SCREEN_WIDTH / 2 - text3.get_width() / 2, SCREEN_HEIGHT / 2))

    # directions
    custom_font4 = pygame.font.Font("assests/fonts/Brainfish_Rush.ttf", 25)
    text4 = custom_font4.render("-use left and right arrow keys to move", True, (0, 0, 0))
    scr.blit(text4, (SCREEN_WIDTH / 2 - text4.get_width() / 2, SCREEN_HEIGHT / 2+text3.get_height()))



    # update display
    pygame.display.flip()
    print('TITLE SCREEN!!!!')
    time.sleep(5) # pauses and gives player time to read instructions


# if you die this screen appears
def game_over(surf):
    # convert images
    blue = pygame.image.load("assests/sprites/water.png").convert()
    dirt = pygame.image.load("assests/sprites/dirt.png").convert()
    grass = pygame.image.load("assests/sprites/grass.png").convert()
    caterpillar = pygame.image.load("assests/sprites/caterpillar.png").convert()
    watermelon = pygame.image.load("assests/sprites/watermelon.png").convert()
    poison = pygame.image.load("assests/sprites/poison.png").convert()
    butterfly = pygame.image.load("assests/sprites/butterfly.png").convert()

    # transparent black background
    grass.set_colorkey((0, 0, 0))
    caterpillar.set_colorkey((0, 0, 0))
    watermelon.set_colorkey((0, 0, 0))
    poison.set_colorkey((0, 0, 0))
    butterfly.set_colorkey((0, 0, 0))

    # fill the screen
    for x in range(0, SCREEN_WIDTH, blue.get_width()):
        for y in range(0, SCREEN_HEIGHT, blue.get_height()):
            surf.blit(blue, (x, y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT - (2 * dirt.get_height()), SCREEN_HEIGHT, dirt.get_height()):
            surf.blit(dirt, (x, y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT - grass.get_height() - (2 * dirt.get_height()),
                       SCREEN_HEIGHT - (2 * dirt.get_height()), dirt.get_height()):
            surf.blit(grass, (x, y))

    # draw the text
    custom_font = pygame.font.Font("assests/fonts/Black_Crayon.ttf", 125)
    text = custom_font.render("GAME OVER", True, (0, 0, 0))
    surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT/2 - text.get_height()))


# if you get ten watermelons before dying, this screen appears
def butterfly(surf):
    # convert images
    blue = pygame.image.load("assests/sprites/water.png").convert()
    dirt = pygame.image.load("assests/sprites/dirt.png").convert()
    grass = pygame.image.load("assests/sprites/grass.png").convert()
    caterpillar = pygame.image.load("assests/sprites/caterpillar.png").convert()
    watermelon = pygame.image.load("assests/sprites/watermelon.png").convert()
    poison = pygame.image.load("assests/sprites/poison.png").convert()
    butterfly = pygame.image.load("assests/sprites/large_butterfly.png").convert()

    # transparent black background
    grass.set_colorkey((0, 0, 0))
    caterpillar.set_colorkey((0, 0, 0))
    watermelon.set_colorkey((0, 0, 0))
    poison.set_colorkey((0, 0, 0))
    butterfly.set_colorkey((0, 0, 0))

    # fill the screen
    for x in range(0, SCREEN_WIDTH, blue.get_width()):
        for y in range(0, SCREEN_HEIGHT, blue.get_height()):
            surf.blit(blue, (x, y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT - (2 * dirt.get_height()), SCREEN_HEIGHT, dirt.get_height()):
            surf.blit(dirt, (x, y))
    for x in range(0, SCREEN_WIDTH, dirt.get_width()):
        for y in range(SCREEN_HEIGHT - grass.get_height() - (2 * dirt.get_height()),
                       SCREEN_HEIGHT - (2 * dirt.get_height()), dirt.get_height()):
            surf.blit(grass, (x, y))

    # draw the text
    custom_font = pygame.font.Font("assests/fonts/Brainfish_Rush.ttf", 75)
    text = custom_font.render("You Turned Into A Butterfly!!", True, (0, 0, 0))
    surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

    surf.blit(butterfly, (SCREEN_WIDTH / 2-butterfly.get_width()/2, SCREEN_HEIGHT/2-butterfly.get_height()/2))