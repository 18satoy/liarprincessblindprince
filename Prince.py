#this is the file for the Prince class

import pygame

class Prince ():
    def __init__(self):
        self.prince = pygame.image.load("ouji.png")
        #image from the PlayStation Store
        self.princeRect = self.prince.get_rect(midbottom = (300, 500))
        
        self.isMoving = False
        self.moveLeft = False
        self.moveRight = False
        self.jump = False
        
        self.jumpY = 0
        self.keyCount = 0
        
        #multiplayer
        self.PID = "Prince"
        
    def event(self, platRects):
        self.moveLeft = False
        self.moveRight = False
        keys = pygame.key.get_pressed()
        
        #movement
        if keys[pygame.K_d]:
            self.moveRight = True
            self.speed = 10
        elif keys[pygame.K_a]:
            self.moveLeft = True
            self.speed = -10
        if keys[pygame.K_w] and self.onGround(platRects):
            self.jump = True
    
    #taken from dreamincode.net  Walkthrough a Platform Game made with pygame #1      
    def onGround(self, platRects):
        collision = self.princeRect.collidelist(platRects)
        if collision > -1: return True
        else: return False
    
    def movement(self, platRects):
        #left, right, jump
        if self.moveRight and self.princeRect.right < 900:
            self.princeRect.centerx += self.speed
        elif self.moveLeft and self.princeRect.left > 0:
            self.princeRect.centerx += self.speed
        if self.jump:
            self.jumpY = -20
            self.jump = False
            
        self.princeRect.bottom += self.jumpY
        
        #jump and on ground logic
        if self.onGround(platRects):
            if self.jumpY >= 0:
                for plat in platRects:
                        if plat.collidepoint(self.princeRect.midbottom):
                            self.princeRect.bottom = plat.top + 1
            
                self.jumpY = 0
            else:
                #when height not enough to get on upper platform
                plat = platRects[self.princeRect.collidelist(platRects)]
                if self.princeRect.centerx - 20 > plat.right:
                    self.princeRect.left = plat.right
                elif self.princeRect.centerx  + 28 < plat.left:
                    self.princeRect.right = plat.left
                else:
                    self.princeRect.top = plat.bottom
                self.jumpY = 2
        else:
            self.jumpY += 2
            
    def draw(self, screen, bg):
        screen.blit(self.prince, self.princeRect)
