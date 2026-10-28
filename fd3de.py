# Made and developed by gneval9 Software
# 27-10-2026
# V0.20.1

import framedirect as FD
import math as m
import ast
import atexit
import os
import pathlib
import keyboard

from . import utils

FD.init()

os.system("tput civis")
os.system("stty -echo")

def close_all():
	FD.close()
	os.system("tput cnorm")
	os.system("stty echo")

atexit.register(close_all)


screen_x = FD.screen_width
screen_y = FD.screen_height


scenes = {}
ALL = "ALL"


center = (screen_x // 2, screen_y // 2)

f = 550 * (screen_x / 1280)		# Distáncia focal
camera_offset = 300	# Distancia de la cámara

perspective = "front" # front, up, side


# Colores
RED = FD.RED
GREEN = FD.GREEN
BLUE = FD.BLUE
WHITE = FD.WHITE
BLACK = FD.BLACK
YELLOW = FD.YELLOW
CYAN = FD.CYAN
MAGENTA = FD.MAGENTA
GRAY = FD.GRAY
ORANGE = FD.ORANGE


def key_input(key):
	return keyboard.is_pressed(key)



def load(path):

	archivo = pathlib.Path(path)

	if archivo.suffix != ".fd3de":
		raise ValueError("Error: El archivo no es un .fd3de")
		

	with open(path, "r") as f:
		file = ast.literal_eval(f.read())

	return(file)


def spawn(model):
	return {
		"original": model,
		"rotation": [0, 0, 0],
		"position": [0, 0, 0]
	}



def update():
	FD.update()



def get_center(obj):
	cx = 0
	cy = 0
	cz = 0

	for v in obj["original"]:
		cx += v[0]
		cy += v[1]
		cz += v[2]

	cx = cx / len(obj["original"])
	cy = cy / len(obj["original"])
	cz = cz / len(obj["original"])

	return (cx, cy, cz)



def move(axis, dist, obj):
	if axis == "x":
		obj["position"][0] += dist

	elif axis == "y":
		obj["position"][1] += dist

	elif axis == "z":
		obj["position"][2] += dist

	else:
		raise ValueError(f"Error: '{axis}' no es un argumento válido para la función 'move()'")
		




def rotate(axis, angle, obj):
	if axis == "x":
		obj["rotation"][0] += angle

	elif axis == "y":
		obj["rotation"][1] += angle

	elif axis == "z":
		obj["rotation"][2] += angle

	else:
		raise ValueError(f"Error: '{axis}' no es un argumento válido para la función 'rotate()'")
		



def orbit(axis, deg, obj, target):
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




def scene_new(scene):
	if scene in scenes:	
		raise ValueError("La escena ya existe.")
	
	elif scene == "ALL":
		raise ValueError(f"El nombre '{ALL}' está reservado y no se puede utilizar como nombre para la escena.")

	scenes[scene] = []


def scene_rm(scene):
	for n in scenes:
		if n is scene:
			for n in range(len(scenes[scene])):
				clear_object(*scenes[scene][n][:1], *scenes[scene][n][2:])
			del scenes[scene]
			break


def scene_add(scene, obj, color=WHITE, scale=1, perspective_3d=True):
	for n in scenes[scene]:
		if n[0] is obj:
			raise ValueError("El objeto ya existe en la escena.")
	
	scenes[scene].append((obj, color, scale, perspective_3d))


def scene_del(scene, obj):
	for n in scenes[scene]:
		if n[0] is obj:
			clear_object(n[0], n[2], n[3])
			scenes[scene].remove(n)
			break



def scene_move_all(axis, dist, scene):
	for n in range(len(scenes[scene])):
		move(axis, dist, scenes[scene][n][0])



def scene_orbit_all(axis, dist, scene, target):
	for n in range(len(scenes[scene])):
		orbit(axis, dist, scenes[scene][n][0], target)



def render_scene(scene):
	if scene == ALL:
		for i in scenes:
			for n in range(len(scenes[i])):
				render(*scenes[i][n])
		
		update()

		for i in scenes:
			for n in range(len(scenes[i])):
				clear_object(*scenes[i][n][:1], *scenes[i][n][2:])

	else:
		for n in range(len(scenes[scene])):
			render(*scenes[scene][n])
		
		update()


		for n in range(len(scenes[scene])):
			clear_object(*scenes[scene][n][:1], *scenes[scene][n][2:])






def render(obj, color=WHITE, scale=1, perspective_3d=True):

	projected = []

	ax, ay, az = obj["rotation"]
	px, py, pz = obj["position"]

	ax = m.radians(ax)
	ay = m.radians(ay)
	az = m.radians(az)

	cosx, sinx = m.cos(ax), m.sin(ax)
	cosy, siny = m.cos(ay), m.sin(ay)
	cosz, sinz = m.cos(az), m.sin(az)

	# ---- Transformación completa ----
	for v in obj["original"]:

		x, y, z = v[0] * scale, v[1] * scale, v[2] * scale

		# Rot X
		y, z = y * cosx - z * sinx, y * sinx + z * cosx

		# Rot Y
		x, z = x * cosy + z * siny, -x * siny + z * cosy

		# Rot Z
		x, y = x * cosz - y * sinz, x * sinz + y * cosz

		# Traslación
		x += px 
		y += py 
		z += pz 

		# Cámara
		z += camera_offset

		if z <= 60:
			z = 60

	
		if perspective == "front":
			#print()

			try:

				if perspective_3d == True:
					Px = ((f * x) / z)		
					Py = ((f * y) / z)

					projected.append([Px, Py])

				else:
					Px = x
					Py = y
					projected.append([Px, Py])

			except ZeroDivisionError:
				Px = 0
				Py = 0
				projected.append([Px, Py])






		elif perspective == "up":
			print(x,y,z)
			try:

				if perspective_3d == True:
					Px = (f * x) / y
					Py = (f * z) / y
					projected.append([Px, Py*-1])

				else:
					Px = x
					Py = y

			except ZeroDivisionError:
				Px = 0
				Py = 0
				projected.append([Px, Py*-1])


		elif perspective == "side":
			print(x,y,z)

			Px = (f * x) / x
			Py = (f * z) / x
			projected.append([Px, Py])





	# ---- Dibujar aristas ----
	for i in range(len(projected)):

		if projected[i] is None:
			continue

		for k in range(3, len(obj["original"][i])):

			index = obj["original"][i][k]

			if 0 <= index < len(projected) and projected[index] is not None:

				x1, y1 = projected[i]
				x2, y2 = projected[index]
			

				FD.draw_line(
					round(x1 + center[0]),
					round(-y1 + center[1]),
					round(x2 + center[0]),
					round(-y2 + center[1]),
					color
				)




def clear_object(obj, scale=1, perspective_3d=True):
	render(obj, BLACK, scale, perspective_3d)
	
