import pygame
def drawWall(surface,x,y,long,bol_hor) :
    #dessine un mur de longueur long, horizontale ou verticale
    if bol_hor == True :
        rect = pygame.Rect(x, y, long, 4)
    else :
        rect = pygame.Rect(x, y, 4, long)   
    pygame.draw.rect(surface,0 , rect, 0)


def drawTexture(surface,x,y,long,haut,str_text) :
    #dessine la texture d'une pièce avec le nom de la texture
    
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
    
def drawFlat(surface,x,y,long,haut,str_text,nom) :
    #dessine les contours du plan avec la texture, le nom et la superficie
    
    #texture 
    drawTexture(surface,x,y,long,haut,str_text)
    
    #mur
    drawWall(surface,x,y,long,1)
    drawWall(surface,x,y,haut,0)
    drawWall(surface,x,y+haut-4,long,1)
    drawWall(surface,x+long-4,y,haut,0)

    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 40) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²

    drawObject(surface,x, y+haut, "echelle.png")
    texte = nom + " : " + str(surf) + "m²"
    i_texte = font.render(texte,1,(0,100,200)) 
    surface.blit(i_texte, (x + long/2 - i_texte.get_width()/2, y - i_texte.get_height()))
    pygame.font.quit()
    
    
def drawRoom(surface,x,y,long,haut) :
    #dessine les contours d'une pièce sur surface
    #position : x, y (par rapport au coin en haut à gauche de la fenêtre)
    #taille : long, haut (en px)
    
    #mur
    drawWall(surface,x,y,long,1)
    drawWall(surface,x,y,haut,0)
    drawWall(surface,x,y+haut-4,long,1)
    drawWall(surface,x+long-4,y,haut,0)

    

    
def drawBathRoom(surface,x_flat,y_flat,x,y,long=90,haut=120, bol_baignoire = False) :
    #dessine une salle de bain standard avec ou sans baignoire
    
    x_bath = x_flat + x
    y_bath = y_flat + y
    
    drawTexture(surface, x_bath,y_bath,long,haut, "74.png")
    drawRoom(surface, x_bath, y_bath,long,haut)
    
    drawObject(surface, x_bath + 4, y_bath, "wc.png")
    drawObject(surface, x_bath + 16,y_bath + 82, "lavabo_bathroom.png")
    if bol_baignoire == True :
        drawObject(surface, x_bath + long - 52,y_bath + 4, "baignoire.png")
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 20) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    texte = "salle de bain " 
    i_texte = font.render(texte,1,(0,0,200))
    surface.blit(i_texte, (x_bath,y_bath+haut/3))
    texte = str(surf) + "m²"
    i_texte = font.render(texte,1,(0,0,200))
    surface.blit(i_texte, (x_bath+long/2 - i_texte.get_width()/2,y_bath+haut/2))
    pygame.font.quit()

def drawBedRoom(surface,x_flat,y_flat,x,y,long=240,haut=180, nom = "chambre") :
    #dessine une chambre standart
    
    x_bed = x_flat + x
    y_bed = y_flat + y
    
    drawTexture(surface, x_bed,y_bed,long,haut, "67.png")
    drawRoom(surface, x_bed, y_bed,long,haut)
    
    drawObject(surface, x_bed + 4, y_bed, "lit.png")
    
    #nom de la pièce et surface de la pièce
    pygame.font.init()
    font = pygame.font.Font(None, 20) #charge la police par défaut de pygame
    surf = long*haut/3600 # surface en m²
    texte = nom
    i_texte = font.render(texte,1,(200,0,20))
    surface.blit(i_texte, (x_bed+20,y_bed+haut/3))
    texte = str(surf) + "m²"
    i_texte = font.render(texte,1,(200,0,20))
    surface.blit(i_texte, (x_bed+long/2 - i_texte.get_width()/2,y_bed+haut/2))
    pygame.font.quit()

           
def drawObject(surface, x, y, nom, angle = 0) :
    #dessine un objet à la position voulue
    image = pygame.image.load("./image/"+nom)
    if angle != 0 :
        image = pygame.transform.rotate(image, angle)
    surface.blit(image,(x,y))
