import fd3de
import time
import math as m
import keyboard
import FDWriter
import framedirect as FD

LEM = fd3de.spawn(fd3de.load("Modelos/LEM.fd3de"))
flame = fd3de.spawn(fd3de.load("Modelos/flame.fd3de"))
plano = fd3de.spawn(fd3de.load("Modelos/plano.fd3de"))

nave_speed_x = 0
nave_speed_y = 0

g = 9.81
top = -100
debug = True

flame_old = False
rot_input_speed = 8

fd3de.scene_new("main")

fd3de.scene_add("main", LEM, fd3de.WHITE)
fd3de.scene_add("main", plano, fd3de.GREEN, 3)

fd3de.move("y", -40, flame)
fd3de.move("y", -200, plano)

fd3de.move("z", 200, LEM)
fd3de.move("z", 200, flame)
fd3de.move("z", 200, plano)

def orbit(obj, target, axis, deg):
	rad = deg*m.pi/180
	tx, ty, tz = target["position"]
	ox, oy, oz = obj["position"]

	x, y, z = ox-tx, oy-ty, oz-tz

	if axis == "x":
		y, z = y*m.cos(rad)-z*m.sin(rad), y*m.sin(rad)+z*m.cos(rad)

	elif axis == "y":
		x, z = x*m.cos(rad)+z*m.sin(rad), -x*m.sin(rad)+z*m.cos(rad)

	elif axis == "z":
		x, y = x*m.cos(rad)-y*m.sin(rad), x*m.sin(rad)+y*m.cos(rad)

	obj["position"] = [tx+x, ty+y, tz+z]



def propulsion(obj):
	global nave_speed_x, nave_speed_y

	rad = (obj["rotation"][2] + 90)*m.pi/180

	px = m.cos(rad)
	py = m.sin(rad)

	nave_speed_x += px * 3
	nave_speed_y += py * 3



while True:
	if keyboard.is_pressed("right"):
		fd3de.rotate("z", -rot_input_speed, LEM)
		fd3de.rotate("z", -rot_input_speed, flame)
		orbit(flame, LEM, "z", -rot_input_speed)

	if keyboard.is_pressed("left"):
		fd3de.rotate("z", rot_input_speed, LEM)
		fd3de.rotate("z", rot_input_speed, flame)
		orbit(flame, LEM, "z", rot_input_speed)



	if keyboard.is_pressed("space"):
		propulsion(LEM)

		if not flame_old:
			fd3de.scene_add("main", flame, fd3de.ORANGE, 2)
		flame_old = True
	

	else:
		flame_old = False
		fd3de.scene_del("main", flame)

	if keyboard.is_pressed("g"):
		debug = not debug
		time.sleep(0.05)










	# Physics
	# -------

	nave_speed_y += -g / 10
	LEM["position"][1] += nave_speed_y
	LEM["position"][0] += nave_speed_x
	flame["position"][1] += nave_speed_y
	flame["position"][0] += nave_speed_x
	   



	if LEM["position"][1] < top:
		LEM["position"][1] = top
		flame["position"][1] = top -40

		if nave_speed_y < -20 or nave_speed_x > 7 or nave_speed_x < -7:
			print("EXPLODED")
			exit()

		nave_speed_x = 0
		nave_speed_y = 0
		
		flame["position"][0] = LEM["position"][0]
	
		LEM["rotation"][2] = 0
		flame["rotation"][2] = 0





	# Debug
	# -----
	
	if debug == True:

		FDWriter.write(f"Orientation: {LEM["rotation"][2]+90}", 60, 60, 2, FD.WHITE, True)

		FDWriter.write(f"nave_speed_x: {round(nave_speed_x)}", 60,100, 2, FD.WHITE, True)
		FDWriter.write(f"nave_speed_y: {round(nave_speed_y)}", 60,120, 2, FD.WHITE, True)

		FDWriter.write(f"nave_coord_x: {round(LEM["position"][0])}", 60,140, 2, FD.WHITE, True)
		FDWriter.write(f"nave_coord_y: {round(LEM["position"][1])}", 60,160, 2, FD.WHITE, True)


	fd3de.render_scene("main")

	if debug == True:

		FDWriter.write(f"Orientation: {LEM["rotation"][2]+90}", 60, 60, 2, FD.BLACK, True)

		FDWriter.write(f"nave_speed_x: {round(nave_speed_x)}", 60,100, 2, FD.BLACK, True)
		FDWriter.write(f"nave_speed_y: {round(nave_speed_y)}", 60,120, 2, FD.BLACK, True)

		FDWriter.write(f"nave_coord_x: {round(LEM["position"][0])}", 60,140, 2, FD.BLACK, True)
		FDWriter.write(f"nave_coord_y: {round(LEM["position"][1])}", 60,160, 2, FD.BLACK, True)





