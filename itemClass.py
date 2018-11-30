#this is the file for the item class

import pygame

class Key():
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect(midbottom=(x, y))
    
    def hit(self, prince, items):
        if self.rect.colliderect(prince.princeRect):
            prince.keyCount += 1
            items.remove(self)
    def draw(self, screen):
        screen.blit(self.image, self.rect)