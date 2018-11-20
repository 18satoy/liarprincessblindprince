#this is the file for the platform class

import pygame

class Platform():
    def __init__(self, sizeX, sizeY, x, y, color):
        self.surface = pygame.surface.Surface((sizeX, sizeY))
        self.rect = self.surface.get_rect(midbottom=(x, y))
        self.surface.fill(color)
    
    def collide(self, player, prince):
        if not player.isWolf:
            #forward
            if player.rectPrin.collidepoint(self.rect.bottomleft):
                player.rectPrin.right = self.rect.left
                player.rectWolf.right = self.rect.left
            #backward
            elif player.rectPrin.collidepoint(self.rect.bottomright):
                player.rectPrin.left = self.rect.right
                player.rectWolf.left = self.rect.right
        else:
            #forward
            if player.rectWolf.collidepoint(self.rect.bottomleft):
                player.rectPrin.right = self.rect.left
                player.rectWolf.right = self.rect.left
            #backward
            elif player.rectWolf.collidepoint(self.rect.bottomright):
                player.rectPrin.left = self.rect.right
                player.rectWolf.left = self.rect.right
                
        #prince
        #forward
        if prince.princeRect.collidepoint(self.rect.bottomleft):
            prince.princeRect.right = self.rect.left
        #backward
        elif prince.princeRect.collidepoint(self.rect.bottomright):
            prince.princeRect.left = self.rect.right
    
    def draw(self, screen):
        screen.blit(self.surface, self.rect)

class Wall(Platform):
    def __init__(self, sizeX, sizeY, x, y, color):
        super().__init__(sizeX, sizeY, x, y, color)
        
    def hit(self, player, prince, walls):
        if player.rectPrin.colliderect(self.rect) or player.rectWolf.colliderect(self.rect):
            if player.keyCount > 0:
                player.keyCount -= 1
                walls.remove(self)
            else:
                player.rectPrin.right = self.rect.left
                player.rectWolf.right = self.rect.left
                
        if prince.princeRect.colliderect(self.rect):
            prince.princeRect.right = self.rect.left