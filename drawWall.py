import pygame
def drawWall(surface,x,y,long,bol_hor) :
    #dessine un mur de longueur long, horizontale ou verticale
    if bol_hor == True :
        rect = pygame.Rect(x, y, long, 4)
    else :
        rect = pygame.Rect(x, y, 4, long)   
    pygame.draw.rect(surface,0 , rect, 0)
    
def drawFlat(surface,x,y,long,haut,text) :
    #dessine les contours 
    
    #texture 
    image = pygame.image.load("./pattern/"+text) #charge une image à partir d'un
                                                 #fichier
    
    i = 0
    j = 0
    imax = int(long / 100)
    jmax = int(haut / 99)
    
    while i < imax :
        j = 0
        while j < jmax :
            surface.blit(image,(i*100+x,j*99+y))
            j = j+1
        i = i+1
    #mur
    drawWall(surface,x,y,long,1)
    drawWall(surface,x,y,haut,0)
    drawWall(surface,x,y+haut-4,long,1)
    drawWall(surface,x+long-4,y,haut,0)
    
    
def drawRoom(surface,x,y,long,haut) :
    #dessine les contours d'une pièce sur surface
    #position : x, y (par rapport au coin en haut à gauche de la fenêtre)
    #taille : long, haut (en px)
    
    #mur
    drawWall(surface,x,y,long,1)
    drawWall(surface,x,y,haut,0)
    drawWall(surface,x,y+haut-4,long,1)
    drawWall(surface,x+long-4,y,haut,0)

    
def drawBathRoom(surface,x_flat,y_flat,x,y,long=90,haut=120) :
    x_bath = x_flat + x
    y_bath = y_flat + y
    drawRoom(surface, x_bath, y_bath,long,haut)
    
    drawObject(surface, x_bath + 4, y_bath, "wc.png")
    drawObject(surface, x_bath + 16,y_bath + 82, "lavabo_bathroom.png")
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

#def drawPlan(area,nbroom) :
        
def drawObject(surface, x, y, nom, angle = 0) :
    image = pygame.image.load("./image/"+nom)
    if angle != 0 :
        image = pygame.transform.rotate(image, angle)
    surface.blit(image,(x,y))
