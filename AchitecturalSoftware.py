
import pygame
pygame.display.init()
ecran = pygame.display.set_mode((800, 600), pygame.FULLSCREEN) #fenêtre de tracé
image = pygame.image.load("./68.png") #charge une image à partir d'un fichier

continuer = True
while(continuer): #Boucle d'événements
        for event in pygame.event.get(): #parcours de la liste des événements
                if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
                        continuer=False
pygame.quit()
