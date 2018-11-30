#this is the file for the platform class

import pygame

class Platform():
    def __init__(self, sizeX, sizeY, x, y, color):
        self.sizeX = sizeX
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

#can be removed with key
class Wall(Platform):
    def __init__(self, sizeX, sizeY, x, y, color):
        super().__init__(sizeX, sizeY, x, y, color)
        
    def hit(self, player, prince, walls):
        if player.isWolf and player.rectWolf.colliderect(self.rect):
            player.rectWolf.right = self.rect.left
            player.rectPrin.right = self.rect.left
        if ((not player.isWolf) and player.rectPrin.colliderect(self.rect)):
            player.rectPrin.right = self.rect.left
            player.rectWolf.right = self.rect.left
        if prince.princeRect.colliderect(self.rect):
            if prince.keyCount > 0:
                prince.keyCount -= 1
                walls.remove(self)
            else:
                prince.princeRect.right = self.rect.left