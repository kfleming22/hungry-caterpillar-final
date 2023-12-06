import pygame
import random
from parameters import *


# make class for the poison
class Poison(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assests/sprites/poison.png").convert()
        self.image.set_colorkey((0, 0, 0)) # makes black background transparent
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = poisonfall
        self.rect.center = (x, y)


# used in main code to check for collisions with caterpillar
    def coordinates(self):
        poison_coord = pygame.Rect(self.x, self.y, poisonw, poisonh)
        return poison_coord


# updates position of the poison as it's falling
    def update(self):
        self.speed += 0.0002 # poison gets faster the longer the game continues
        self.y += self.speed
        self.rect.y = self.y
        if self.y > SCREEN_HEIGHT- self.image.get_height():
            self.y = 0
            self.x = self.image.get_width()+random.randint(20,SCREEN_WIDTH-2*self.image.get_width())
        self.rect.x = self.x
        self.rect.y = self.y


# stops poison
    def stop(self):
        self.speed = 0


# makes image of poison appear on screen
    def draw(self, surf):
        surf.blit(self.image, self.rect.center)
