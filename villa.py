
import pygame
from draw import *
pygame.display.init()

m = 60 #sert pour l'echelle : 1m : 60px

long_terrasse = 4*m

ecran = pygame.display.set_mode((940+long_terrasse, 640)) #fenêtre de tracé
ecran.fill((255,255,255)) # colore en blanc l'écran



long_flat = 12*m
haut_flat = 9*m

posX_flat = 940/2- long_flat/2
posY_flat = 640/2- haut_flat/2

drawFlat(ecran,posX_flat,posY_flat,long_flat,haut_flat,"95.png","exemple de villa")

drawBathRoom(ecran,posX_flat,posY_flat,0,3*m,3.5*m,2*m, True)
drawBedRoom(ecran,posX_flat,posY_flat,0,0, 3.5*m,3*m, "ch 3")
drawBedRoom(ecran,posX_flat,posY_flat,long_flat-4*m,0, 4*m,3*m, "ch 2")
drawBedRoom(ecran,posX_flat,posY_flat, 0,haut_flat - 3*m, 5*m,3*m, "ch 1")
drawKitchen(ecran,posX_flat,posY_flat,6*m,6*m, 4*m, 3*m)

drawObject(ecran, posX_flat+3*m, posY_flat+6.5*m, "canape.png",90)
drawObject(ecran, posX_flat+6.5*m, posY_flat+3.5*m, "billard.png")

drawObject(ecran, posX_flat+5*m, posY_flat+0.7*m-20, "table.png",0)

drawTerrasse(ecran,posX_flat,posY_flat, long_flat,0,4*m,haut_flat, True)

pygame.display.flip()
continuer = True

while(continuer): #Boucle d'événements
        for event in pygame.event.get(): #parcours de la liste des événements
                if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
                        continuer=False
pygame.quit()
