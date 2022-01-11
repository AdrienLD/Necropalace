#   Author  :   Nolwen / Lionel / Adrien LD
#   Date    :   26/06/2019
#   Desc    :   Home Page

from tkinter import*
from PIL import Image, ImageTk
from time import*

L = 1024
H = 576

fen = Tk()
can = Canvas(fen, width =L , height =H , background = 'black')
can.pack(padx = 0, pady = 0)
liste = [0,0]
fenetre = 3
difficulte = 1
difficulteString = " "
fautcomparer = 0
J1,J2 = 3,3
liste_ppc = ["Les ciseaux sont cassés par la pierre","La pierre est recouverte par le papier","Le papier est coupé par les ciseaux", "Egalité"]
liste_coul = ['black','red','blue']
comptage_points_ppc = 0

def action(event):
	x = event.x
	y = event.y
	if fenetre == 0: fenetre0(x,y)
	elif fenetre == 1: fenetre1(x,y)
	elif fenetre == 2: fenetre2(x,y)
	elif fenetre == 3: fenetre3(x,y)
	fon_score()

def fenetre0(x,y):
	if 723>x>304 and 353>y>228: creer_can3()
	elif 1000>x>636 and 548>y>500: creer_can2()
	elif 244>x>19 and 554>y>494: creer_can4()

def fenetre1(x,y):
	if 647>x>376 and 534>y>474: creer_can()
	elif 845>x>620 and 311>y>264: changerdifficulte(0,264,311)
	elif 845>x>620 and 368>y>321: changerdifficulte(1,321,368)
	elif 845>x>620 and 425>y>378: changerdifficulte(2,378,425)

def fenetre2(x,y):
	fichier = open("Adrien/Fichiers/joueur1.txt", "w")
	if x>L/2: fichier.write("0")
	else: fichier.write("1")
	fichier.close()
	can.update()
	fen.destroy()
	import Necropalace

def fenetre3(x,y):
	if 0<x<500 and 190<y<290: creer_can6()
	if 510<x<1010 and 225<y<325: creer_can7()
	if 0<x<500 and 310<y<410:creer_can5()
	if 510<x<1010 and 360<y<460:creer_can()
	if 0<x<500 and 455<y<555: print("Indisponnible pour le moment")
	if 820<x<1020 and 500<y<565: fen.destroy()

def changerdifficulte(valeur,y1,y2):
	global difficulte
	can.create_line(620,264,620,311,845,311,845,264,620,264, width = 3, fill = 'black')
	can.create_line(620,321,620,368,845,368,845,321,620,321, width = 3, fill = 'black')
	can.create_line(620,378,620,425,845,425,845,378,620,378, width = 3, fill = 'black')
	can.create_line(620,y1,620,y2,845,y2,845,y1,620,y1, width = 3, fill = 'red')
	difficulte = valeur

def creer_can7():
	fen.destroy()
	import jeux_loi

def creer_can6():
	fen.destroy()
	import Echecs

def creer_can5():
	global fond, fenetre
	can.delete(ALL)
	fen.title("Pierre Papier Ciseaux")
	fond = PhotoImage(file = "Lionel/Images/plato_ppc.png")
	can.create_image((L/2)+2, (H/2)+2, image=fond)
	can.update()

	fenetre = 4

def creer_can4():
	global fond, fenetre
	can.delete(ALL)
	fen.title("Plateforme de Jeux")
	fond = PhotoImage(file = "Lionel/Images/menu2.png")
	can.create_image((L/2)+2, (H/2)+2, image=fond)
	can.update()
	fenetre = 3

def fon_score():
	fichier = open("Adrien/Fichiers/score.txt", "w")
	fichier.write(str("01"))
	fichier.close()

def creer_can3():
	global fond, fenetre
	can.delete(ALL)
	fen.title("Choisir Joueur")
	fond = PhotoImage(file = "Adrien/Images/vitres/Joueur1.png")
	can.create_image(L/2, (H/2)+(H/15), image=fond)
	can.update()
	fenetre = 2

def creer_can2():
	global fond, fenetre
	can.delete(ALL)
	fen.title("Paramètres")
	fond = PhotoImage(file = "Adrien/Images/autres/paramètresvf2.png")
	can.create_image(514, 290, image=fond)
	can.update()
	fenetre = 1

def creer_can():
	global fond, fenetre
	can.delete(ALL)
	fen.title("Accueil")
	fond = PhotoImage(file = "Adrien/Images/autres/accueilvf.png")
	can.create_image(514, 290, image=fond)
	fenetre = 0
	can.update()
	ouverturefichier()
	
def ouverturefichier():
	difficulteString = str(difficulte)
	fichier = open("Adrien/Fichiers/informations.txt", "w")
	fichier.write(difficulteString)
	fichier.close()
	
def jeu1(event):
	global J1, fautcomparer
	if fenetre == 4:
		if event.char == "a": J1 = 0
		if event.char == "z": J1 = 1
		if event.char == "e": J1 = 2
		if J2!=3: comparaison(J1,J2)

def jeu2(event):
	global J2, fautcomparer
	if fenetre == 4:
		if event.char == "1": J2 = 0
		if event.char == "2": J2 = 1
		if event.char == "3": J2 = 2
		if J1!=3: comparaison(J1,J2)
		
def comparaison(C1, C2):
	if C1 == C2 : inscrireresultat(3,0)
	elif C1 == 0:
		if C2 == 1: inscrireresultat(1,2)
		elif C2 == 2: inscrireresultat(0,1)
	elif C1 == 1:
		if C2 == 0: inscrireresultat(1,1)
		elif C2 == 2: inscrireresultat(2,2)
	elif C1 == 2:
		if C2 == 0: inscrireresultat(1,1)
		elif C2 == 1: inscrireresultat(2,2)

def inscrireresultat(a,b):
	global Imageachoisir,J1,J2
	J1,J2 = 3,3
	can.delete(ALL)
	creer_can5()
	can.create_text(L/2,H/1.5, text = str(liste_ppc[a]), font = ("Helvetica", 42), fill = liste_coul[b])
	Imageachoisir = PhotoImage(file = "Lionel/Images/Image_"+str(a)+".png")
	can.create_image(L/2, H/2, image = Imageachoisir)
	repartirpoints(a,b)
	can.update()

def repartirpoints(a,b):
	global comptage_points_ppc
	if a != 3:
		comptage_points_ppc = comptage_points_ppc+1
		
	if comptage_points_ppc == 5:
		creer_can4()

creer_can4()
can.bind_all("<KeyPress-a>", jeu1)
can.bind_all("<KeyPress-z>", jeu1)
can.bind_all("<KeyPress-e>", jeu1)
can.bind_all("<KeyPress-1>", jeu2)
can.bind_all("<KeyPress-2>", jeu2)
can.bind_all("<KeyPress-3>", jeu2)

can.bind("<Button-1>",action)
fen.mainloop()

