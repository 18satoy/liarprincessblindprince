#this has the screens for start, help/controls, gameover, level cleared, and game cleared

import pygame, sys

#start screen
def startScreen(screen, bg):
    screen.blit(bg, (0, 0))
    title = pygame.font.Font(None, 72).render("Liar Princess and the Blind Prince",
        True, (255, 255, 255))
    titleRect = title.get_rect()
    titleX = 600 - (titleRect.width // 2)
    titleY = 300 - (titleRect.height // 2)
    
    help = pygame.font.Font(None, 60).render("Press h for controls", True, (255, 255, 255))
    helpRect = help.get_rect()
    helpX = 600 - (helpRect.width // 2)
    helpY = 400 - (helpRect.height // 2)
    
    start = pygame.font.Font(None, 60).render("Press Space to play", True, (255, 255, 255))
    startRect = start.get_rect()
    startX = 600 - (startRect.width // 2)
    startY = 450 - (startRect.height // 2)
    
    screen.blit(title, (titleX, titleY))
    screen.blit(help, (helpX, helpY))
    screen.blit(start, (startX, startY))

#shows controls for game
def controls(screen, bg):
    screen.blit(bg, (0, 0))
    controls = pygame.image.load('control.png')
    screen.blit(controls, (200, 0))
    text = pygame.font.Font(None, 48).render("Press Space to go back", True, (255, 255, 255))
    textRect = text.get_rect()
    textX = 600 - (textRect.width // 2)
    textY = 560 - (textRect.height // 2)
    screen.blit(text, (textX, textY))

#when game over
def lose(screen, bg):
    screen.blit(bg, (0, 0))
    text = pygame.font.Font(None, 72).render("Game Over", True, (255, 255, 255))
    textRect = text.get_rect()
    textX = 600 - (textRect.width // 2)
    textY = 300 - (textRect.height // 2)
    next = pygame.font.Font(None, 60).render("Press Space to play again", True, (255, 255, 255))
    nextRect = next.get_rect()
    nextX = 600 - (nextRect.width // 2)
    nextY = 400 - (nextRect.height // 2)
    screen.blit(bg, (0, 0))
    screen.blit(text, (textX, textY))
    screen.blit(next, (nextX, nextY))
                
#when level cleared
def complete(screen, bg):
    screen.blit(bg, (0, 0))
    text = pygame.font.Font(None, 90).render("Level Cleared!", True, (255, 255, 255))
    textRect = text.get_rect()
    textX = 600 - (textRect.width // 2)
    textY = 300 - (textRect.height // 2)
    screen.blit(bg, (0, 0))
    screen.blit(text, (textX, textY))
    next = pygame.font.Font(None, 48).render("Press Space for Next Level", True, (255, 255, 255))
    nextRect = next.get_rect()
    nextX = 600 - (nextRect.width // 2)
    nextY = 400 - (nextRect.height // 2)
    screen.blit(next, (nextX, nextY))
#when game cleared
def end(screen, bg):
    screen.blit(bg, (0, 0))
    text = pygame.font.Font(None, 90).render("Game Cleared!", True, (255, 255, 255))
    textRect = text.get_rect()
    textX = 600 - (textRect.width // 2)
    textY = 300 - (textRect.height // 2)
    screen.blit(text, (textX, textY))