
import pygame
pygame.display.init()
ecran = pygame.display.set_mode((800, 600), pygame.FULLSCREEN) #fen�tre de trac�
image = pygame.image.load("./68.png") #charge une image � partir d'un fichier

continuer = True
while(continuer): #Boucle d'�v�nements
        for event in pygame.event.get(): #parcours de la liste des �v�nements
                if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si n�cessaire
                        continuer=False
pygame.quit()
