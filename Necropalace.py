#   Author  :   Adrien LD
#   Date    :   26/06/2019
#   Desc    :   Necropalace Game

from tkinter import*
from random import*
from tkinter import messagebox
from PIL import Image, ImageTk
from time import*

######################
#####  variables  ####
######################
H = 631
L = 981
coordonnee = []
cases = []
deplacements = [-15,-30,-14,-28,-13,-26,-1,-2,1,2,13,26,14,28,15,30]
joueur1, joueur2,tour,poss,tirer,regles,xc, yc, cx, cy, C, ep = 0,0,0,0,0,0,0,0,70,70,70,70
fichier = open("Adrien/Fichiers/informations.txt", "r")
difficulte = int(fichier.readline())
fichier.close()
affichagemenu = 0


######################
##### fonctions ######
######################
def j1ouj2():
	global joueur1, joueur2,tour
	fichier = open("Adrien/Fichiers/joueur1.txt", "r")
	joueur1 = int(fichier.readline())
	fichier.close()
	if joueur1 == 1: joueur2 = 0
	else: joueur2 = 1
	tour = joueur1
	

def coordonne(): # Permet de relever les coordonnée de chaque case
	cx = 0
	i = 0
	cy = C
	while cy < 20*C :
		cx += C
		if cx >= L :
			cy += C
			cx = C
		coordonnee.append([cx, cy])
		i += 1

def touteslesimages1():
	global imgregles, imagevitrenormale ,imagevitrecassee ,imagevitrevador ,imagevitrevador2 ,imagevitreyoda ,imagevitredeplacement ,imagevitreyoda2,imagemenu ,imagemenu2
	imgregles = PhotoImage(file = "Adrien/Images/vitres/règles.png")
	imagevitrenormale = PhotoImage(file = "Adrien/Images/vitres/Vitre1.png")
	imagevitrecassee = PhotoImage(file = "Adrien/Images/vitres/Vitre33.png")
	imagevitrevador = PhotoImage(file = "Adrien/Images/vitres/vitrevador.png")
	imagevitrevador2 = PhotoImage(file = "Adrien/Images/vitres/Image1.png")
	imagevitreyoda = PhotoImage(file = "Adrien/Images/vitres/vitreyoda.png")
	imagevitredeplacement = PhotoImage(file = "Adrien/Images/vitres/vitredeplacement.png")
	imagevitreyoda2 = PhotoImage(file = "Adrien/Images/vitres/Image2.png")   
	imagemenu = PhotoImage(file = "Adrien/Images/vitres/menu starwars2.png")
	imagemenu2 = PhotoImage(file = "Adrien/Images/vitres/menu starwars.png")   
	
def xety(i):
	x = coordonnee[i][0]
	y = coordonnee[i][1]
	return x,y

def placerjoueurs():
	can.delete(ALL)
	for i in range(0,126):
		x,y = xety(i)
		if cases[i] == [1] or cases[i] == [6]: can.create_image(x-35,y-35,image = imagevitrecassee)
		placer2(i,x,y)
	can.update()
			
def placer2(i,x,y):
	if cases[i] == [0] or cases[i] == [3] or cases[i] == [2]: can.create_image(x-35,y-35,image = imagevitrenormale)
	if cases[i] == [2]: can.create_image(x-35,y-35,image = imagevitrevador2)
	if cases[i] == [3]: can.create_image(x-35,y-35,image = imagevitreyoda2)
	elif cases[i] == [4]:
		if tour == 1 : can.create_image(x-35,y-35,image = imagevitrevador)
		else: can.create_image(x-35,y-35,image = imagevitreyoda)
	elif cases[i] == [5]: can.create_image(x-35,y-35,image = imagevitredeplacement)
	elif cases[i] == [6]: can.create_image(x-35,y-35,image = imagemenu)
	else:placermenu(i,x,y)
			
def placermenu(i,x,y):
	if affichagemenu == 1 :	affichermenu2()
	if affichagemenu == 2 :	affichermenu3()
	if affichagemenu == 3 :	affichermenu4()
	
def placerjoueursdepart(a,b):
	cases[a] = [2]
	cases[b] = [3]

def casesdepart():
	j = 0
	for i in range (0,14): cases[i] = [1]
	for i in range (0,9):
		j = 14+j
		cases[j] = [1]
		cases[j-1] = [1]
	for i in range (112,126): cases[i] = [1]
	cases[0] = [6]

def perdu():
	can.delete(ALL)
	if tour == 1: mortvador()	
	if tour == 0: mortyoda()	
	fen.destroy()
	import accueil

def perdu2(i):
	can.delete(ALL)
	if i == 1: mortvador()	
	if i == 0: mortyoda()	
	fen.destroy()
	import accueil
	
def creerdeplacementspossibles(i,choix):
	deplacement = deplacements[i]
	choix2 = choix + deplacement
	deplacement2 = deplacements[i+1]
	choix3 = choix + deplacement2
	return choix2,choix3
	
def bougerj1(choix,x,y):
	global poss
	for i in range (0,16,2):
		choix2, choix3 = creerdeplacementspossibles(i,choix)
		if cases[choix2] == [0]:
			poss = 1
			cases[choix2] = [4]
			if cases[choix3]== [0]: cases[choix3] = [4]
	if poss == 0: perdu()
		
def arreterdeplacement(choix,x,y):
	for i in range (0,16):
		deplacement = deplacements[i]
		choix2 = choix + deplacement
		if cases[choix2] == [4]:
			global poss
			poss = 0
			cases[choix2] = [0]

def actionsuite1(choix,x,y):
	global choixdepart, tour, tirer
	if cases[choix] == [2] and poss == 0:
		bougerj1(choix,x,y)
		choixdepart = choix
	if cases[choix] == [4] and poss == 1:
		arreterdeplacement(choixdepart,x,y)
		cases[choixdepart] = [1]
		bougerjoueur(choix,choixdepart)
		cases[choix] = [2]
		tour = 0
		tirer = 1

def fon_score(gagnant):
	print("rien")
	'''
	fichier = open("Adrien/Fichiers/score.txt", "r")
	score1 = int(fichier.readline(1))
	score2 = int(fichier.readline(2))
	fichier.close()
	
	score2 = score2-score1*10
	if gagnant == 1: score1 = score1+1
	else : score2 = score2+1
	fichier = open("Adrien/Fichiers/score.txt", "w")
	fichier.write(str(score1))
	fichier.write(str(score2))
	fichier.close'''

def actionsuite2(choix,x,y):
	global tour, tirer, choixdepart
	if cases[choix] == [3] and poss == 0:
		bougerj1(choix,x,y)
		choixdepart = choix
	if cases[choix] == [4] and poss == 1:
		arreterdeplacement(choixdepart,x,y)
		cases[choixdepart] = [1]
		bougerjoueur(choix,choixdepart)
		cases[choix] = [3]
		tour, tirer = 1,1

def bougerjoueur(choix,choixdepart):
	a = coordonnee[choix][0]
	b = coordonnee[choix][1]
	c = coordonnee[choixdepart][0]
	d = coordonnee[choixdepart][1]
	e = (a - c)/300
	f = (b - d)/300
	vitrecasseefon(e,f,c,d)

def action(event):
	global regles
	cx = (event.x // (C)) * C
	cy = ((event.y // (C + 1)) * C)
	choix = coordonnee.index ([cx + C, cy + C])
	x = coordonnee[choix][0]
	y = coordonnee[choix][1]
	actionpart2(x,y,choix)
	poss2 = posaprestirer(choix)
	if poss2 == 0: perdu2()
	if regles == 1: regles = 0
		
def actionpart2(x,y,choix):
	global affichagemenu
	if tour == 1 and tirer == 0 and affichagemenu == 0: actionsuite1(choix,x,y)
	elif tirer == 2 and affichagemenu == 0: effectuertir(choix)
	if tour == 0 and tirer == 0 and affichagemenu == 0: actionsuite2(choix,x,y)
	if tirer == 1 and affichagemenu == 0: tirer2(choix)
	
	if cases[choix] == [6] and affichagemenu == 0:affichagemenu = 1
	elif affichagemenu == 2:sauvegardespossibles(choix)
	elif affichagemenu == 3:chargementspossibles(choix)
	elif affichagemenu != 0:actionaffichermenu(choix)
	placerjoueurs()

def actionaffichermenu(choix):
	global affichagemenu
	if choix == 2: affichagemenu = 2
	elif choix == 3: affichagemenu = 3
	elif choix == 1: quitter()
	elif choix == 4: afficheraide()
	else : affichagemenu = 0
	
def sauvegardespossibles(choix):
	global affichagemenu
	if choix == 16 : sauvegarde(1)
	elif choix == 30 : sauvegarde(2)
	elif choix == 44 : sauvegarde(3)
	elif choix == 58 : sauvegarde(4)
	elif choix == 1 or choix == 2 or choix == 3 or choix == 4:actionaffichermenu(choix)
	else : affichagemenu = 0

def chargementspossibles(choix):
	global affichagemenu
	if choix == 17 : chargement(1)
	elif choix == 31 : chargement(2)
	elif choix == 45 : chargement(3)
	elif choix == 59 : chargement(4)
	elif choix == 1 or choix == 2 or choix == 3 or choix == 4:actionaffichermenu(choix)
	else : affichagemenu = 0

def affichermenu2():
	can.create_image(105,35,image = imagemenu2)
	can.create_image(175,35,image = imagemenu2)
	can.create_image(245,35,image = imagemenu2)
	can.create_image(315,35,image = imagemenu2)
	can.create_text(105,35, text = "Quitter", font = ("Helvetica", 13), fill = 'green')
	can.create_text(175,35, text = "Sauver", font = ("Helvetica", 13), fill = 'green')
	can.create_text(245,35, text = "Charger", font = ("Helvetica", 13), fill = 'green')
	can.create_text(315,35, text = "Aide", font = ("Helvetica", 13), fill = 'green')

def affichermenu3():
	affichermenu2()
	can.create_text(175,105, text = "Sauve.1", font = ("Helvetica", 13), fill = 'green')
	can.create_text(175,175, text = "Sauve.2", font = ("Helvetica", 13), fill = 'green')
	can.create_text(175,245, text = "Sauve.3", font = ("Helvetica", 13), fill = 'green')
	can.create_text(175,315, text = "Sauve.4", font = ("Helvetica", 13), fill = 'green')
	
def affichermenu4():
	affichermenu2()
	can.create_text(245,105, text = "Charge.1", font = ("Helvetica", 13), fill = 'green')
	can.create_text(245,175, text = "Charge.2", font = ("Helvetica", 13), fill = 'green')
	can.create_text(245,245, text = "Charge.3", font = ("Helvetica", 13), fill = 'green')
	can.create_text(245,315, text = "Charge.4", font = ("Helvetica", 13), fill = 'green')

def posaprestirer(choix):
	poss2, poss3 = 0,0
	chiffre = cases.index([2])
	chiffre2 = cases.index([3])
	for i in range(0,15,2):
		choix2 = chiffre + deplacements[i]
		choix3 = chiffre2 + deplacements[i]
		if cases[choix2] != [1] : poss2 = 1
		if cases[choix3] != [1] : poss3 = 1
	if poss2 == 0:perdu2(1)
	if poss3 == 0:perdu2(0)

def effectuertir(choix):
	if cases[choix] == [5]:
		cases[choix] = [1]
		for g in range (2,4): effectuertir2(g,choix)
		vitrecassee2(choix)
		global tirer,poss
		tirer = 0
		poss = 0
	poss2 = posaprestirer(choix)
	if poss2 == 0: perdu2()
	annoncerjoueur()
		
def annulertirv2(choix):
	for g in range (2,4): effectuertir2(g,choix)
	global tirer,poss
	tirer = 0
	poss = 0
	annoncerjoueur()
	
def effectuertir2(g,choix):
	casepion = cases.index([g])
	for i in range (0,16):
		deplacement = deplacements[i]
		choix2 = casepion + deplacement
		if cases[choix2] == [5]: cases[choix2] = [0]
		
def tirer2(choix):
	global poss,tirer
	for i in range (0,16):
		deplacement = deplacements[i]
		choix2 = choix + deplacement
		if cases[choix2] == [0]:
			cases[choix2] = [5]
			poss = 1
			tirer = 2
	if poss == 0: 
		annulertirv2(choix)
		perdu()
		tirer = 0
	
def difficultee(difficulte):
	float(difficulte)
	global casesvides
	if difficulte ==2: casesvides = 0.75
	elif difficulte == 1: casesvides = 0.80
	else: casesvides = 0.85
	
def vitrecasseefon(x,y,c,d):
	g,h = c,d
	placerjoueurs()
	c,d = vitrecassee1(x,y,c,d)
	for i in range (1,33): 
		imagevitre = PhotoImage(file = "Adrien/Images/vitres/Vitre"+str(i)+".png")
		can.create_image(g-35, h-35, image=imagevitre)
		can.update()
	if tour == 1: imagevitrecasseeenmouvementvador(x,y,c,d)
	else: imagevitrecasseeenmouvementyoda(x,y,c,d)
	can.update()

def imagevitrecasseeenmouvementyoda(x,y,c,d):
	for i in range (0,300): 
		c,d = vitrecassee1(x,y,c,d)
		vitre = can.create_image(c-35,d-35,image =imagevitreyoda2 )
		can.update()
		can.delete(vitre)
		

def imagevitrecasseeenmouvementvador(x,y,c,d):
	for i in range (0,300): 
		c,d = vitrecassee1(x,y,c,d)
		vitre = can.create_image(c-35,d-35,image =imagevitrevador2 )
		can.update()
		can.delete(vitre)
		

def annoncerjoueur():
	if tour == joueur1:
		if tour == 1: can.create_text(L/2,H/2, text = "Au tour du joueur 1", font = ("Helvetica", 42), fill = 'red')
		if tour == 0: can.create_text(L/2,H/2, text = "Au tour du joueur 1", font = ("Helvetica", 42), fill = 'green')
	if tour == joueur2:
		if tour == 1: can.create_text(L/2,H/2, text = "Au tour du joueur 2", font = ("Helvetica", 42), fill = 'red')
		if tour == 0: can.create_text(L/2,H/2, text = "Au tour du joueur 2", font = ("Helvetica", 42), fill = 'green')
	can.update()
	sleep(.8)
	placerjoueurs()
	
def annulertir(event):
	global tirer,poss
	if tirer == 2:
		for i in range (0,157):
			if cases[i] == [5]: cases[i] = [0]
		placerjoueurs()
		tirer = 0
		poss = 0
		annoncerjoueur()

def vitrecassee1(x,y,c,d):
	c = c+x
	d = d+y	
	return c,d

def vitrecassee2(choix):
	placerjoueurs()
	x = coordonnee[choix][0]
	y = coordonnee[choix][1]
	for i in range (1,33):
		imagevitre = PhotoImage(file = "Adrien/Images/vitres/Vitre"+str(i)+".png")
		can.create_image(x-35, y-35, image=imagevitre)
		can.update()
		sleep(.01)

def ouvririmage2(i):
	global p2
	can.delete(ALL)
	fime = "Adrien/Images/GIF/frame_0"+str(i)+"_delay-0.04s.gif"
	imageparametres = Image.open(fime)
	pn2 = ImageTk.PhotoImage(imageparametres)
	can.create_image(L/2, H/2, image=pn2) 
	can.update()
	sleep(.02)

def gifquitter():
	for i in range(30,80): ouvririmage2(i)
			
def quitter(): 
	if messagebox.askyesno("Validation", "Etes vous sûrs de vouloir quitter?"):
		gifquitter()
		fen.destroy()
		import accueil


def sauvegarde(e):
	global affichagemenu
	fichier = open("Adrien/Fichiers/Sauvegarde"+str(e)+".txt", "w")
	for i in range(0,157): fichier.write(str(cases[i]))
	fichier.close()
	messagebox.showinfo('Sauvegarde efféctuée', 'Sauvegarde '+str(e)+' éffectuée')
	affichagemenu = 0
	placerjoueurs()

def chargement(i):
	global cases, affichagemenu
	cases = []
	fichier = open("Adrien/Fichiers/Sauvegarde"+str(i)+".txt", "r")
	casestemp = str(fichier.readline())
	for i in range(1,400,3): cases.append([int(casestemp[i])])
	fichier.close()
	affichagemenu = 0
	placerjoueurs()

def sauveretquitter():
	sauvegarde(1)
	quitter()

def afficheraide1():													#Affiche les règles du jeu
	while regles == 1:
		global imgregles
		can.create_image(L/2, H/2, image=imgregles) 
		can.update()
		sleep(.1)
	placerjoueurs()

def afficheraide():														#Crée un variable qui permet d'afficher les règles du jeu
	global regles
	regles = 1
	afficheraide1()

def mortvador():
	for i in range (44,98):
		imageparametres = Image.open("Adrien/Images/GIF2/frame_"+str(i)+"_delay-0.04s.gif")
		pn2 = ImageTk.PhotoImage(imageparametres)
		can.create_image(L/2, H/2, image=pn2)
		can.update()
		sleep(.04)
		
def mortyoda():
	for i in range(0,10): mortyoda2(i)
	for i in range(10,100): mortyoda2(i)
	for i in range(100,156): mortyoda2(i)

def mortyoda2(i):
	global pn2
	if i<10: fime = "Adrien/Images/GIF2/frame_00"+str(i)+"_delay-0.05s.gif"
	elif i<100: fime = "Adrien/Images/GIF2/frame_0"+str(i)+"_delay-0.05s.gif"
	else: fime = "Adrien/Images/GIF2/frame_"+str(i)+"_delay-0.05s.gif"
	imageparametres = Image.open(fime)
	pn2 = ImageTk.PhotoImage(imageparametres) 
	can.create_image(L/2, H/2, image=pn2)
	can.update()
	sleep(.01)

def imagebombe(event):
	global cases
	imagebombe3()
	for i in range (8,155):
		if cases[i]==[0] or cases[i]==[4] or cases[i]==[5]: cases[i]=[1]
	placerjoueurs()

def imagebombe3():
	for i in range(0,9): ouvririmage(i)
	for i in range(10,99): ouvririmage(i)
	for i in range(100,146): ouvririmage(i)	
		
def ouvririmage(i):
	can.delete(ALL)
	if i<10: frame = "Adrien/Images/GIF/frame_00"+str(i)+"_bombe.gif"
	elif i<100: frame = "Adrien/Images/GIF/frame_0"+str(i)+"_bombe.gif"
	else: frame = "Adrien/Images/GIF/frame_"+str(i)+"_bombe.gif"
	imagebombe2 = Image.open(frame)
	imagebombe2 = ImageTk.PhotoImage(imagebombe2) 
	creerimage2(imagebombe2)
	can.update()
		
def creerimage2(imagebombe2):
	for f in range (100,1000,360):
		for i in range (150,1000,360):
			can.create_image(i, f, image=imagebombe2)

def depart():
	coordonne()
	difficultee(difficulte)
	for i in range (0,157):
		d = random()
		if d>casesvides:
			cases.append([1])
		else :
			cases.append([0])
	depart2()
	
def depart2():
	placerjoueursdepart(59,66)
	j1ouj2()
	casesdepart()
	fon_score(1)
	touteslesimages1()
	placerjoueurs()
	annoncerjoueur()


#######################
##programme principal##
#######################
fen = Tk()
fen.title("Necropalace")
can = Canvas(fen, width = L, height = H)
can.pack(side = LEFT, padx = 0, pady = 0)
windowWidth = fen.winfo_reqwidth()
windowHeight = fen.winfo_reqheight()
positionRight = int(fen.winfo_screenwidth()/6 - windowWidth/6)
positionDown = int(fen.winfo_screenheight()/8 - windowHeight/8)
fen.geometry("+{}+{}".format(positionRight, positionDown))

depart()

######################
###### bouttons ######
######################
can.bind("<Button-1>",action)
can.bind("<Button-3>",annulertir)
can.bind_all('<KeyPress-Up>',imagebombe)
fen.mainloop()
