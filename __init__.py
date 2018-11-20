#this is the main file, runs the game by play()

import pygame, sys
from Girl import *
from platformClass import *
from Prince import *
from itemClass import *
from stageGenerator import *

def play():

    pygame.init()
    screen = pygame.display.set_mode((900,600))
    pygame.display.set_caption("Liar Princess and the Blind Prince")
    
    platforms = []
    platforms.append(Platform(1800, 100, 450, 600, (0, 0, 0)))
    platforms.append(Platform(200, 15, 1100, 450, (0, 0, 0)))
    platforms.append(Platform(300, 15, 800, 300, (0, 0, 0)))
    platforms.append(Platform(250, 15, 1400, 450, (0, 0, 0)))
    platforms.append(Platform(100, 15, 1500, 375, (0, 0, 0)))
    platforms.append(Platform(200, 15, 1650, 480, (0, 0, 0)))
    platforms.append(Platform(200, 15, 1900, 450, (255, 255, 255)))
    platRects = [plat.rect for plat in platforms]
    
    walls = []
    walls.append(Wall(25, 180, 790, 300, (0, 0, 0)))
    walls.append(Wall(25, 180, 890, 500, (0, 0, 0)))
    walls.append(Wall(25, 180, 1660, 480, (0, 0, 0)))
    wallRect = [wall.rect for wall in walls]
    
    items = []
    items.append(Item('heart.png', 100, 500))
    items.append(Item('heart.png', 825, 285))
    #image taken from dreamincode.net walkthrough a platform game made with pygame
    
    player = Girl()
    prince = Prince()
    bg = pygame.image.load('bg.png').convert()
    #image taken from http://www.geocities.jp/kajiji21/haikei/mori_hiru.jpg
    bgX = 0
    
        
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #side scroll
        
        #if too far right of screen
        if ((not player.isWolf) and player.rectPrin.right > 600) or \
            (player.isWolf and player.rectWolf.right > 600):
            shift = -(player.rectPrin.right - 600)
            player.rectPrin.centerx += shift
            player.rectWolf.centerx += shift
            bgX += shift
            for plat in platRects:
                plat.x += shift
            for wall in wallRect:
                wall.x += shift
            for item in items:
                item.rect.x += shift
            prince.princeRect.x += shift
        #if too far left of screen
        elif ((not player.isWolf) and player.rectPrin.left <= 150 and bgX < 0) or\
            (player.isWolf and player.rectWolf.left <= 150 and bgX < 0):
            shift = 150 - player.rectPrin.left
            player.rectPrin.centerx += shift
            player.rectWolf.centerx += shift
            bgX += shift
            for plat in platRects:
                plat.x += shift
            for wall in wallRect:
                wall.x += shift
            for item in items:
                item.rect.x += shift
            prince.princeRect.x += shift
        if player.rectPrin.left == 0: bgX = 0
        
        
        
        screen.blit(bg, (bgX, 0))
                
        player.event(platRects)
        player.movement(platRects, bg)
        
        prince.event(platRects)
        prince.movement(platRects, bg)
    
        prince.draw(screen, bg)
        player.draw(screen, bg)
        
        for plat in platforms:
            plat.draw(screen)
            plat.collide(player, prince)
        for wall in walls:
            if wall.hit(player, prince, walls):
                wall.hit(player, prince, walls)
            wall.draw(screen)
        for item in items:
            if item.hit(player, items):
                items.remove(item)
            item.draw(screen)
        
            
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

play()