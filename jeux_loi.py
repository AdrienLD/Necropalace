#   Author  :   Lionel
#   Date    :   26/06/2019
#   Desc    :   Goose game

from tkinter import *
from random import *

####################
###  Variable  #####
####################

L = 1024
H = 576

tour = [1]
position = [0,0]

#coordoner des case de plateau
cases = [[30,500,120,570],[120,510,235,560],[235,510,350,560],[350,510,465,560],[465,510,610,560],[120,510,235,560],[610,510,760,560],[760,510,875,560],[875,510,995,560],[930,395,995,510],[930,300,995,395],[930,185,995,300],[930,70,995,185],[845,20,995,70],[730,20,845,70],[600,20,730,70],[440,20,600,70],[350,10,440,80],[175,20,350,70],[45,20,175,70],[45,70,120,160],[120,115,290,160],[290,115,435,160],[435,115,610,160],[610,115,820,160],[820,100,905,175],[830,175,905,280],[830,280,905,430],[760,430,905,490],[540,430,760,490],[350,430,540,490],[130,430,350,490],[60,335,130,460],[130,335,290,395],[290,335,450,395],[450,335,640,395],[640,335,800,395],[730,230,800,335],[670,185,800,230],[580,185,670,290],[440,240,580,290],[305,210,440,310]]

##################
###  Fonction  ###
##################

def importimage():
	global fond, id1, id2, id3, id4, id5, id6
	fond = PhotoImage(file = "Lionel/Images/plateau_l_oie.png")
	id1 = PhotoImage(file = "Lionel/Images/de1.png")
	id2 = PhotoImage(file = "Lionel/Images/de2.png")
	id3 = PhotoImage(file = "Lionel/Images/de3.png")
	id4 = PhotoImage(file = "Lionel/Images/de4.png")
	id5 = PhotoImage(file = "Lionel/Images/de5.png")
	id6 = PhotoImage(file = "Lionel/Images/de6.png")

def draw_victoire():
	
	can.create_text(350,180,text = "Victoire",fill = "#FFFFFF")

def draw():
	
	x1_middle = (cases[position[0]][2] + cases[position[0]][0])/2
	y1_middle = (cases[position[0]][3] + cases[position[0]][1])/2
	x1_longueur = cases[position[0]][2] - cases[position[0]][0]
	y1_longueur = cases[position[0]][3] - cases[position[0]][1]	
		
	x2_middle = (cases[position[1]][2] + cases[position[1]][0])/2
	y2_middle = (cases[position[1]][3] + cases[position[1]][1])/2
	x2_longueur = cases[position[1]][2] - cases[position[1]][0]
	y2_longueur = cases[position[1]][3] - cases[position[1]][1]	
		
	if x1_longueur < y1_longueur:
		rayon1 = x1_longueur/2 -5
	else:
		rayon1 = y1_longueur/2 -5
			
	if x2_longueur < y2_longueur:
		rayon2 = x2_longueur/2 -5
	else:
		rayon2 = y2_longueur/2 -5
		
	can.delete("all")																										#suprime tous le plateau
	importimage()																										
	can.create_image(L/2, H/2, image = fond)																				# recree un plateau
	can.create_oval(x1_middle-rayon1,y1_middle-rayon1,x1_middle+rayon1,y1_middle+rayon1,width = 0,fill = "#FF0000")			# pion 1
	can.create_oval(x2_middle-rayon2,y2_middle-rayon2,x2_middle+rayon2,y2_middle+rayon2,width = 0,fill = "#0000FF")			# pion 2
	if(position[0] == 40 or position[1] == 40):
		draw_victoire()
		return()

def de(a):
	if a == 1:
		can.create_image(105, 250, image = id1)
	if a == 2:
		can.create_image(105, 250, image = id2)	
	if a == 3:
		can.create_image(105, 250, image = id3)	
	if a == 4:
		can.create_image(105, 250, image = id4)	
	if a == 5:
		can.create_image(105, 250, image = id5)	
	if a == 6:
		can.create_image(105, 250, image = id6)	

#################
###  Programe ###
#################

fen = Tk()
can = Canvas(fen, width = L, height = H, background = 'white')
can.pack()


importimage()

can.create_image(L/2, H/2, image = fond)


def clique(event):
	if tour[0] == 1:
		rand = randint(1,6)
		if position[0] + rand <= 40:
			if position[0] != 34 or rand == 6:
				position[0] = position[0] + rand
		if position[0] == 1: position[0] = 0
		if position[0] == 6: position[0] = 10
		if position[0] == 11: position[0] = 9
		if position[0] == 12: position[0] = 13
		if position[0] == 15: position[0] = 17
		if position[0] == 16: position[0] = 24
		if position[0] == 19: position[0] = 17
		if position[0] == 23: position[0] = 29
		if position[0] == 28: position[0] = 30
		if position[0] == 31: position[0] = 30
		if position[0] == 32: position[0] = 35
		if position[0] == 39: position[0] = 33
			
		draw()
		de(rand)
		tour[0] = 2
	else:
		rand = randint(1,6)
		if position[1] + rand <= 40:
			if position[1] != 34 or rand == 6:
				position[1] = position[1] + rand
		if position[1] == 1: position[1] = 0
		if position[1] == 6: position[1] = 10
		if position[1] == 11: position[1] = 9
		if position[1] == 12: position[1] = 13
		if position[1] == 15: position[1] = 17
		if position[1] == 16: position[1] = 24
		if position[1] == 19: position[1] = 17
		if position[1] == 23: position[1] = 29
		if position[1] == 28: position[1] = 30
		if position[1] == 31: position[1] = 30
		if position[1] == 32: position[1] = 35
		if position[1] == 39: position[1] = 33
		
		draw()
		de(rand)	
		tour[0] = 1

can.bind("<Button-1>", clique)
draw()




fen.mainloop()
