
import pygame
from draw import *
pygame.display.init()

ecran = pygame.display.set_mode((940, 640)) #fenêtre de tracé
ecran.fill((255,255,255)) # colore en blanc l'écran
m = 60 #sert pour l'echelle : 1m : 60px

posX_flat = 940/2-3*60
posY_flat = 640/2-5*30
long_flat = 7*m-20
haut_flat = 5*m

drawFlat(ecran,posX_flat,posY_flat,long_flat,haut_flat,"74.png")

drawBathRoom(ecran,posX_flat,posY_flat,0,0)


drawObject(ecran, posX_flat+5*m, posY_flat+3*m-20, "canape.png",270)
drawObject(ecran, posX_flat+5*m, posY_flat+3*m-20, "canape.png",180)
drawObject(ecran, posX_flat+5*m, posY_flat+0.5*m-20, "table.png")
drawObject(ecran, posX_flat, posY_flat+3.5*m, "lavabo_cuisine.png")

pygame.display.flip()
continuer = True

while(continuer): #Boucle d'événements
        for event in pygame.event.get(): #parcours de la liste des événements
                if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
                        continuer=False
pygame.quit()
