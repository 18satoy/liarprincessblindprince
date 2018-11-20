#this is the file for the item class

import pygame

class Item():
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect(midbottom=(x, y))
    
    def hit(self, player, items):
        if player.rectPrin.colliderect(self.rect):
            player.keyCount += 1 
            items.remove(self)
    def draw(self, screen):
        screen.blit(self.image, self.rect)