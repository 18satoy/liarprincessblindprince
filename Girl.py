#this is the file for the Werewolf girl class
import pygame

class Girl ():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        princess = pygame.image.load('hime.png')
        self.princess = pygame.transform.scale(princess, (100, 100))
        self.rectPrin = self.princess.get_rect(midbottom=(450,500))
        self.wolf = pygame.image.load('test.png')
        self.rectWolf = self.wolf.get_rect\
            (midbottom=(self.rectPrin.centerx, self.rectPrin.bottom))
        self.isWolf = False
        
        self.keyCount = 0
        #movement
        
        self.isMoving = False
        self.moveLeft = False
        self.moveRight = False
        self.jump = False
        self.wolfJump = False
        self.attack = False
        
        self.jumpY = 0
        self.speed = 0
    
    def event(self, platRects):
        self.moveLeft = False
        self.moveRight = False
        keys = pygame.key.get_pressed()
        
        #movement
        if keys[pygame.K_RIGHT]:
            self.moveRight = True
            self.speed = 5
        elif keys[pygame.K_LEFT]:
            self.moveLeft = True
            self.speed = -5
        if keys[pygame.K_SPACE] and self.onGround(platRects):
            if self.isWolf:
                self.wolfJump = True
            else: self.jump = True
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            self.isWolf = not self.isWolf
        if keys[pygame.K_KP_ENTER]:
            self.attack = True
        
    
    #taken from dreamincode.net  Walkthrough a Platform Game made with pygame #1       
    def onGround(self, platRects):
        if not self.isWolf:
            collision = self.rectPrin.collidelist(platRects)
        else: collision = self.rectWolf.collidelist(platRects)
        if collision > -1: return True
        else: return False
    
    def movement(self, platRects, bg):
        #left, right, jump
        if self.moveRight and self.rectPrin.right < 900:
            self.rectPrin.centerx += self.speed
            self.rectWolf.centerx += self.speed
        elif self.moveLeft and self.rectPrin.left > 0:
            self.rectPrin.centerx += self.speed
            self.rectWolf.centerx += self.speed
        if self.jump:
            self.jumpY = -18
            self.jump = False
            
        #wolf jump
        if self.wolfJump:
            self.jumpY = -25
            self.wolfJump = False
        self.rectPrin.bottom += self.jumpY
        self.rectWolf.bottom += self.jumpY
        
        #jump and on ground logic
        if self.onGround(platRects):
            if self.jumpY >= 0:
                for plat in platRects:
                    if not self.isWolf:
                        if plat.collidepoint(self.rectPrin.bottomright):
                            self.rectPrin.bottom = plat.top + 1
                            self.rectWolf.bottom = plat.top + 1
                    else:
                        if plat.collidepoint((self.rectWolf.bottomright)):
                            self.rectPrin.bottom = plat.top + 1
                            self.rectWolf.bottom = plat.top + 1
            
                self.jumpY = 0
            else:
                self.rectPrin.top = \
                    platRects[self.rectPrin.collidelist(platRects)].bottom
                self.rectWolf.top = \
                    platRects[self.rectWolf.collidelist(platRects)].bottom
                self.jumpY = 2
        else:
            self.jumpY += 2
            
    
    def changeMode(self):
        if self.onGround(platRects):
            self.isWolf = not self.isWolf
           
    def attack(self):
        #work in progress
        if self.isWolf:
            pass
    
    def draw(self, screen, bg):
        if not self.isWolf: 
            screen.blit(self.princess, self.rectPrin)
        else:
            screen.blit(self.wolf, self.rectWolf)
        

