
import pygame
from drawWall import *
pygame.display.init()
ecran = pygame.display.set_mode((940, 640)) #fenêtre de tracé
image = pygame.image.load("./pattern/68.png") #charge une image à partir d'un fichier
i = 0
while i < 4 :
        ecran.blit(image,(i*203,0))
        ecran.blit(image,(i*203,317))
        i = i+1
drawRoom(ecran,100,200,50,150)
drawRoom(ecran,146,200,50,150)
pygame.display.flip()
continuer = True

while(continuer): #Boucle d'événements
        for event in pygame.event.get(): #parcours de la liste des événements
                if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
                        continuer=False
pygame.quit()
