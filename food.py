import pygame
import random
from parameters import *


# make class for food (food is the watermelon)
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assests/sprites/watermelon.png").convert()
        self.image.set_colorkey((0, 0, 0)) # makes black background transparent
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = watermelonfall
        self.rect.center = (x, y)


# used to check for collision with caterpillar
    def coordinates(self):
        w_coord = pygame.Rect(self.x, self.y, wmw, wmh)
        return w_coord


# updates position of watermelon on the screen
    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.y > SCREEN_HEIGHT- self.image.get_height():
            self.y = 0
            self.x = self.image.get_width()+random.randint(20,SCREEN_WIDTH-2*self.image.get_width())
        self.rect.x = self.x
        self.rect.y = self.y


# stops watermelon
    def stop(self):
        self.speed = 0


# makes image of watermelon appear on screen
    def draw(self, surf):
        surf.blit(self.image, self.rect.center)


# used in main code to put watermelon back at the top after collision
    def redo(self, surf):
        self.y = 0
        self.x = self.image.get_width() + random.randint(20, SCREEN_WIDTH - 2 * self.image.get_width())
        surf.blit(self.image, self.rect.center)

