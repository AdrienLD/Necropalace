def deplacementpionblanc1():
	#Suprimme le pion precedant et creer un pion sur la nouvelle case
	if coord[sel][4] == 1 and coord[sel][5] == 2:
		if coord[sel][8] == 1 and coord[sel-8][4] == 0 and coord[sel-16][4] == 0:
			coord[sel-8][7] = 1
			coord[sel-16][7] = 1
		else:
			coord[sel-8][7] = 1
		if coord[sel-8][4] != 0:
			coord[sel-8][7] = 0
		if sel == 15 or sel == 23 or sel == 31 or sel == 39 or sel == 47 or sel == 55:
			if coord[sel-9][5] == 1:
				coord[sel-9][9] = 1
		elif sel == 8 or sel == 16 or sel == 24 or sel == 32 or sel == 40 or sel == 48:
			if coord[sel-7][5] == 1:
				coord[sel-7][9] = 1
		else:
			if coord[sel-9][5] == 1:
				coord[sel-9][9] = 1 
			if coord[sel-7][5] == 1:
				coord[sel-7][9] = 1

def deplacementpionblanc2():
	if coord[sel][4] == 1 and coord[sel][5] == 2:
		if coord[sel2][7] == 1:
			coord[sel2][4] = 1
			coord[sel][4] = 0

			coord[sel2][5] = 2
			coord[sel][5] = 0

			if coord[sel][8] == 1:
				coord[sel][8] = 0

		if coord[sel2][9] == 1:
			coord[sel2][4] = 1
			coord[sel][4] = 0

			coord[sel2][5] = 2
			coord[sel][5] = 0
			coord[sel2][9] = 0
			if coord[sel2][8] == 1:
				coord[sel2][8] = 0
		if 0<=sel2<=7:
			morphing()

def deplacementpionnoir1():
	#Suprimme le pion precedant et creer un pion sur la nouvelle case
	if coord[sel][4] == 1 and coord[sel][5] == 1:
		if coord[sel][8] == 1 and coord[sel+8][4] == 0 and coord[sel+16][4] == 0:
			coord[sel+8][7] = 1
			coord[sel+16][7] = 1
		else:
			coord[sel+8][7] = 1
		if coord[sel+8][4] != 0:
			coord[sel+8][7] = 0
		if sel == 15 or sel == 23 or sel == 31 or sel == 39 or sel == 47 or sel == 55:
			if coord[sel+7][5] == 2:
				coord[sel+7][9] = 1
		elif sel == 8 or sel == 16 or sel == 24 or sel == 32 or sel == 40 or sel == 48:
			if coord[sel+9][5] == 2:
				coord[sel+9][9] = 1
		else:
			if coord[sel+9][5] == 2:
				coord[sel+9][9] = 1 
			if coord[sel+7][5] == 2:
				coord[sel+7][9] = 1

def deplacementpionnoir2():
	if coord[sel][4] == 1 and coord[sel][5] == 1:
		if coord[sel2][7] == 1:
			coord[sel2][4] = 1
			coord[sel][4] = 0

			coord[sel2][5] = 1
			coord[sel][5] = 0

			if coord[sel][8] == 1:
				coord[sel][8] = 0

		if coord[sel2][9] == 1:
			coord[sel2][4] = 1
			coord[sel][4] = 0

			coord[sel2][5] = 1
			coord[sel][5] = 0
			coord[sel2][9] = 0
			if coord[sel2][8] == 1:
				coord[sel2][8] = 0
		if 56<=sel2<=63:
			morphing()
			
def morphing():
	morph = Toplevel()
	Button(morph, text='Reine', command=lambda : morphr(0)).pack(padx=10, pady=10)
	Button(morph, text='Fou', command=lambda : morphr(1)).pack(padx=10, pady=10)
	Button(morph, text='Cavalier', command=lambda : morphr(2)).pack(padx=10, pady=10)
	Button(morph, text='Tour', command=lambda : morphr(3)).pack(padx=10, pady=10)
	Button(morph, text='Quitter', command=morph.destroy).pack(padx=10, pady=10)
	morph.transient(fen) 				# Réduction popup impossible 
	morph.grab_set()					# Interaction avec fenetre jeu impossible
	fen.wait_window(morph)				# Arrêt script principal

def morphr(n):
	listeq = [5, 4, 3, 2]
	m = listeq[n]
	coord[sel2][4]=m
