#   Author  :   Nolwen
#   Date    :   26/06/2019
#   Desc    :   Chess Game

from tkinter import*
from tkinter import messagebox
import sys

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

H = 700
C = H / 8
coord = []
j = 0
listv = [0]
listt = [0]
save1 = [[]]
turn = 0
t = 0
temp = 0
echec_continu = 0
coul = 0
trouver = 0
fin = 0
echec_save = 0

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def prepin(a, b, d):
	listp = [pn, pb, tn, tb, cn, cb, fn, fb, ren, reb, ron, rob]
	if coord[c][4] == a and coord[c][5] == b :							#a determine la piece et b determine la couleur (1 pour noir et 2 pour blanc)
		x = coord[c][0]+C/2
		y = coord[c][1]+C/2
		can.create_image(x, y, image=listp[d])

def pin():
	#Creation des pieces et liste de toutes les pieces possibles
	global c
	c = 0
	k = 0
	while c < 64:
		for i in range(1, 7):
			prepin(i, 1, k)														#k va permettre d'assigner l'image à une pièce et i, la pièce
			k += 1
			prepin(i, 2, k)
			k += 1
		c += 1
		k = 0

def rondjaune():
	#Met un rond jaune quand on peut se deplacer sur une cazse
	for h in range(0, 64):
		x0 = coord[h][0] + C/3.5
		y0 = coord[h][1] + C/3.5
		x = coord[h][2] - C/3.5
		y = coord[h][3] - C/3.5
		if coord[h][7] == 1:
			can.create_oval(x0, y0, x, y, fill = 'yellow')
		if coord[h][9] == 1:
			can.create_rectangle(x0 - C/3.5, y0 - C/3.5, x + C/3.5, y + C/3.5, outline = 'red', width=1)

def cases():
		#Creation des cases de l'echequier et des pieces initialles
	#Creation de l'echequier
	k = 0
	coul = 1
	for l in range(0,8):
		for m in range(0, 8):
			x0 = coord[k][0]
			y0 = coord[k][1]
			x = coord[k][2]
			y = coord[k][3]
			k += 1
			if coul == 0:
				if k % 2 ==0:
					can.create_rectangle(x0, y0, x, y, fill = '#FFE8AF')
				else:
					can.create_rectangle(x0, y0, x, y, fill = '#8B6914')
			else:
				if k % 2 ==0:
					can.create_rectangle(x0, y0, x, y, fill = '#8B6914')
				else: 
					can.create_rectangle(x0, y0, x, y, fill = '#FFE8AF')
		coul = l % 2
	rondjaune()
	initial_echec()
	#Creation des pions innitiaux
	pin()

def coords():
	cy, cx = C, C
	xc, yc = 0, 0
	for i in range(0, 8):																		#creation des coordonnees des 4 linges
		for n in range(0, 8):
			coord.append([xc, yc, cx, cy, 0, 0, 0, 0, 0, 0, 0])									#Creation des coordonnees d'une seule ligne repetee ensuite 4 fois en changeant les coordonnees
			xc += C
			cx += C
		j = 1
		cy += C				#On change l'hordonnee pour changer de lignes
		yc += C
		xc = 0					#On reset les valeurs pour changer de colonnes
		cx = C

def couleurs():
	for c in range(0, 16):
		coord[c][5] = 1
	for c in range(48, 64):
		coord[c][5] = 2

def pion():

	for p in range(0, 64):
		if 8 <= p <= 15 or 48 <= p <= 55:
			coord[p][4] = 1
		if p == 0 or p == 7 or p == 56 or p == 63:
			coord[p][4] = 2
		if p == 1 or p == 6 or p == 57 or p == 62:
			coord[p][4] = 3
		if p == 2 or p == 5 or p == 58 or p == 61:
			coord[p][4] = 4
		if p == 3 or p == 59:
			coord[p][4] = 5
		if p == 4 or p == 60:
			coord[p][4] = 6
	couleurs()

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def pionreset():
	#Replace les pions
	for i in range(0, 64):
		if 0<=i<=15:
			coord[i][5] = 1
		elif 48<=i<=63:
			coord[i][5] = 2
		else:
			coord[i][5] = 0
		if 8<=i<=15 or 48<=i<=55:
			coord[i][4] = 1
		elif i==0 or i==7 or i==56 or i==63:
			coord[i][4] = 2
		elif i==1 or i==6 or i==57 or i==62:
			coord[i][4] = 3
		elif i==2 or i==5 or i==58 or i==61:
			coord[i][4] = 4
		elif i==3 or i==59:
			coord[i][4] = 5
		elif i==4 or i==60:
			coord[i][4] = 6
		else:
			coord[i][4] = 0

def reset():
	#Recréé une partie
	nvl = messagebox.askquestion("Nouvelle Partie", "Voulez-vous recommencer une partie ?")
	if  nvl == 'yes':
		pionreset()
		premierdeplacementdepion()
		cases()
		load = open("save.ceciestunesauvegarde")
		load.write("0")
		load.close()

def menud():
	#Créé un menu défilant
	menu = Menu(fen)
	sousmenu = Menu(menu)
	menu.add_cascade(label="Fichier", menu=sousmenu)
	sousmenu.add_command(label="Nouvelle Partie", command=reset)
	sousmenu.add_command(label="Sauvegarder Partie", command=sauvegarde)
	sousmenu.add_command(label="Charger Partie", command=charger)
	sousmenu.add_command(label="Quitter", command=exit)
	fen.config(menu = menu)

def exit():
	#Quitte le jeu
	ex = messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter le jeu? \nToute partie non sauvegardée sera perdue.")
	if  ex == 'ok':
		fen.destroy()

def sauvegarde_coord():
	#Sauvegarde la matrice coord en une autre matrice en chaine de caractère
	save=coord
	d = []
	e = []
	for j in range(0,64):									#convertie les nombres dans la matrice coord en caractères dans la matrice e
		for i in range(0,10):
			a = coord[j][i]
			b = str(a)
			d.append(b)
		e.append(d)
		d = []
	ligne = [";".join(l) for l in e]							# colonnes
	save = "|\n".join(ligne)										# lignes
	return(save)

def sauvegarde():
	save_turn()
	save_score()
	s = sauvegarde_coord()
	save2 = open("Echecs\\bin\\save.ceciestunesauvegarde", mode="w")
	save2.write(s)
	save2.close()

def charger_coord(fichier):
	contenu = fichier.read()
	fichier.close()
	ligne = contenu.split("|\n")								# lignes
	mat = [l.split(";") for l in ligne]							# colonnes
	d = []
	e = []
	for j in range(0,64):									#convertie les caractères dans la matrice coord en nombres dans la matrice e
		for i in range(0,10):
			a = mat[j][i]
			b = float(a)
			coord[j][i] = b

def charger():
	#Charge la dernière sauvegarde
	load = open("Echecs\\bin\\save.ceciestunesauvegarde")
	charger_coord(load)
	load_turn()
	load_score()
	cases()
	Tableau(turn)

def save_turn():
	#Sauvegarde le tour
	global turn
	save = open("Echecs\\bin\\turn.temp", mode="w")
	save_turn = str(turn)
	save.write(save_turn)
	save.close()

def load_turn():
	global turn
	load = open("Echecs\\bin\\turn.temp", mode="r")
	load_turn = load.read()
	turn = float(load_turn)
	load.close()

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def jaune(d, c):
	#Met la pièce jaune
	list = [ps, ts, cs, fs, res, ros]
	if coord[c][6] == 1:
		x = coord[c][0]+C/2
		y = coord[c][1]+C/2
		can.create_image(x, y, image=list[d])

def select(casex, casey):
	#Permet de sauvegarder la case que l'on selectionne
	for o in range(0, 64):
		lim1 = coord[o][0]
		lim2 = coord[o][1]
		lim3 = coord[o][2]
		lim4 = coord[o][3]
		if lim1 < casex <  lim3 and lim2 < casey < lim4:
			global sel
			sel = o

def selectjaune(b):
	#Permet de mettre une image jaune sur la case selectinnée
	if coord[sel][4] == b:
		c = b - 1
		reborn()
		jaune(c, sel)

def clicoul():
	#Change la couleur su pion selectionne
	selectjaune(1)
	selectjaune(2)
	selectjaune(3)
	selectjaune(4)
	selectjaune(5)
	selectjaune(6)

def action(event):
	#Permet de jouer au jeu tous simplement
	v = listv[0]
	x = event.x
	y = event.y
	if v == 0:
		deselection()
		select(x, y)
		savechec()
		listv[0] = 1
		tour_par_tour2()
		clicoul()
	else:
		deposition(x, y)
		if sel == sel2:
			remove()
		deplacement2()
		listv[0] = 0
		remove()
		reborn()

def remove():
	#Arrete de selectionner
	for i in range(0, 64):
		coord[i][7] = 0
		coord[i][9] = 0

def deposition(casex ,casey):
	#Permet de trouver la case où l'on pose la piece
	for g in range(0, 64):
		lim1 = coord[g][0]
		lim2 = coord[g][1]
		lim3 = coord[g][2]
		lim4 = coord[g][3]
		if lim1 < casex <  lim3 and lim2 < casey < lim4:
			global sel2
			sel2 = g

def deselection():
	#Permet de ne rien selectioner
	for d in range(0, 64):
		if coord[d][7] == 1:
			coord[d][7] = 0

def reborn():
	#Recreee l'echequier avec les pieces au bon endroit
	can.delete(ALL)
	cases()

def premierdeplacementdepion():
	#Permet à la première rangée de pion de pouvoir de déplacer
	for i in range(0, 64):
		if coord[i][4] == 1:
			coord[i][8] = 1

def deplacement1(c):
	#Détermine les déplacement possible
	if c == 1:
		if coord[sel][5] == 1:
			coord[sel][6] = 1
		pionnoir1()
		tour1(1, 2, 2)
		fou1(1, 2, 4)
		reine1(1, 2)
		cavalier1(1, 2)
		roi1(1, 2)
	else:
		if coord[sel][5] == 2:
			coord[sel][6] = 1
		roi1(2, 1)
		tour1(2, 1, 2)
		fou1(2, 1, 4)
		reine1(2, 1)
		cavalier1(2, 1)
		pionblanc1()

def deplacement2():
	#Permet le déplacement en fonction des cases disponibles
	global turn, trouver
	if sel != sel2 and coord[sel2][7] == 1 or coord[sel2][9] == 1:
		points()
		trouver = 1
		pion2(1, 1)
		pion2(1, 2)
		dep2(2, 1)
		dep2(2, 2)
		dep2(3, 1)
		dep2(3, 2)
		dep2(4, 1)
		dep2(4, 2)
		dep2(6, 1)
		dep2(6, 2)
		reine2(1)
		reine2(2)
		turn += 1
		Tableau(turn)
		mise_en_echec()

def tour_par_tour1():
	#Fait une sauvegarde de la matrice coord pour savoir plus tard si elle a changé
	global save1
	save1 = coord

def tour_par_tour2():
	#Compare save1 et coord pour savoir si le joueur a joué
	global turn, j, trouver
	tour_par_tour1()
	if turn%2 == 0 and j != 1:
		deplacement1(0)
	elif turn%2 != 0 and j != 1:
		deplacement1(1)
	else:
		listv[0] = 1

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def dep():
	deplacement1(0)
	deplacement1(1)

def savechec():
	save_echec = sauvegarde_coord()
	save = open("Echecs\\bin\\echec.tem", 'w')
	save.write(save_echec)
	save.close()

def loadechec():
	global turn
	load = open("Echecs\\bin\\echec.tem")
	charger_coord(load)
	turn -= 1

def initial_echec():
	#Ordonne a la case de se mettre en echec
	global trouver, coule, turn, fin
	fin_de_partie_provisoir()
	if trouver == 1:
		for i in range(0, 64):
			if coord[i][10] == 1:
				messagebox.showerror("ECHEC", "Le joueur est en echec")
			if coord[i][10] == 1 and echec_continu == 1 and coord[sel2][5] == coule:
				loadechec()
				fin += 1
		trouver = 0

def mise_en_echec():
	#Permet que le joueur sous en echec
	global sel
	temp = sel
	for deplacementfictif in range(0, 64):
		sel = deplacementfictif
		dep()
	verif_echec()
	sel = temp
	deselection()
	remove()

def verif_echec():
	global trouver, echec_continu, coule
	trouver = 1
	coul = 0
	for i in range(0, 64):
		if coord[i][4] == 6:
			if coord[i][9] == 1:
				coord[i][10] = 1
				coule = coord[i][5]
				echec_continu = 1
			elif coord[i][5] == coul and echec_continu == 1: coord[i][10] = 1
			else:
				fin = 0
				coord[i][10] = 0
		else:
			coord[i][10] = 0

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

k_o = 0
k_ba = 0
k_d = 0
k_g = 0
k_a = 0
k_b = 0
k_o2 = 0
k_ba2 = 0
k_d2 = 0
k_g2 = 0
k_a2 = 0
k_b2 = 0

def konami():
	#OEuf de Paques
	global echec_save
	a,b,c,d,e,f = k_o,k_ba,k_g,k_d,k_a,k_b 							#haut haut bas bas gauche droite gauche droite B A
	if a+b+c+d+e+f == 10:
		sauvegarde()
		fen.destroy()
		import fusee

def konami_o(event):
	global k_o
	k_o += 1
	if k_o == 2:
		global k_o2
		k_o2 = 2

def konami_ba(event):
	global k_ba
	if k_o2 == 2:
		k_ba += 1
		if k_ba == 2: 
			global k_ba2
			k_ba2 = 2

def konami_g(event):
	global k_g
	k_g += 1
	if k_g == 2 and k_ba2 == 2:
		global k_g2
		k_g2 = 2

def konami_d(event):
	global k_d
	k_d += 1
	if k_d == 2:
		global k_d2
		k_b2 = 2

def konami_a(event):
	global k_a
	k_a += 1
	if k_a == 1 and k_d2 == 2 and k_g2 == 2:
		global k_a2
		k_a2 = 2

def konami_b(event):
	global k_b
	k_b += 1
	if k_b == 1 and k_a == 1 :
		konami()
		global k_b2
		k_b2 = 2

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def pionblanc1():
	#Suprimme le pion precedant et creer un pion sur la nouvelle case
	if coord[sel][4] == 1 and coord[sel][5] == 2:
		if coord[sel][8] == 1 and coord[sel-8][4] == 0 and coord[sel-16][4] == 0:
			coord[sel-8][7] = 1
			coord[sel-16][7] = 1
		else: coord[sel-8][7] = 1
		if coord[sel-8][4] != 0: coord[sel-8][7] = 0
		if sel == 15 or sel == 23 or sel == 31 or sel == 39 or sel == 47 or sel == 55:
			if coord[sel-9][5] == 1: coord[sel-9][9] = 1
		elif sel == 8 or sel == 16 or sel == 24 or sel == 32 or sel == 40 or sel == 48:
			if coord[sel-7][5] == 1: coord[sel-7][9] = 1
		else:
			if coord[sel-9][5] == 1: coord[sel-9][9] = 1 
			if coord[sel-7][5] == 1: coord[sel-7][9] = 1

def pion2(p, c):
	if coord[sel][4] == p and coord[sel][5] == c:
		if coord[sel2][7] == 1:
			coord[sel2][4] = p
			coord[sel][4] = 0
			coord[sel2][5] = c
			coord[sel][5] = 0
			if coord[sel][8] == 1:  coord[sel][8] = 0
		if coord[sel2][9] == 1:
			coord[sel2][4] = p
			coord[sel][4] = 0
			coord[sel2][5] = c
			coord[sel][5] = 0
			coord[sel2][9] = 0
			if coord[sel2][8] == 1: coord[sel2][8] = 0
		if 0<=sel2<=7: morphing()
		if 56<=sel2<=63: morphing()

def pionnoir1():
	#Suprimme le pion precedant et creer un pion sur la nouvelle case
	if coord[sel][4] == 1 and coord[sel][5] == 1:
		if coord[sel][8] == 1 and coord[sel+8][4] == 0 and coord[sel+16][4] == 0:
			coord[sel+8][7] = 1
			coord[sel+16][7] = 1
		else: coord[sel+8][7] = 1
		if coord[sel+8][4] != 0: coord[sel+8][7] = 0
		if sel == 15 or sel == 23 or sel == 31 or sel == 39 or sel == 47 or sel == 55:
			if coord[sel+7][5] == 2: coord[sel+7][9] = 1
		elif sel == 8 or sel == 16 or sel == 24 or sel == 32 or sel == 40 or sel == 48:
			if coord[sel+9][5] == 2: coord[sel+9][9] = 1
		else:
			if coord[sel+9][5] == 2: coord[sel+9][9] = 1 
			if coord[sel+7][5] == 2: coord[sel+7][9] = 1

def morphing():
	global morph
	morph = Toplevel()
	Button(morph, text='Reine', command=lambda : morphr(0)).pack(padx=10, pady=10)
	Button(morph, text='Fou', command=lambda : morphr(1)).pack(padx=10, pady=10)
	Button(morph, text='Cavalier', command=lambda : morphr(2)).pack(padx=10, pady=10)
	Button(morph, text='Tour', command=lambda : morphr(3)).pack(padx=10, pady=10)
	morph.transient(fen) 				# Réduction popup impossible 
	morph.grab_set()					# Interaction avec fenetre jeu impossible
	fen.wait_window(morph)				# Arrêt script principal

def morphr(n):
	listeq = [5, 4, 3, 2]
	m = listeq[n]
	coord[sel2][4]=m
	morph.destroy()

def pretour1(b, m):
	for i in range(1, 10):
		c = i * m
		if sel+c>63 or sel+c<0: break																			#Evite d'etre "out of range"
		if coord[sel+c][4] == 0: coord[sel+c][7] = 1																#Permet à la tour de se deplacer sur un case vide
		elif coord[sel+c][4] != 0 and coord[sel+c][5] == b:
			coord[sel+c][9] = 1																#Permet de manger unr pièce
			break																			#Arrete la boucle pour ne pas que la tour continu son chemin malgré les obstacles
		elif coord[sel+c][4] != 0: break 

def pretour2(b, o):
	for i in range(1, 10):
		if o == 1:
			k = -i
			if sel+k == 7 or sel+k == 15 or sel+k == 23 or sel+k == 31 or sel+k == 39 or sel+k == 47 or sel+k == 55 or sel+k == 63: break
			if sel+k<0: break
		elif o == 0:
			k = i
			if sel+k == 0 or sel+k == 8 or sel+k == 16 or sel+k == 24 or sel+k == 32 or sel+k == 40 or sel+k == 48 or sel+k == 56: break
			if sel+k>63: break
		if coord[sel+k][4] == 0: coord[sel+k][7] = 1
		elif coord[sel+k][4] != 0 and coord[sel+k][5] == b:
			coord[sel+k][9] = 1
			break
		elif coord[sel+k][4] != 0 : break

def tour1(a, b, d):
	c = 0
	if coord[sel][4] == d and coord[sel][5] == a:
		pretour1(b, 8)
		pretour1(b, -8)
		pretour2(b, 1)
		pretour2(b, 0)

def dep2(a, d):
	if coord[sel][4] == a and coord[sel][5] == d:
		if coord[sel2][7] == 1:
			coord[sel2][4] = a
			coord[sel][4] = 0
			coord[sel2][5] = d
			coord[sel][5] = 0
			coord[sel][7] = 0
		if coord[sel2][9] == 1:
			coord[sel2][4] = a
			coord[sel][4] = 0
			coord[sel2][5] = d
			coord[sel][5] = 0
			coord[sel2][9] = 0

def prefou(a, e, c, s):
	for i in range(1, 10):
		d = i * c
		if s ==1:									#Deplacement droit
			if sel-d<0 or sel-d>63 or  sel == 7 or sel == 15 or sel == 23 or sel == 31 or sel == 39 or sel == 47 or sel == 55 or sel == 63: break
			if sel-d == 7 or sel-d == 15 or sel-d == 23 or sel-d == 31 or sel-d == 39 or sel-d == 47 or sel-d == 55 or sel-d == 63:
				if coord[sel-d][4] == 0: coord[sel-d][7] = 1
				if coord[sel-d][5] == e:
					coord[sel-d][9] = 1
				break
		else:									#Deplacement gauche
			if sel-d<0 or sel-d>63 or  sel == 0 or sel == 8 or sel == 16 or sel == 24 or sel == 32 or sel == 40 or sel == 48 or sel == 56: break
			if sel-d == 0 or sel-d == 8 or sel-d == 16 or sel-d == 24 or sel-d == 32 or sel-d == 40 or sel-d == 48 or sel-d == 56:
				if coord[sel-d][4] == 0: coord[sel-d][7] = 1
				if coord[sel-d][5] == e: 
					coord[sel-d][9] = 1
				break
		if coord[sel-d][4] != 0:
			if coord[sel-d][5] == a: break
			elif coord[sel-d][5] == e:
				coord[sel-d][9] = 1 
				break
		if coord[sel-d][4] == 0: coord[sel-d][7] = 1

def fou1(a, b, c):
	if coord[sel][4] == c and coord[sel][5] == a:
		prefou(a, b, 7, 1)									#Deplacement superieur droit
		prefou(a, b, -9, 1)									#Deplacement inferieur droit
		prefou(a, b, -7, 0)									#Deplacement inferieur gauche
		prefou(a, b, 9, 0)									#Deplacement inferieur gauche

def reine1(a, b):
	fou1(a, b, 5)
	tour1(a, b, 5)

def reine2(a):
	dep2(5, a)
	dep2(5, a)

def precavalier(f, b):
	if coord[sel+f][5] == 0: coord[sel+f][7] = 1
	if coord[sel+f][4] != 0 and coord[sel+f][5] == b: coord[sel+f][9] = 1

def cavalier1(a, b):
	if coord[sel][4] == 3 and coord[sel][5] == a:
		if sel+17<64 and sel != 7 and sel != 15 and sel != 23 and sel != 31 and sel != 39 and sel != 47 and sel != 55 and sel != 63: precavalier(17, b)
		if sel+15<64 and sel != 0 and sel != 8 and sel != 16 and sel != 24 and sel != 32 and sel != 40 and sel != 48 and sel != 56: precavalier(15, b)
		if sel+10<64 and sel != 7 and sel != 15 and sel != 23 and sel != 31 and sel != 39 and sel != 47 and sel != 55 and sel != 63 and sel != 6 and sel != 14 and sel != 22 and sel != 30 and sel != 38 and sel != 46 and sel != 54 and sel != 62: precavalier(10, b)
		if sel+6<64 and sel != 0 and sel != 8 and sel != 16 and sel != 24 and sel != 32 and sel != 40 and sel != 48 and sel != 56 and sel != 1 and sel != 9 and sel != 17 and sel != 25 and sel != 33 and sel != 41 and sel != 49 and sel != 57: precavalier(6, b)
		if sel-15>=0 and sel != 7 and sel != 15 and sel != 23 and sel != 31 and sel != 39 and sel != 47 and sel != 55 and sel != 63: precavalier(-15, b)
		if sel-17>=0 and sel != 0 and sel != 8 and sel != 16 and sel != 24 and sel != 32 and sel != 40 and sel != 48 and sel != 56: precavalier(-17, b)
		if sel-10>=0 and sel != 0 and sel != 8 and sel != 16 and sel != 24 and sel != 32 and sel != 40 and sel != 48 and sel != 56 and sel != 1 and sel != 9 and sel != 17 and sel != 25 and sel != 33 and sel != 41 and sel != 49 and sel != 57: precavalier(-10, b)
		if sel-6>=0 and sel != 15 and sel != 23 and sel != 31 and sel != 39 and sel != 47 and sel != 55 and sel != 63 and sel != 6 and sel != 14 and sel != 22 and sel != 30 and sel != 38 and sel != 46 and sel != 54 and sel != 62: precavalier(-6, b)

def preroi(f, b):
	if coord[sel+f][5] == b:
		coord[sel+f][9] = 1
	elif coord[sel+f][5] == 0:
		coord[sel+f][7] = 1

def roi1(a, b):
	if coord[sel][4] == 6 and coord[sel][5] == a:
		if sel-9>=0 and sel-9 != 7 and sel-9 != 15 and sel-9 != 23 and sel-9 != 31 and sel-9 != 39 and sel-9 != 47 and sel-9 != 55 and sel-9 != 63: preroi(-9, b)
		if sel-8>0: preroi(-8, b)
		if sel-7>=0 and sel-7 != 0 and sel-7 != 8 and sel-7 != 16 and sel-7 != 24 and sel-7 != 32 and sel-7 != 40 and sel-7 != 48 and sel-7 != 56: preroi(-7, b)
		if sel+1<64  and sel+1 != 0 and sel+1 != 8 and sel+1 != 16 and sel+1 != 24 and sel+1 != 32 and sel+1 != 40 and sel+1 != 48 and sel+1 != 56: preroi(1,b )
		if sel-1>=0 and sel-1 != 7 and sel-1 != 15 and sel-1 != 23 and sel-1 != 31 and sel-1 != 39 and sel-1 != 47 and sel-1 != 55 and sel-1 != 63: preroi(-1, b)
		if sel+7<64 and sel+7 and sel+7 != 7 and sel+7 != 15 and sel+7 != 23 and sel+7 != 31 and sel+7 != 39 and sel+7 != 47 and sel+7 != 55 and sel+7 != 63: preroi(7, b)
		if sel+9<64 and sel+9 and sel+9 != 0 and sel+9 != 8 and sel+9 != 16 and sel+9 != 24 and sel+9 != 32 and sel+9 != 40 and sel+9 != 48 and sel+9 != 56: preroi(9, b)
		if sel+8<64: preroi(8, b)


####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

j1, j2 = 0, 0

def Tableau(turn):
	global tab
	tab = Canvas(fen, width = 150, height = H)
	tab.grid(column = 1, row = 0, sticky='n')
	tab.create_text(50, 25, text = 'Noirs')
	tab.create_text(50, 150, text = 'Blancs')
	tab.destroy
	if turn%2 != 0:
		tab.create_oval(40, 50, 60, 70, fill = 'yellow')
	else:
		tab.create_oval(40, 175, 60, 195, fill = 'yellow')
	Score()

def Score():
	global j1, j2, tab
	scoreJ1 = str(j1)
	scoreJ2 = str(j2)
	tab.create_text(100, 25, text = scoreJ1)
	tab.create_text(100, 150, text = scoreJ2)

def points():
	if coord[sel][5] == 1 and coord[sel2][5] == 2: prepointsj1()
	if coord[sel][5] == 2 and coord[sel2][5] == 1: prepointsj2()

def prepointsj1():
	global j1
	if coord[sel2][4] == 1: j1 += 1
	if coord[sel2][4] == 2: j1 += 5
	if coord[sel2][4] == 3: j1 += 3
	if coord[sel2][4] == 4: j1 += 2
	if coord[sel2][4] == 5: j1 += 10

def prepointsj2():
	global j2
	if coord[sel2][4] == 1: j2 += 1
	if coord[sel2][4] == 2: j2 += 5
	if coord[sel2][4] == 3: j2 += 3
	if coord[sel2][4] == 4: j2 += 2
	if coord[sel2][4] == 5: j2+= 10

def fin_de_partie_provisoir():
	global fin, j1, j2
	if fin == 10:
		for i in range(0, 64):
			if coord[i][10] == 1:
				if coord[i][5] == 1:
					messagebox.showwarning("FIN DE PARTIE", "Les Blancs on gagnés")
					can.bind('<Button-1>', exit2)
					deselection()
					remove()
					j1 += 20
				if coord[i][5] == 2:
					messagebox.showwarning("FIN DE PARTIE", "Les Noirs on gagnés")
					can.bind('<Button-1>', exit2)
					deselection()
					remove()
					j2 += 20

def exit2(event):
	#Quitte le jeu
	sauvegarde()
	fen.destroy()
	import accueil
	


def save_score():
	#Sauvegarde le tour
	global j1, j2
	save1 = open("Echecs\\scorej1.temp", mode="w")
	save2 = open("Echecs\\scorej2.temp", mode="w")
	save_j1 = str(j1)
	save_j2 = str(j2)
	save1.write(save_j1)
	save2.write(save_j2)
	save2.close()
	save1.close()

def load_score():
	global j1, j2
	load1 = open("Echecs\\scorej1.temp", mode="r")
	load2 = open("Echecs\\scorej1.temp", mode="r")
	load_j1 = load1.readline(1)
	j1 = int(load_j1)
	load_j2 = load2.readline(1)
	j2 = int(load_j2)
	load2.close()
	load1.close()

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

fen = Tk()
can = Canvas(fen, width = H, height = H)
can.grid(column = 0, row = 0)

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

pn = PhotoImage(file = "Echecs\\image\\pionn.png")
pb = PhotoImage(file = "Echecs\\image\\pionb.png")
tb = PhotoImage(file = "Echecs\\image\\tourb.png")
tn = PhotoImage(file = "Echecs\\image\\tourn.png")
fb = PhotoImage(file = "Echecs\\image\\foub.png")
fn = PhotoImage(file = "Echecs\\image\\foun.png")
rob = PhotoImage(file = "Echecs\\image\\roib.png")
ron = PhotoImage(file = "Echecs\\image\\roin.png")
reb = PhotoImage(file = "Echecs\\image\\reineb.png")
ren = PhotoImage(file = "Echecs\\image\\reinen.png")
cb = PhotoImage(file = "Echecs\\image\\cavalierb.png")
cn = PhotoImage(file = "Echecs\\image\\cavaliern.png")
ps = PhotoImage(file = "Echecs\\image\\pionsel.png")
ts = PhotoImage(file = "Echecs\\image\\toursel.png")
cs = PhotoImage(file = "Echecs\\image\\cavaliersel.png")
fs = PhotoImage(file = "Echecs\\image\\fousel.png")
res = PhotoImage(file = "Echecs\\image\\reinesel.png")
ros = PhotoImage(file = "Echecs\image\\roisel.png")

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

def verif(event):
	x = event.x
	y = event.y
	for i in range(0, 64):
		if coord[i][0]<x<coord[i][2] and coord[i][1]<x<coord[i][3]:
			print(coord[i][10])



coords()
Tableau(0)
pion()
cases()
premierdeplacementdepion()
menud()

can.bind('<Button-1>', action)
can.bind('<Button-3>', verif)
can.bind_all('<KeyPress-Up>', konami_o)
can.bind_all('<KeyPress-Down>', konami_ba)
can.bind_all('<KeyPress-Left>', konami_g)
can.bind_all('<KeyPress-Right>', konami_d)
can.bind_all('<KeyPress-a>', konami_a)
can.bind_all('<KeyPress-b>', konami_b)

fen.mainloop()
