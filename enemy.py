#file for the enemy class

import pygame

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.enemyRect = self.image.get_rect(midbottom=(x, y))
        self.speed = 5
        
    def move(self, plat):
        self.enemyRect.centerx += self.speed
        if self.enemyRect.right >= plat.right:
            self.speed = -5
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.enemyRect.left <= plat.left:
            self.speed = 5
            self.image = pygame.transform.flip(self.image, True, False)
            
    def draw(self, screen, bg):
        screen.blit(self.image, self.enemyRect)