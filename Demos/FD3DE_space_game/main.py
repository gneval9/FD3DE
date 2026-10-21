# Made and developed by gneval9 Software
# | 01-03-2026 | 22-05-2026 |

import fd3de
import atexit
import keyboard
import wall_mover as WM
import os
import time
import random

import nave_anim

import framedirect as FD
import FDWriter as FDW


WM.main()
FD.init()

nave_data = fd3de.load("Modelos/nave.fd3de")
back_line_data = fd3de.load("Modelos/long_line.fd3de")
laser = fd3de.load("Modelos/laser.fd3de")
piedra_load = fd3de.load("Modelos/cubo.fd3de")


nave = fd3de.spawn(nave_data)
back_line = fd3de.spawn(back_line_data)


fd3de.perspective = "side"

fd3de.rotate("y", 180, nave)
fd3de.rotate("x", -10, nave)

fd3de.move("z", -150, nave)
fd3de.move("y", -100, nave)

fd3de.move("z", -130, back_line)
fd3de.move("y", -150, back_line)

screen_x, screen_y = FD.screen_width, FD.screen_height


puntos = 0

laseres = []
piedras = []
last_shot = 0

space_was_pressed = False

last_speed_update = 0

rock_speed = -3

init_time = time.time()



def render():
	fd3de.render(back_line, 0xFF101010)

	fd3de.render(nave, fd3de.RED, 0.9)
	
	WM.check_wall_pos()
	WM.render(fd3de.YELLOW)
	fd3de.update()


	WM.render(fd3de.BLACK)
	
	

	fd3de.clear_object(nave, 0.9)

	for l in laseres:
		fd3de.clear_object(l)

	for p in piedras:
		fd3de.clear_object(p,0.3)





def shoot():
	nuevo_laser = fd3de.spawn(laser)
	fd3de.move("x", nave["position"][0] - nuevo_laser["position"][0], nuevo_laser)
	fd3de.move("y", nave["position"][1] - nuevo_laser["position"][1], nuevo_laser)
	fd3de.move("z", nave["position"][2] - nuevo_laser["position"][2] + 50, nuevo_laser)
	laseres.append(nuevo_laser)


	

while True:

	# Detectar entradas de teclado
	#-----------------------------

	if keyboard.is_pressed("right") and nave["position"][0] < 180:
		fd3de.move("x", 7, nave)
		nave["rotation"][2] = -15


	elif keyboard.is_pressed("left") and nave["position"][0] > -180:
		fd3de.move("x", -7, nave)
		nave["rotation"][2] = 15
		

	else:
		fd3de.rotate("z", nave["rotation"][2]*-1, nave)




	if keyboard.is_pressed("space"):
		if time.time() - last_shot > 0.5 and space_was_pressed == False:
			last_shot = time.time()
			shoot()
			space_was_pressed = True

	if not keyboard.is_pressed("space"):
		space_was_pressed = False



	# GUI
	#____

	FDW.write(f"Puntos: {puntos}", 40, 40, 5)


	if time.time() - last_shot > 0.5:
		FD.draw_line(20, 60, 300, 60, FD.GREEN)
	else:
		FD.draw_line(20, 60, 300, 60, FD.RED)





	# Generar y mover piedras
	#-------------------------

	if time.time() - last_speed_update > 5:
		rock_speed += -0.2
		last_speed_update = time.time()
		
	else:
		pass

	if len(piedras) < 5:
		random_rot = random.randint(0,90)
		while True:
			random_z = random.randint(-150,150)
			random_x = random.randint(-180,180)
			ok = True
			
			for p in piedras:
				if abs(random_x - p["position"][0]) < 100 and abs(random_z - p["position"][2]) < 150:
					ok = False
					break

			if ok:
				break 	


		piedra = fd3de.spawn(piedra_load) 	
		fd3de.move("z", 600 + random_z, piedra)
		fd3de.move("y", -100, piedra)
		fd3de.move("x", random_x, piedra)
		
		fd3de.rotate("y", random_rot, piedra)
		fd3de.rotate("x", random_rot, piedra)

		piedras.append(piedra)


	for p in range(len(piedras)-1, -1, -1):
		fd3de.move("z", rock_speed, piedras[p])
		fd3de.render(piedras[p], fd3de.GREEN, 0.3)

		if piedras[p]["position"][2] < -130:
			fd3de.clear_object(piedras[p], 0.3)
			del piedras[p]
			FD.fill(FD.BLACK)
			
			FDW.write(f"Puntos: {puntos}", screen_x // 2 - 250, screen_y // 2 + 200, 10, FD.GREEN)

			while True:
				FDW.write("HAS PERDIDO", screen_x // 2 - 500, screen_y // 2 - 100, 20, FD.RED)
				FD.update()
				print(" ")
				time.sleep(0.7)
				FDW.write("HAS PERDIDO", screen_x // 2 - 500, screen_y // 2 - 100, 20, FD.WHITE)
				FD.update()
				print(" ")
				time.sleep(0.5)

			exit()




	# Mover y eliminar láseres
	#--------------------------

	for n in range(len(laseres)-1, -1, -1):
		fd3de.move("z", 20, laseres[n])
		fd3de.render(laseres[n], fd3de.WHITE)

		if laseres[n]["position"][2] > 800:
			fd3de.clear_object(laseres[n])
			del laseres[n]


	# Colision de los láseres
	#-------------------------

	for n in range(len(laseres)-1, -1, -1):
		for i in range(len(piedras)-1, -1, -1):
			if abs(laseres[n]["position"][0] - piedras[i]["position"][0]) < 30 and abs(laseres[n]["position"][2] - piedras[i]["position"][2]) < 30:
				fd3de.clear_object(piedras[i],0.3)
				fd3de.clear_object(laseres[n])
				del piedras[i]
				del laseres[n]
				FDW.write(f"Puntos: {puntos}", 40, 40, 5, FD.BLACK)
				puntos += 1
				FDW.write(f"Puntos: {puntos}", 40, 40, 5)

				break

	WM.move_walls()

	render()

