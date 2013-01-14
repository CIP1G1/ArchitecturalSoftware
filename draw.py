import pygame
#fonctions de base
def drawWall(surface,x,y,long,bol_hor, ep = 4) :
    #dessine un mur de longueur long, horizontale ou verticale
    #ep : epaisseur en pixel du mur, par défaut 4px d'épaisseur soit 6.6cm
    
    if bol_hor == True :
        rect = pygame.Rect(x, y, long, ep)
    else :
        rect = pygame.Rect(x, y, ep, long)   
    if ep == 6 : #mur principal, en noir
        pygame.draw.rect(surface,0 , rect, 0)
    else : #autre mur, en gris claire
        pygame.draw.rect(surface,(200,200,200) , rect, 0)
def drawRoom(surface,x,y,long,haut, ep = 4) :
    #dessine les contours d'une pièce sur surface
    #position : x, y (par rapport au coin en haut à gauche de la fenêtre)
    #taille : long, haut (en px)
    #ep : epaisseur des murs, 4 par défaut pour une pièce, 6 pour les contours principaux
    
    #mur
    drawWall(surface,x,y,long,1, ep)
    drawWall(surface,x,y,haut,0, ep)
    drawWall(surface,x,y+haut-ep,long,1, ep)
    drawWall(surface,x+long-ep,y,haut,0, ep)
    
def drawObject(surface, x, y, nom, angle = 0) :
    #dessine un objet à la position voulue avec éventuellement un angle
    image = pygame.image.load("./image/objets/"+nom)
    if angle != 0 :
        image = pygame.transform.rotate(image, angle)
    surface.blit(image,(x,y))
    
def drawTexture(surface,x,y,long,haut,str_text) :
    #dessine la texture d'une pièce
    #str_text nom du fichier de la texture(dans pattern/)
    
    i_text = pygame.image.load("./pattern/"+str_text) #charge depuis un fichier
    long_text = i_text.get_width()
    haut_text = i_text.get_height()
    i = 0
    j = 0
    imax = int(long / long_text)
    jmax = int(haut / haut_text)
    
    while i < imax + 1 :
        j = 0
        while j < jmax + 1 :
            if j != jmax and i != imax :
                surface.blit(i_text,(i*long_text+x,j*haut_text+y))
            elif j == jmax and i != imax : #on ne colle pas toute la texture pour ne pas dépasser
                text_rect = pygame.Rect(0,0, long_text, haut % haut_text)
                surface.blit(i_text,(i*long_text+x,j*haut_text+y),text_rect)
            elif j != jmax and i == imax :
                text_rect = pygame.Rect(0,0, long % long_text, haut_text)
                surface.blit(i_text,(i*long_text+x,j*haut_text+y),text_rect)
            else:
                text_rect = pygame.Rect(0,0, long % long_text, haut % haut_text)
                surface.blit(i_text,(i*long_text+x,j*haut_text+y),text_rect)
            j = j+1
        i = i+1

#fonction combinés    
def drawFlat(surface,x,y,long,haut,str_text,nom) :
    #dessine les contours du plan habitable avec la texture, le nom et la superficie
    
    #texture 
    drawTexture(surface,x,y,long,haut,str_text)
    
    #mur
    drawRoom(surface, x, y,long,haut, 6)
    
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 40) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    surf = round(surf, 1)
    texte = nom + " : " + str(surf) + "m²"
    i_texte = font.render(texte,1,(0,100,200)) 
    surface.blit(i_texte, (x + long/2 - i_texte.get_width()/2, y - i_texte.get_height()))
    pygame.font.quit()

    #affiche l'échelle
    drawObject(surface,x, y+haut, "echelle.png")
    
    


    
def drawBathRoom(surface,x_flat,y_flat,x,y,long=90,haut=120, bol_baignoire = False) :
    #dessine une salle de bain standard avec ou sans baignoire
    
    x_bath = x_flat + x
    y_bath = y_flat + y

    if haut < 120 : #pas assès de place pour une baignoire
        bol_baignoire = False
    
    drawTexture(surface, x_bath,y_bath,long,haut, "74.png")
    drawRoom(surface, x_bath, y_bath,long,haut)
    
    drawObject(surface, x_bath + 4, y_bath, "wc.png")
    drawObject(surface, x_bath + 16,y_bath + haut - 34, "lavabo_bathroom.png")
    if bol_baignoire == True :
        drawObject(surface, x_bath + long - 52,y_bath + 4, "baignoire.png")
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 20) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    surf = round(surf, 1)
    texte = "salle de bain " 
    i_texte = font.render(texte,1,(0,0,200))
    surface.blit(i_texte, (x_bath,y_bath+haut/3))
    texte = str(surf) + "m²"
    i_texte = font.render(texte,1,(0,0,200))
    surface.blit(i_texte, (x_bath+long/2 - i_texte.get_width()/2,y_bath+haut/2))
    pygame.font.quit()

def drawBedRoom(surface,x_flat,y_flat,x,y,long=240,haut=180, nom = "chambre") :
    #dessine une chambre standart avec un lit
    
    x_bed = x_flat + x
    y_bed = y_flat + y
    
    drawTexture(surface, x_bed,y_bed,long,haut, "67.png")
    drawRoom(surface, x_bed, y_bed,long,haut)
    
    drawObject(surface, x_bed + 4, y_bed, "lit.png")
    
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 20) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    surf = round(surf, 1)
    texte = nom
    i_texte = font.render(texte,1,(200,0,20))
    surface.blit(i_texte, (x_bed+20,y_bed+haut/3))
    texte = str(surf) + "m²"
    i_texte = font.render(texte,1,(200,0,20))
    surface.blit(i_texte, (x_bed+long/2 - i_texte.get_width()/2,y_bed+haut/2))
    pygame.font.quit()
    
def drawKitchen(surface,x_flat,y_flat,x,y,long=180,haut=180, nom = "cuisine") :
    #dessine une cuisine standart
    
    x_kitch = x_flat + x
    y_kitch = y_flat + y
    
    drawTexture(surface, x_kitch,y_kitch,long,haut, "61.png")
    drawRoom(surface, x_kitch, y_kitch,long,haut)
    
    drawObject(surface, x_kitch , y_kitch, "lavabo_cuisine.png")
    drawObject(surface, x_kitch + 2 , y_kitch + 25, "micro_onde.png")
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 20) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    surf = round(surf, 1)
    texte = nom
    i_texte = font.render(texte,1,(150,115,185))
    surface.blit(i_texte, (x_kitch+20,y_kitch+haut/3))
    texte = str(surf) + "m²"
    i_texte = font.render(texte,1,(150,115,185))
    surface.blit(i_texte, (x_kitch+long/2 - i_texte.get_width()/2,y_kitch+haut/2))
    pygame.font.quit()
    
def drawTerrasse(surface,x_flat,y_flat,x,y,long=240,haut=180,  bol_piscine = False, nom = "terrasse") :
    #dessine une terrasse standart avec ou sans piscine
    
    x_ter = x_flat + x
    y_ter = y_flat + y
    
    drawTexture(surface, x_ter,y_ter,long,haut, "94.jpg")

    if bol_piscine == True :
        drawTexture(surface, x_ter +20 ,y_ter + 40 ,long - 40,haut - 80, "eau.png")
    
    #affiche le nom et la superficie de la terrasse
    pygame.font.init()
    font = pygame.font.Font(None, 40) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    surf = round(surf, 1)
    texte = nom + " : " + str(surf) + "m²"
    i_texte = font.render(texte,1,(0,100,200)) 
    surface.blit(i_texte, (x_flat + x + long/2 - i_texte.get_width()/2, y_flat - i_texte.get_height()))
    pygame.font.quit()
             

