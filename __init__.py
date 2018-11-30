#this is the main file, runs the game by play()

import pygame, sys
from Girl import *
from platformClass import *
from Prince import *
from itemClass import *
from enemy import *
from stageGenerator import *
from startScreen import *

###


def play(level=1):
    
    pygame.init()
    screen = pygame.display.set_mode((1200,650))
    pygame.display.set_caption("Liar Princess and the Blind Prince")
    
    #generate stage
    solPath, solRect = randomStageGenerator(level)
    plats, platRect = otherPlats(solPath, level)
    
    walls, items, enemies = puzzles(plats, solPath, solRect, platRect, level)
    wallRect = [wall.rect for wall in walls]
    
    #key image taken from dreamincode.net walkthrough a platform game made with pygame
    
    
    player = Girl()
    prince = Prince()
    if level == 1:
        bg = pygame.image.load('bg.png').convert()
        #image taken from http://www.geocities.jp/kajiji21/haikei/mori_hiru.jpg
    elif level == 2:
        bg = pygame.image.load('bg2.png').convert()
        #image from https://blogs.yahoo.co.jp/kero3a/9425784.html
    else:
        bg = pygame.image.load('bg3.png')
        #image from http://kabegami.org/blog/2012/10/19/%E6%A3%AE%E3%81%AE%
        #   E4%B8%AD%E3%81%AE%E6%9D%91\-village-in-the-forest/
    bgX = 0
    
    #position players appropriately
    player.rectPrin.midbottom = solPath[0].rect.midtop
    player.rectWolf.midbottom = solPath[0].rect.midtop
    prince.princeRect.midbottom = solPath[0].rect.midtop
    prince.princeRect.left -= 80
    
    #game states
    if level == 1:
        start = True
        game = False
    else:
        start = False
        game = True
        
    gameOver = False
    clear = False
    help = False
    gameClear = False
    
    
    running = True
    
    while running:
        
        #start screen
        if start:
            startScreen(screen, bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        start = False
                        help = True
                    elif event.key == pygame.K_SPACE:
                        start = False
                        game = True
                        
        #controls/help screen
        if help:
            controls(screen, bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        help = False
                        start = True
        
        #game over screen
        if gameOver:
            lose(screen, bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameOver = False
                        play(1)
                         
        #level cleared screen                
        if clear:
            complete(screen, bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        clear = False
                        play(level + 1)
        
        #game clear screen
        if gameClear:
            end(screen, bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        clear = False
                        play(1)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        #game screen
        if game:  
            
            #side scroll
            
            #if too far right of screen
            if ((not player.isWolf) and player.rectPrin.right > 600) or \
                (player.isWolf and player.rectWolf.right > 600):
                shift = -(player.rectPrin.right - 600)
                player.rectPrin.centerx += shift
                player.rectWolf.centerx += shift
                bgX += shift
                for plat in platRect:
                    plat.x += shift
                for wall in wallRect:
                    wall.x += shift
                for item in items:
                    item.rect.x += shift
                for enemy in enemies:
                    enemy[0].enemyRect.x += shift
                prince.princeRect.x += shift
            #if too far left of screen
            elif ((not player.isWolf) and player.rectPrin.left <= 150 and bgX < 0) or\
                (player.isWolf and player.rectWolf.left <= 150 and bgX < 0):
                shift = 150 - player.rectPrin.left
                player.rectPrin.centerx += shift
                player.rectWolf.centerx += shift
                bgX += shift
                for plat in platRect:
                    plat.x += shift
                for wall in wallRect:
                    wall.x += shift
                for item in items:
                    item.rect.x += shift
                for enemy in enemies:
                    enemy[0].enemyRect.x += shift
                prince.princeRect.x += shift
            if player.rectPrin.left == 0: bgX = 0
            
            
            
            screen.blit(bg, (bgX, 0))
            
            #enemy logic
            for enemy in enemies:
                monster, loc = enemy
                monster.move(solRect[loc])
                if monster.enemyRect.colliderect(prince.princeRect):
                    gameOver = True
                if (not player.isWolf) and monster.enemyRect.colliderect(player.rectPrin):
                    gameOver = True
                monster.draw(screen, bg)
            
            #player logic        
            player.event(platRect)
            player.attack(enemies)
            player.movement(platRect)
            if player.rectPrin.centery > 580 or player.rectWolf.centery > 580:
                gameOver = True
                game = False
            
            prince.event(platRect)
            prince.movement(platRect)
            if prince.princeRect.centery > 580:
                gameOver = True
                game = False
                
            prince.draw(screen, bg)
            player.draw(screen, bg)
            
            #platforms, walls, keys 
            for plat in plats:
                plat.draw(screen)
                plat.collide(player, prince)
            for wall in walls:
                if wall.hit(player, prince, walls):
                    wall.hit(player, prince, walls)
                wall.draw(screen)
            for item in items:
                if item.hit(prince, items):
                    items.remove(item)
                item.draw(screen)
            
            #check if level or game cleared    
            if solRect[-1].colliderect(prince.princeRect) and \
                solRect[-1].colliderect(player.rectPrin) and \
                solRect[-1].colliderect(player.rectWolf):
                if level == 3:
                    gameClear = True
                else:
                    clear = True
                game = False
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

play()