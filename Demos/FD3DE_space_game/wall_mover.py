import fd3de
import time
import os

walls_r = []
walls_l = []

pared = fd3de.load("Modelos/wall.fd3de")

def render(color):
		
	for n in range(len(walls_r)):
		fd3de.render(walls_r[n], color)
		
	

	for n in range(len(walls_l)):
		fd3de.render(walls_l[n], color)
	



def move_walls():
	global walls_l, walls_r

	for n in range(len(walls_r)):
		fd3de.move("z", -3, walls_r[n])
		fd3de.move("z", -3, walls_l[n])


def check_wall_pos():
	if walls_r[0]['position'][2] < -400:
		main()
	


def main():
	global walls_l, walls_r

	walls_r = []
	walls_l = []

	for n in range(0,3):
		walls_r.append(fd3de.spawn(pared))
		walls_l.append(fd3de.spawn(pared))


	for n in range(len(walls_r)):
		fd3de.move("y", -100, walls_r[n])
		fd3de.move("x", -360, walls_r[n])

	for n in range(len(walls_l)):
		fd3de.move("y", -100, walls_l[n])
		fd3de.move("x", 360, walls_l[n])

	for n in range(len(walls_r)):
		fd3de.move("z", 400*n, walls_r[n])
		fd3de.move("z", 400*n, walls_l[n])


