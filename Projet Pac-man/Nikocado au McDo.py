import pygame # importation de la librairie pygame
from pygame.locals import *
from pygame import mixer
import Classes
from Classes import*
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
# définir une clock
clock=pygame.time.Clock()
FPS=400

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("The journey of Nikocado") 

# chargement de l'image de fond et du laby
fond=pygame.image.load("Images\-Amogus.png").convert_alpha()
rip_bozo=pygame.image.load("Images\-Nick-Avocado.png").convert_alpha()

# musique
mixer.init()
mixer.music.load("Sons\Retro.mp3")
mixer.music.play(10)

# creation du joueur et des ennemis
player = Classes.Joueur()
listeEnnemis = []
for indice in range(Classes.Ennemi.NbEnnemis):
    mechant = Classes.Ennemi()
    old_x2, old_y2 = mechant.rect.x, mechant.rect.y
    vi_Y=mechant.vitesseY
    vi_X=mechant.vitesseX
    listeEnnemis.append(mechant)

# creation des burgers et des cocas
liste_burger=pygame.sprite.Group()
liste_coca=pygame.sprite.Group()

burger=Classes.Burger(51,131)
burger2=Classes.Burger(91,131)
burger3=Classes.Burger(131,131)
burger4=Classes.Burger(171,131)
burger5=Classes.Burger(211,131)
burger6=Classes.Burger(251,131)
burger7=Classes.Burger(291,131)
burger8=Classes.Burger(331,131)
burger9=Classes.Burger(451,131)

burger10=Classes.Burger(491,131)
burger11=Classes.Burger(531,131)
burger12=Classes.Burger(571,131)
burger13=Classes.Burger(611,131)
burger14=Classes.Burger(651,131)
burger15=Classes.Burger(691,131)
burger16=Classes.Burger(731,131)

burger17=Classes.Burger(51,171)
burger18=Classes.Burger(211,171)
burger19=Classes.Burger(251,171)
burger20=Classes.Burger(291,171)
burger21=Classes.Burger(331,171)
burger22=Classes.Burger(371,171)
burger23=Classes.Burger(451,171)
burger24=Classes.Burger(491,171)
burger25=Classes.Burger(531,171)
burger26=Classes.Burger(571,171)
burger27=Classes.Burger(731,171)

burger28=Classes.Burger(51,211)
burger29=Classes.Burger(171,211)
burger30=Classes.Burger(211,211)
burger31=Classes.Burger(571,211)
burger32=Classes.Burger(611,211)
burger33=Classes.Burger(731,211)

burger34=Classes.Burger(51,251)
burger35=Classes.Burger(91,251)
burger36=Classes.Burger(131,251)
burger37=Classes.Burger(171,251)
burger38=Classes.Burger(571,251)
burger39=Classes.Burger(611,251)
burger40=Classes.Burger(651,251)
burger41=Classes.Burger(691,251)
burger42=Classes.Burger(731,251)
burger43=Classes.Burger(211,251)

burger44=Classes.Burger(51,291)
burger45=Classes.Burger(211,291)
burger46=Classes.Burger(211,291)
burger47=Classes.Burger(211,291)
burger48=Classes.Burger(211,291)
burger49=Classes.Burger(211,291)
burger50=Classes.Burger(211,291)

burger51=Classes.Burger(211,331)
burger52=Classes.Burger(211,331)
burger53=Classes.Burger(211,331)
burger54=Classes.Burger(211,331)
burger55=Classes.Burger(211,331)
burger56=Classes.Burger(211,331)
burger57=Classes.Burger(211,331)
burger58=Classes.Burger(211,331)
burger59=Classes.Burger(211,331)
burger60=Classes.Burger(211,331)
burger61=Classes.Burger(211,331)

burger62=Classes.Burger(211,371)
burger63=Classes.Burger(211,371)
burger64=Classes.Burger(211,371)
burger65=Classes.Burger(211,371)

burger66=Classes.Burger(211,411)
burger67=Classes.Burger(211,411)
burger68=Classes.Burger(211,411)
burger69=Classes.Burger(211,411)
burger70=Classes.Burger(211,411)
burger71=Classes.Burger(211,411)
burger72=Classes.Burger(211,411)
burger73=Classes.Burger(211,411)
burger74=Classes.Burger(211,411)
burger75=Classes.Burger(211,411)
burger76=Classes.Burger(211,411)
burger77=Classes.Burger(211,411)
burger78=Classes.Burger(211,411)
burger79=Classes.Burger(211,411)
burger80=Classes.Burger(211,411)

burger81=Classes.Burger(211,171)
burger82=Classes.Burger(211,171)
burger83=Classes.Burger(211,171)
burger84=Classes.Burger(211,171)
burger85=Classes.Burger(211,171)
burger86=Classes.Burger(211,171)
burger87=Classes.Burger(211,171)
burger88=Classes.Burger(211,171)
burger89=Classes.Burger(211,171)
burger90=Classes.Burger(211,171)
burger91=Classes.Burger(211,171)
burger92=Classes.Burger(211,171)
burger93=Classes.Burger(211,171)
burger94=Classes.Burger(211,171)
burger95=Classes.Burger(211,171)
burger96=Classes.Burger(211,171)
burger97=Classes.Burger(211,171)
burger98=Classes.Burger(211,171)
burger99=Classes.Burger(211,171)
burger100=Classes.Burger(211,171)
burger101=Classes.Burger(211,171)
burger102=Classes.Burger(211,171)
burger103=Classes.Burger(211,171)
burger104=Classes.Burger(211,171)
burger105=Classes.Burger(211,171)
burger106=Classes.Burger(211,171)
burger107=Classes.Burger(211,171)
burger108=Classes.Burger(211,171)
burger109=Classes.Burger(211,171)
burger110=Classes.Burger(211,171)
burger111=Classes.Burger(211,171)
burger112=Classes.Burger(211,171)
burger113=Classes.Burger(211,171)
burger114=Classes.Burger(211,171)
burger115=Classes.Burger(211,171)
burger116=Classes.Burger(211,171)
burger117=Classes.Burger(211,171)
burger118=Classes.Burger(211,171)
burger119=Classes.Burger(211,171)
burger120=Classes.Burger(211,171)
burger121=Classes.Burger(211,171)
burger122=Classes.Burger(211,171)

coca=Classes.Coca(89,210)
coca2=Classes.Coca(681,210)

liste_coca.add([coca,coca2])
liste_burger.add([burger,burger2,burger3,burger4,burger5,burger6,burger7,burger8,burger9,burger10,burger11,burger12,burger13,burger14,burger15,burger16,burger17, burger18, burger19, burger20,burger21,burger22,burger23,burger24,burger25,burger26,burger27,burger28,burger29,burger30,burger31,burger32,burger33,burger34,burger35,burger36,burger37,burger38,burger39,burger40,burger41,burger42,burger43,burger44,burger45,burger46,burger47,burger48,burger49,burger50,burger51,burger52,burger53,burger54,burger55,burger56,burger57,burger58,burger59,burger60,burger61,burger62,burger63,burger64,burger65,burger66,burger67,burger68,burger69,burger70,burger71,burger72,burger73,burger74,burger75,burger76,burger77,burger78,burger79,burger80,burger81,burger82,burger83,burger84,burger85,burger86,burger87,burger88,burger89,burger90,burger91,burger92,burger93,burger94,burger95,burger96,burger97,burger98,burger99,burger100,burger101,burger102,burger103,burger104,burger105,burger106,burger107,burger108,burger109,burger110,burger111,burger112,burger113,burger114,burger115,burger116,burger117, burger118, burger119, burger120,burger121,burger122])





# Record
record=open("Record.txt","r")
high_score=record.read()

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte
while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    # joueur en action
    player.health_bar(screen)
    player.update(screen)
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
        # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                player.image=pygame.image.load("Images\-NickGauche.png").convert_alpha()
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la droite
                player.image=pygame.image.load("Images\-NickDroite.png").convert_alpha()
            if event.key == pygame.K_DOWN: # on déplace le vaisseau de 1 pixel vers le bas
                player.sens = "bas"
                player.image=pygame.image.load("Images\-NickBas.png").convert_alpha()
            if event.key == pygame.K_UP: # on déplace le vaisseau de 1 pixel vers le haut
                player.sens = "haut"
                player.image=pygame.image.load("Images\-NickHaut.png").convert_alpha()

    # R.I.P
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False 
                sys.exit()
                
    # DEDICACE A LEO ROI SOLEIL ET DAN LE RACISTE
            if event.key == pygame.K_j:
                mixer.music.load("Sons\Giorno_JJBA.mp3")
                mixer.music.play()
        
    ### Actualisation de la scene ###
    # joueur
    old_x, old_y = player.rect.x, player.rect.y
    vx=player.vitesseX
    vy=player.vitesseY
    player.deplacer()
    screen.blit(player.image,player.rect) # appel de la fonction qui dessine le joueur
    # duo de vilain
    for ennemi in listeEnnemis:
        screen.blit(ennemi.image,ennemi.rect) # appel de la fonction qui dessine les ennemis
    # labyrinthe
    mur = pygame.image.load("Images\-MazeBlock.png").convert_alpha() 
    dessiner_niveau(screen, niveau, mur)
    #dessin des deux
    liste_burger.draw(screen)
    liste_coca.draw(screen)
    # burgers
                
    # cocas



    ### Collisions ###
    player.rect.x, player.rect.y, vx, vy = bloque_sur_collision1(niveau, (old_x, old_y), (player.rect.x, player.rect.y), vx, vy)
    # vilains VS murs & joueur
    sus=pygame.mixer.Sound("Sons\Vine_Boom.mp3")
    for vilain in listeEnnemis:   
        vilain.rect.x,vilain.rect.y, vi_X, vi_Y = bloque_sur_collision1(niveau,(old_x2, old_y2), (vilain.rect.x, vilain.rect.y), vi_X, vi_Y)    
        if vilain.rect.x <= player.rect.x:
            vilain.rect.x +=  vilain.vitesseX
        if vilain.rect.x >= player.rect.x:
            vilain.rect.x -= vilain.vitesseX
        if vilain.rect.y <= player.rect.y:
            vilain.rect.y += vilain.vitesseY
        if vilain.rect.y >= player.rect.y:
            vilain.rect.y -= vilain.vitesseY
        
        # Coca = Tueur de TheRock
        boire = pygame.sprite.spritecollide(player, liste_coca, True)
        for boisson in boire:
            player.etat="charge"
            boire.remove(boisson)

        if player.etat=="charge":
            vilain.image=pygame.image.load("Images\-Rock2.png").convert_alpha()
            if player.rect.colliderect(vilain.rect):
                vilain.disparaitre()
                player.score+=200
                player.compteur+=1
                
        if player.compteur>=2:   
            player.etat="normal"
            player.compteur=0  

        if player.etat=="normal":
            vilain.image=pygame.image.load("Images\-Rock.png").convert_alpha()
            if vilain.rect.colliderect(player.rect):
                sus.play()
                player.mourir()
                vilain.disparaitre()
                
    # manger       
    miam = pygame.sprite.spritecollide(player, liste_burger, True)
    for graille in miam:
        player.marquer()
        miam.remove(graille)

    ### Fin de jeu ###
    if player.health<=0:
        player.vitesseX=0
        player.vitesseY=0
        final_score=player.score

        if len(high_score)==0:
            with open("Record.txt","w") as file:
                file.write(str(final_score)) 
        else:
            if int(high_score) < player.score:
                with open("Record.txt","w") as file:
                    file.write(str(final_score))
                final_score=int(high_score)

        top_score=player.font.render(f"Record:{int(high_score)}",1,(255,195,0))
        score_fin=player.font.render(f"Score actuel:{player.score}",1,(234,31,31))
        fin_text=player.font.render(f"R.I.P Bozo, Appuie sur Echap pour en finir...",1,(255,255,255))

        screen.blit(rip_bozo,(0,0))
        rip_bozo.blit(fin_text,(222,550))
        rip_bozo.blit(score_fin,(0,150))
        rip_bozo.blit(top_score,(0,120))
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)