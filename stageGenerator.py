#this generates the stages for the game

import pygame, random, copy
from platformClass import *
from itemClass import *
from enemy import *



def randomStageGenerator(level):
    stageLen = 2700
    minPlat = 100
    solPath = []
    if level == 1:
        color = (82, 44, 9)
    elif level == 2:
        color = (34, 77, 23)
    else:
        color = (102, 141, 60)
    
    #goal platform for now
    goalY = random.choice([500, 475, 450, 425, 400, 375, 350, 325, 300, 275, 250, 225, 200])
    goal = Platform(200, 15, 2500, goalY, (255, 255, 255))
    
    #first platform
    firstY = random.choice([600, 575, 550, 525, 500, 475, 450])
    firstPlat = Platform(800, 100, 300, firstY, color)
    
    solPath.append(firstPlat)
    stageGenerator(goal, solPath, level, color)
    
    #final goal platform to ensure solvability
    height = random.choice([50, 40, 30, -30, -40, -50])
    goal.rect.y = solPath[-1].rect.top + height
    goal.rect.x = solPath[-1].rect.right + (goal.sizeX // 2) + 40
    solPath.append(goal)
    solRect = [plat.rect for plat in solPath]
    
    return solPath, solRect
    
    
    
def stageGenerator(goal, solPath, level, color):
    if (len(solPath) > 1) and (goal.rect.left - solPath[-1].rect.right) <= 50:
        if goal.rect.left - solPath[-1].rect.right < 0:
            solPath[-1].sizeX -= (goal.rect.left - solPath[-1].rect.right - 30)
        return solPath
    else:
        #as level increases, shorter platforms used
        if level == 1:
            platX = random.choice([200, 250, 300, 350, 400, 450])
        elif level == 2:
            platX = random.choice([200, 250, 300, 350, 400, 200, 300])
        elif level >= 3:
            platX = random.choice([200, 250, 225, 300, 250, 350, 400, 325, 150])
        dy = random.choice([60, 50,40,30,-30,-40,-50, -60])
        placeX = solPath[-1].rect.right + (platX // 2) + random.randint(80, 105)
        test = Platform(platX, 15, placeX, solPath[-1].rect.top + dy, color)
        if isLegal(goal, test, solPath):
            solPath.append(test)
            stageGenerator(goal, solPath, level, color)
        else: 
            stageGenerator(goal, solPath, level, color)
            

def isLegal(goal, test, solPath):
    if (test.rect.left - solPath[-1].rect.right) > 150: 
        return False
    if solPath[-1].rect.top - test.rect.top > 100:
        return False
    return True

def otherPlats(solPath, level):
    numPlats = len(solPath)
    extraPlats = len(solPath)
    plats = copy.copy(solPath)
    
    #colors for platforms for each level
    if level == 1:
        color = (82, 44, 9)
    elif level == 2:
        color = (34, 77, 23)
    else:
        color = (102, 141, 60)
    for num in range(2, extraPlats):
        lenX = random.choice([250, 300, 350, 400])
        locX = random.randrange(solPath[num - 1].rect.right, solPath[num].rect.left, 30)
        vertical = random.choice(["up", "down", "up", "down", "up", "down", 'up'])
        if vertical == "up":
            dy = random.choice([-250, -150, -200])
            height = min(solPath[num - 1].rect.top, solPath[num].rect.top) + dy
        else:
            dy = random.choice([130, 110, 150])
            height = max(solPath[num - 1].rect.top, solPath[num].rect.top) + dy
        dummy = Platform(lenX, 15, locX, height, color)
        plats.append(dummy)
    platRect = [plat.rect for plat in plats]
    return plats, platRect

def puzzles(plats, solPath, solRect, platRects, level):
    #generate walls
    walls = []
    # number of walls increases with level
    if level == 1:
        numWalls = random.randint(2, 4)
    elif level == 2:
        numWalls = random.randint(3, len(solPath) - 3)
    elif level == 3:
        numWalls = random.randint(3, len(solPath) - 2)
    platNums = [ i for i in range(1, len(solPath) - 1)]
    indices = []
    if level == 1:
        color = (82, 44, 9)
    elif level == 2:
        color = (34, 77, 23)
    else:
        color = (102, 141, 60)
    for num in range(numWalls):
        loc = random.choice(platNums)
        platNums.remove(loc)
        indices.append(loc)
        locX = solPath[loc].rect.centerx + 10
        locY = solPath[loc].rect.top
        wall = Wall( 30, 210, locX, locY, color)
        walls.append(wall)
        
    #generate keys as necessary 
    keys = []
    numKeys = numWalls
    for key in range(numKeys):
        index = indices[key]
        x = random.randint(solPath[index - 1].rect.left + 40, solPath[index - 1].rect.right - 30)
        if index - 1 == 0:
            x = solPath[index-1].rect.right - 50
        y = solPath[index -1].rect.top + 1
        item = Key('heart.png', x, y)
        keys.append(item)
        
    #generate enemies    
    enemPlats = solRect[1:]    
    enemies = []
    #no enemies for first level
    if level > 1:
        #number of enemies increase as level increases
        if level == 2:
            numEnemies = random.choice([1, 2])
        elif level == 3:
            numEnemies = random.choice([2, 3, 4, 5])
        for num in range(numEnemies + 1):
            loc = random.randint(0, len(enemPlats) - 1)
            platNum = loc + 1
            x = solRect[platNum].centerx
            y = solRect[platNum].top
            enemy = Enemy(x, y)
            enemies.append((enemy, platNum))
        
    return walls, keys, enemies
   