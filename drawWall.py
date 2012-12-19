import pygame
def drawWall(surface,x,y,long,horizontal) :
    if horizontal == True :
        rect = pygame.Rect(x, y, long, 4)
    else :
        rect = pygame.Rect(x, y, 4, long)   
    pygame.draw.rect(surface,0 , rect, 0)
    
def drawRoom(surface,x,y,long,haut) :
    drawWall(surface,x,y,long,1)
    drawWall(surface,x,y,haut,0)
    drawWall(surface,x,y+haut-4,long,1)
    drawWall(surface,x+long-4,y,haut,0)
#1m = 60px
#def drawPlan(area,nbroom) :
        
