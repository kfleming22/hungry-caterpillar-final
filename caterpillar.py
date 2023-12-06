import pygame
from parameters import *


# class for caterpillar (the sprite controlled by player)
class Caterpillar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        cp = pygame.image.load("assests/sprites/caterpillar.png")
        cp.set_colorkey((0,0,0)) # makes black background transparent
        self.forward_image = cp
        cpr = pygame.transform.flip(self.forward_image, True, False)
        cpr.set_colorkey((0,0,0)) # makes black background transparent
        self.reverse_image = cpr
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0


# will be used in main code to compare coordinates with food and poison
    def coordinates(self):
        cp_coord = pygame.Rect(self.x, self.y, caterpillar_width, caterpillar_height)
        return cp_coord


# moves caterpillar left and switches direction it faces
    def move_left(self):
        self.x_speed = -1 * 1
        self.image = self.reverse_image


# moves caterpillar right and switches direction it faces
    def move_right(self):
        self.x_speed = 1
        self.image = self.forward_image


# stops the caterpillar from moving
    def stop(self):
        self.x_speed = 0


# updates the caterpillar's position on the screen
    def update(self):

        self.x += self.x_speed

        if self.x > SCREEN_WIDTH- caterpillar_width:
            self.x = SCREEN_WIDTH - caterpillar_width
        if self.x < 0:
            self.x = 0
        self.rect.x = self.x
        self.rect.y = self.y


# makes the image of the caterpillar appear
    def draw(self, surf):
        surf.blit(self.image, self.rect)