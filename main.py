import pygame
import sys
from background import *
import time
from caterpillar import*
from poison import *
from food import *

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# import sound
hurt = pygame.mixer.Sound("assests/sounds/hurt.wav")
chomp = pygame.mixer.Sound("assests/sounds/eat.wav")
music = pygame.mixer.Sound("assests/sounds/Sakura-Girl-Daisy-chosic.com_.mp3")
# background music
pygame.mixer.Sound.play(music)


# clock object
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()

# draws background screen
draw_background(background)

# title screen
home(background, screen)


# create objects
poison = Poison(0, 0)
caterpillar = Caterpillar(0, SCREEN_HEIGHT-1.25*blue-caterpillar_height)
watermelon = Food(0,0)


# main while loop
food = 1
lives = 1
while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control caterpillar with keyboard
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                caterpillar.move_left()
            if event.key == pygame.K_RIGHT:
                caterpillar.move_right()

        # will work okay if a single player game
        if event.type == pygame.KEYUP:
            caterpillar.stop()

    # draw background
    draw_background(background, food-1)
    screen.blit(background, (0, 0))

    # find coordinates of sprites
    cp_coord = caterpillar.coordinates()
    poison_coord = poison.coordinates()
    w_coord = watermelon.coordinates()


    # check for collisions with poison
    if cp_coord.colliderect(poison_coord):
        # play hurt sound
        pygame.mixer.Sound.play(hurt)
        poison.remove() # remove poison from screen
        lives = 0


    # check for collisions with watermelon
    if cp_coord.colliderect(w_coord):
        # play eating sound
        pygame.mixer.Sound.play(chomp)
        watermelon.remove() # remove watermelon from screen
        watermelon.redo(screen) # reset watermelon position
        food = int(food*10) # increase score


    # breaks loop once player wins
    if food == 10000000000:
        break


    # constantly updates position of sprites on screen
    poison.update()
    caterpillar.update()
    watermelon.update()


    # make image of sprites appear on screen
    poison.draw(screen)
    watermelon.draw(screen)
    caterpillar.draw(screen)

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(360)


# creates game over background if dead
if lives == 0:
    game_over(background)
    screen.blit(background, (0, 0))


# creates background if player won and turned into a butterfly
if food == 10000000000:
    butterfly(background)
    screen.blit(background, (0, 0))


#update display
pygame.display.flip()

#wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
