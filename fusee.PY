#   Author  :   Nolwen / Lionel / Adrien LD
#   Date    :   26/06/2019
#   Desc    :   Rocket 

from tkinter import *
from random import *
from PIL import Image, ImageTk


H = 900
L = 700
listcoord =  [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]
listj = [0]
v = 0
temps = 0
fusee_save = 0

def etoiles(x, y):
	can.create_oval(x, y, x + 5, y + 5, fill = 'white')

def actions():
	can.delete(ALL)
	dy = 5
	j = listj[0]
	j = j + 1
	listj[0] = j
	for i in range(1, 50):
		listcoord[i][1] = int(listcoord[i][1]) + dy
		y = listcoord[i][1]
		x = listcoord[i][0]
		if y>=L:
			listcoord[i][1] = 0
			listcoord[i][0] = int(randrange (10, H - 1))
		etoiles(x, y)
		if j%2==0: can.create_image(H / 2 + 25, L - 50, anchor = S, image=photo)
		else: can.create_image(H / 2 + 25, L - 50, anchor = S, image=photo2)
	fen.after(1, actions)

def coordonneetoiles():
	for i in range(1, 50):
		listcoord[i][0] = int(randrange (10, H - 1))
		listcoord[i][1] = int(randrange (10, L - 1))

def timer():
	global temps, fusee_save
	temps += 1
	if temps == 10:
		fusee_save = 1
		fen.destroy()
		import Echecs
	fen.after(500, timer)

fen = Tk()
can = Canvas(fen, width = H, height = L, bg = 'black')
image = Image.open("Echecs\\image\\image.png") 
image2 = Image.open("Echecs\\image\\image2.png")
photo = ImageTk.PhotoImage(image) 
photo2 = ImageTk.PhotoImage(image2) 
can.pack(side = LEFT, padx = 0, pady = 0)


coordonneetoiles()
timer()
actions()


fen.mainloop()
