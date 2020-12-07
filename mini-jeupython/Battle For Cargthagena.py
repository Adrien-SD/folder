import pygame
from pygame.locals import *
from time import *

pygame.init()

def explosion(xex,yex):
    global t1,explo,yexplo,xexplo
    t1=time()
    explo=1
    xexplo=xex
    yexplo=yex

def tirforteresseQ(ballerectQ):
    #permet de tirer un boulet lors de l'appuie de la touche Q,le boulet enlève un PV dans la variable vieb lorsqu'il touche le bateau.
    #xfq,yfq sont les coordonnés du boulet,tirfq est la variable pour qu'un seul tir par un soit effectué par la touche Q.

    global xfq,yfq,tirfq,x,y,vieb
    bateaurect=bateau.get_rect(topleft=(x,y))

    if tirfq==1: #tir d'un boulet
        yfq-=(4/hauteur)*ballerectQ.top+2.5
        ballerectQ = balleQ.get_rect(topleft=(xfq,yfq))

    if ballerectQ.top<=0: #le boulet n'a rien touché
        tirfq=0
        ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerectQ.top<=bateaurect.bottom and ballerectQ.right>bateaurect.left and ballerectQ.left<bateaurect.right: #le boulet à touché
        tirfq=0
        vieb-=1
        explosion(xfq,yfq)     #Provoquer une explosion
        ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))

    return ballerectQ


def tirforteresseS(ballerectS):
    #permet de tirer un boulet lors de l'appuie de la touche S,le boulet enlève un PV dans la variable vieb lorsqu'il touche le bateau.
    #xfs,yfs sont les coordonnés du boulet,tirfs est la variable pour qu'un seul tir par un soit effectué par la touche S.

    global xfs,yfs,tirfs,x,y,vieb
    bateaurect=bateau.get_rect(topleft=(x,y))

    if tirfs==1: #tir d'un boulet
        yfs-=(4/hauteur)*ballerectS.top+2.5
        ballerectS = balleS.get_rect(topleft=(xfs,yfs))

    if ballerectS.top<=0: #le boulet n'a rien touché
        tirfs=0
        ballerectS = balleS.get_rect(topleft=((largeur2+2000),hauteur2))

    if ballerectS.top<=bateaurect.bottom and ballerectS.right>bateaurect.left and ballerectS.left<bateaurect.right: #le boulet à touché
        tirfs=0
        vieb-=1
        explosion(xfs,yfs)     #Provoquer une explosion
        ballerectS = balleS.get_rect(topleft=((largeur2+2000),hauteur2))

    return ballerectS

def tirforteresseD(ballerectD):
    #permet de tirer un boulet lors de l'appuie de la touche D,le boulet enlève un PV dans la variable vieb lorsqu'il touche le bateau.
    #xfd,yfd sont les coordonnés du boulet,tirfd est la variable pour qu'un seul tir par un soit effectué par la touche D.

    global xfd,yfd,tirfd,x,y,vieb
    bateaurect=bateau.get_rect(topleft=(x,y))

    if tirfd==1: #tir d'un boulet
        yfd-=(4/hauteur)*ballerectD.top+2.5
        ballerectD = balleD.get_rect(topleft=(xfd,yfd))

    if ballerectD.top<=0: #le boulet n'a rien touché
        tirfd=0
        ballerectD = balleD.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerectD.top<=bateaurect.bottom and ballerectD.right>bateaurect.left and ballerectD.left<bateaurect.right: #le boulet à touché
        tirfd=0
        vieb-=1
        explosion(xfd,yfd)     #Provoquer une explosion
        ballerectD= balleD.get_rect(topleft=(largeur2+2000,hauteur2))

    return ballerectD

def tirforteresseF(ballerectF):
    #permet de tirer un boulet lors de l'appuie de la touche F,le boulet enlève un PV dans la variable vieb lorsqu'il touche le bateau.
    #xff,yff sont les coordonnés du boulet,tirff est la variable pour qu'un seul tir par un soit effectué par la touche F.

    global xff,yff,tirff,x,y,vieb
    bateaurect=bateau.get_rect(topleft=(x,y))

    if tirff==1: #tir d'un boulet
        yff-=(4/hauteur)*ballerectF.top+2.5
        ballerectF= balleF.get_rect(topleft=(xff,yff))

    if ballerectF.top<=0: #le boulet n'a rien touché
        tirff=0
        ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerectF.top<=bateaurect.bottom and ballerectF.right>bateaurect.left and ballerectF.left<bateaurect.right: #le boulet à touché
        tirff=0
        vieb-=1
        explosion(xff,yff)     #Provoquer une explosion
        ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))

    return ballerectF

def tirnavire1(ballerect):
    #permet de tirer un boulet lors de l'appuie de la touche DOWN,le boulet enlève un PV dans la variable vief lorsqu'il touche la forteresse.
    #x1,y1 sont les coordonnés du boulet,tirb1 est la variable pour qu'un seul tir par un soit effectué par la touche DOWN.
    #direction est la variable pour que le boulet n'aquière la direction en fonction de vx 1 seul fois.
    #recharge permet de tirer 2 boulet sur la même touche et est à réinitialiser.

    global x,vx,tirb1,y1,x1,vief,direction,x2,recharge

    if ballerect.left<=410 and ballerect.right >310 and ballerect.bottom > 482 : #le boulet à touché
        vief-=1
        tirb1-=1
        direction=0
        recharge=0
        explosion(x1+70,y1+70)     #Provoquer une explosion
        ballerect = balle.get_rect(topleft=(x+50,y+50))

    if ballerect.left<=665 and ballerect.right >580 and ballerect.bottom > 477 : #le boulet à touché
        vief-=1
        tirb1-=1
        direction=0
        recharge=0
        explosion(x1+70,y1+70)     #Provoquer une explosion
        ballerect = balle.get_rect(topleft=(x+50,y+50))

    if tirb1==1: #tir d'un boulet
        ballerect = balle.get_rect(topleft=(x1+50,y1+50))
        y1+=-(5.5/hauteur)*ballerect.bottom+8
        if direction==0:
            if vx>0:x2= ((-4/(2*hauteur))*ballerect.left)+4 #x2 prend la valeur de la trajectoire à incrémenter dans x1
            else:x2= ((4/(2*hauteur))*ballerect.right)-4
            direction=1
        x1+=x2
        fenetre.blit(balle,(ballerect))

    if ballerect.top < 0 or ballerect.bottom > hauteur: #le boulet n'a rien touché
        tirb1-=1
        ballerect = balle.get_rect(topleft=(x+50,y+50))
        direction=0
        recharge=0

    return ballerect

def tirnavire2(ballerect2):
    #permet de tirer un boulet lors de l'appuie de la touche DOWN,le boulet enlève un PV dans la variable vief lorsqu'il touche la forteresse.
    #xn2,yn2 sont les coordonnés du boulet,tirb2 est la variable pour qu'un seul tir par un soit effectué par la touche DOWN.
    #direction2 est la variable pour que le boulet n'aquière la direction en fonction de vx 1 seul fois.
    #recharge permet de tirer 2 boulet sur la même touche et est à réinitialiser.

    global x,vx,tirb2,yn2,xn2,vief,direction2,x3,recharge

    if ballerect2.left<=410 and ballerect2.right >310 and ballerect2.bottom > 482 : #le boulet à touché
        vief-=1
        tirb2-=1
        direction2=0
        recharge=0
        explosion(xn2+70,yn2+70)     #Provoquer une explosion
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))

    if ballerect2.left<=665 and ballerect2.right >580 and ballerect2.bottom > 477 : #le boulet à touché
        vief-=1
        tirb2-=1
        recharge=0
        direction2=0
        explosion(xn2+70,yn2+70)     #Provoquer une explosion
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))

    if tirb2==1: #tir d'un boulet
        ballerect2 = balle.get_rect(topleft=(xn2+50,yn2+50))
        yn2+=-(5.5/hauteur)*ballerect2.bottom+8
        if direction2==0:
            if vx>0:x3= ((-4/(2*hauteur))*ballerect2.left)+4 #x3 prend la valeur de la trajectoire à incrémenter dans xn2
            else:x3= ((4/(2*hauteur))*ballerect2.right)-4
            direction2=1
        xn2+=x3
        fenetre.blit(balle2,(ballerect2))

    if ballerect2.top < 0 or ballerect2.bottom > hauteur: #le boulet n'a rien touché
        tirb2-=1
        recharge=0
        direction2=0
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
    return ballerect2

def contactboulet():
    #permet de détruire les boulets entre-eux en fonction de leur coordonné
    #remet à zéro les variables de tir, de direction et de recharge

    global tirb1,tirb2,ballerect,ballerect2,ballerectQ,ballerectS,ballerectD,ballerectF,tirfq,tirff,tirfs,tirfd,recharge,direction,direction2

    if ballerect.left<=ballerectQ.right and ballerect.right>ballerectQ.left and ballerect.bottom > ballerectQ.top and ballerect.top<ballerectQ.bottom:
        tirb1=0
        tirfq=0
        recharge=0
        direction=0
        ballerect = balle.get_rect(topleft=(x+50,y+50))
        ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect.left<=ballerectS.right and ballerect.right>ballerectS.left and ballerect.bottom > ballerectS.top and ballerect.top<ballerectS.bottom:
        tirb1=0
        tirfs=0
        recharge=0
        direction=0
        ballerect = balle.get_rect(topleft=(x+50,y+50))
        ballerectS = balleS.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect.left<=ballerectD.right and ballerect.right>ballerectD.left and ballerect.bottom > ballerectD.top and ballerect.top<ballerectD.bottom:
        tirb1=0
        tirfd=0
        recharge=0
        direction=0
        ballerect = balle.get_rect(topleft=(x+50,y+50))
        ballerectD = balleD.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect.left<=ballerectF.right and ballerect.right>ballerectF.left and ballerect.bottom > ballerectF.top and ballerect.top<ballerectF.bottom:
        tirb1=0
        tirff=0
        recharge=0
        direction=0
        ballerect = balle.get_rect(topleft=(x+50,y+50))
        ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect2.left<=ballerectQ.right and ballerect2.right>ballerectQ.left and ballerect2.bottom > ballerectQ.top and ballerect2.top<ballerectQ.bottom:
        tirb2=0
        tirfq=0
        recharge=0
        direction2=0
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
        ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect2.left<=ballerectS.right and ballerect2.right>ballerectS.left and ballerect2.bottom > ballerectS.top and ballerect2.top<ballerectS.bottom:
        tirb2=0
        tirfs=0
        recharge=0
        direction2=0
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
        ballerectS = balleS.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect2.left<=ballerectD.right and ballerect2.right>ballerectD.left and ballerect2.bottom > ballerectD.top and ballerect2.top<ballerectD.bottom:
        tirb2=0
        tirfd=0
        recharge=0
        direction2=0
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
        ballerectD = balleD.get_rect(topleft=(largeur2+2000,hauteur2))

    if ballerect2.left<=ballerectF.right and ballerect2.right>ballerectF.left and ballerect2.bottom > ballerectF.top and ballerect2.top<ballerectF.bottom:
        tirb2=0
        tirff=0
        recharge=0
        direction2=0
        ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
        ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))



def deplace_bateau():
    #permet de changer de direction le bateau

    global x,vx
    if x>=900 or x<=0:
        vx= -(vx)
    x+=vx


def ecrant():
    #permet d'afficher un écran titre animé
    #sonecrant permet de lancer la musique une seul fois

    global sonecrant

    if sonecrant==1: #lance la musique
        sonmer = pygame.mixer.music.load("sonmer.mp3")
        pygame.mixer.music.play()
        sonecrant=0

    fenetre.fill(0)
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fond2,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fond3,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fond4,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)


def commande():
    #permet d'afficher un écran commande animé

    fenetre.blit(fondc1,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fondc2,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fondc3,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)
    fenetre.blit(fondc4,(0,0))
    pygame.display.flip()
    pygame.time.delay(250)

def jouer():
    #permet d'afficher tous les boulets et le bateau,sonjouer permet de charger une seule fois la musique
    #coupb et coupf affiche le nombre de PV de la forteresse et du bateau
    #relie toutes les fonctions tirs

    global ballerect,ballerect2,ballerectD,ballerectF,ballerectQ,ballerectS,vx,vieb,vief,joue,win,sonjouer,coupb,coupf,explo

    if sonjouer==1: #lance la musique
        sonmer = pygame.mixer.music.load("soncombat.mp3")
        pygame.mixer.music.play()
        sonjouer=0

    coupf = myfont1.render("PV Forteresse : "+str(vief),1, Color("RED")) #affiche le nombre de PV restants
    coupb = myfont1.render("PV Navire : "+str(vieb),1, Color("RED"))

    fenetre.fill(0)
    fenetre.blit(fondcom,(0,0))

    deplace_bateau()
    contactboulet()

    ballerect=tirnavire1(ballerect)
    ballerect2=tirnavire2(ballerect2)
    ballerectQ=tirforteresseQ(ballerectQ)
    ballerectS=tirforteresseS(ballerectS)
    ballerectD=tirforteresseD(ballerectD)
    ballerectF=tirforteresseF(ballerectF)

    fenetre.blit(balleQ,(ballerectQ))
    fenetre.blit(balleS,(ballerectS))
    fenetre.blit(balleD,(ballerectD))
    fenetre.blit(balleF,(ballerectF))

    if vx>=0:
        fenetre.blit(bateaudroit, (x,y))
    if vx<=0:
        fenetre.blit(bateaugauche, (x,y))

    if explo==1:
        t=time()
        if t<t1+0.3:
            fenetre.blit(boom, (xexplo-50,yexplo-50))
        else :
            explo=0

    fenetre.blit(coupf, (1015, 150))
    fenetre.blit(coupb,(1035,250))

    if vieb==0 or vief==0:
        joue=0
        win=1

    pygame.display.flip()

def Win():
    #permet d'afficher un écran de fin animé en fonction du gagnant

    global vieb,vief
    fenetre.fill(0)
    if vieb==0:
        fenetre.blit(fondfw1,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondfw2,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondfw3,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondfw4,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)

    if vief==0:
        fenetre.blit(fondnw1,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondnw2,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondnw3,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)
        fenetre.blit(fondnw4,(0,0))
        pygame.display.flip()
        pygame.time.delay(250)

def recommencer():
    #remet à zéro toutes les variables
    global ballerect,ballerect2,ballerectQ,ballerectS,ballerectD,ballerectF,coupb,coupf,tirb1,tirb2,tirfq,tirff,tirfs,tirfd,vieb,vief,recharge,sonjouer,sonecrant,joue,recommence

    ballerect = balle.get_rect(topleft=(x+50,y+50))
    ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
    ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))
    ballerectS = balleS.get_rect(topleft=(largeur2+2000,hauteur2))
    ballerectD = balleD.get_rect(topleft=(largeur2+2000,hauteur2))
    ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))

    tirb1,tirb2,tirfq,tirff,tirfs,tirfd=0,0,0,0,0,0

    vieb,vief=5,8
    recharge,sonjouer,sonecrant=0,1,1

    recommence=0
    joue=1

def jeu():
    #relie toutes les fonctions entre-elles
    global ecran,command,joue,win,recommence,sonecrant,sonjouer
    if ecran==1:
        ecrant()
    if command==1:
        commande()
    if joue==1:
        jouer()
    if win==1:
        Win()
    if recommence==1:
        recommencer()

#Programme principal
noir=0,0,0
pygame.display.set_caption("Battle for Carthagena")
taille = largeur, hauteur = 1200, 519
fenetre = pygame.display.set_mode(taille)

#explosion
boom = pygame.image.load("explosion.png").convert_alpha()
boom = pygame.transform.scale(boom,(100,75))
explo=0

#ecrant
sonecrant=1
fond= pygame.image.load("ecrant1.png").convert()
font=pygame.transform.scale(fond,taille)


fond2= pygame.image.load("ecrant2.png").convert()
fond2=pygame.transform.scale(fond2,taille)


fond3= pygame.image.load("ecrant3.png").convert()
fond3=pygame.transform.scale(fond3,taille)

fond4= pygame.image.load("ecrant4.png").convert()
fond4=pygame.transform.scale(fond4,taille)


#commande
fondc1= pygame.image.load("ecranc1.png")
fondc1=pygame.transform.scale(fondc1,taille)

fondc2= pygame.image.load("ecranc2.png")
fondc2=pygame.transform.scale(fondc2,taille)

fondc3= pygame.image.load("ecranc3.png")
fondc3=pygame.transform.scale(fondc3,taille)

fondc4= pygame.image.load("ecranc4.png")
fondc4=pygame.transform.scale(fondc4,taille)

#jouer
fondcom = pygame.image.load("fondjeu.png")
fondcom = pygame.transform.scale(fondcom,taille)

#Win
fondnw1 = pygame.image.load("fondnw1-1.png")
fondnw1 = pygame.transform.scale(fondnw1,taille)

fondnw2 = pygame.image.load("fondnw1-2.png")
fondnw2 = pygame.transform.scale(fondnw2,taille)

fondnw3 = pygame.image.load("fondnw1-3.png")
fondnw3 = pygame.transform.scale(fondnw3,taille)

fondnw4 = pygame.image.load("fondnw1-4.png")
fondnw4 = pygame.transform.scale(fondnw4,taille)

fondfw1 = pygame.image.load("fondfw1-1.png")
fondfw1 = pygame.transform.scale(fondfw1,taille)

fondfw2 = pygame.image.load("fondfw1-2.png")
fondfw2 = pygame.transform.scale(fondfw2,taille)

fondfw3 = pygame.image.load("fondfw1-3.png")
fondfw3 = pygame.transform.scale(fondfw3,taille)

fondfw4 = pygame.image.load("fondfw1-4.png")
fondfw4 = pygame.transform.scale(fondfw4,taille)

#combat
sonjouer=1
direction,direction2=0,0
x2,x3=0,0
tirb1,tirb2,vieb=0,0,5
vief,tirfq,tirfs,tirfd,tirff=8,0,0,0,0
x,y=240,0
largeur2,hauteur2=50,379
vx=5
xfs,yfs,xf,yf=0,0,0,0
recharge=0

balle = pygame.image.load("ball.png").convert()

balle2 = pygame.image.load("ball.png").convert()

balleQ = pygame.image.load("balle.png").convert()

balleS = pygame.image.load("balle.png").convert()

balleD = pygame.image.load("balle.png").convert()

balleF = pygame.image.load("balle.png").convert()

bateau = pygame.image.load("bateau_left.png").convert_alpha()
bateau=pygame.transform.scale(bateau,(125,100))

bateaugauche = pygame.image.load("bateau_left.png").convert_alpha()
bateaugauche=pygame.transform.scale(bateaugauche,(125,100))

bateaudroit = pygame.image.load("bateau_right.png").convert_alpha()
bateaudroit=pygame.transform.scale(bateaudroit,(125,100))


myfont1 = pygame.font.SysFont("august", 30)
coupf = myfont1.render("PV Forteresse : "+str(vief),1, Color("RED"))

myfont2 = pygame.font.SysFont("august", 30)
coupb = myfont1.render("PV Navire : "+str(vieb),1, Color("RED"))

#Création des hitbox
bateaurect=bateau.get_rect(topleft=(x,y))
bateaurectg=bateaugauche.get_rect(topleft=(x,y))
bateaurectd=bateaudroit.get_rect(topleft=(x,y))


ballerect = balle.get_rect(topleft=(x+50,y+50))
ballerect2 = balle2.get_rect(topleft=(x+50,y+50))
ballerectQ = balleQ.get_rect(topleft=(largeur2+2000,hauteur2))
ballerectS = balleS.get_rect(topleft=((largeur2+2000),hauteur2))
ballerectD = balleD.get_rect(topleft=(largeur2+2000,hauteur2))
ballerectF = balleF.get_rect(topleft=(largeur2+2000,hauteur2))


#bouton jouer
clickable_jeu = pygame.Rect((410,216),(350,100))  #coordonnée(200, 200),dimension (200,100)

#bouton commande
clickable_commande = pygame.Rect((860,297),(295,80))  #coordonnée(200, 200),dimension (200,100)

#bouton quitter
clickable_quitter = pygame.Rect((847,392),(320,100))  #coordonnée(200, 200),dimension (200,100)
clickable_quitter2 = pygame.Rect((468,380),(330,98))

#bouton retour
clickable_retour1 = pygame.Rect((710,362),(410,120))
clickable_retour2 = pygame.Rect((1020,430),(160,56))

#bouton recommencer
clickable_recommencer = pygame.Rect((465,236),(330,98))

continuer=1
ecran=1
command=0
joue=0
win=0
recommence=0
while continuer:
    jeu()
    pygame.time.Clock().tick(300)
    for event in pygame.event.get():
        if event.type==KEYDOWN: #assignement de touche

            if event.key == K_ESCAPE:
                continuer = 0
            if joue==1:
                if event.key==K_RIGHT : vx=5

                elif event.key==K_LEFT : vx= -5

                elif event.key == K_DOWN:
                    if tirb1!=1:
                        x1=x
                        y1=y
                    tirb1=1
                    recharge+=1
                    if recharge==2:
                        if tirb2!=1:
                            xn2=x         #acquisitions de la position du bateau au tir
                            yn2=y
                        tirb2=1

                elif event.key==K_a:                            #querty/azerty bug
                    if tirfq!=1:
                        xfq=largeur2+245
                        yfq=hauteur2
                    tirfq=1

                elif event.key==K_s:
                    if tirfs!=1:
                        xfs=largeur2+335
                        yfs=hauteur2
                    tirfs=1

                elif event.key==K_d:
                    if tirfd!=1:
                        xfd=largeur2+533
                        yfd=hauteur2
                    tirfd=1

                elif event.key==K_f:
                    if tirff!=1:
                        xff=largeur2+619
                        yff=hauteur2
                    tirff=1


        elif event.type == QUIT:  continuer = 0


        elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
            if event.button == 1: # 1= clique gauche
                if ecran==1:
                    if clickable_jeu.collidepoint(event.pos): #zone cliquable
                        joue=1
                        sonjouer=1
                        ecran=0

                    if clickable_commande.collidepoint(event.pos):
                        command=1
                        ecran=0

                    if clickable_quitter.collidepoint(event.pos):
                        continuer=0
                if command==1:
                    if clickable_retour1.collidepoint(event.pos):
                        ecran=1
                        command=0
                if joue==1:
                    if clickable_retour2.collidepoint(event.pos):
                        ecran=1
                        sonecrant=1
                        joue=0
                if win==1:
                    if clickable_quitter2.collidepoint(event.pos):
                        continuer=0
                    if clickable_recommencer.collidepoint(event.pos):
                        win=0
                        recommence=1
                        print(recommence)
    pygame.display.flip()



pygame.quit()