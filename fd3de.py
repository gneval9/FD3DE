# Made and developed by gneval9 Software
# 24-02-2026

import framedirect as FD
import math as m
import ast
import atexit

FD.init()
atexit.register(FD.close)

screen_x = FD.screen_width
screen_y = FD.screen_height

center = (screen_x // 2, screen_y // 2)

f = 330		# Distáncia focal
camera_offset = 300	# Distancia de la cámara

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


def load(path):
	with open(path, "r") as f:
		file = ast.literal_eval(f.read())

	return {
		"original": file,
		"rotation": [0, 0, 0],
		"position": [0, 0, 0]
	}


def update():
	FD.update()


def get_center(obj):
	cx = 0
	cy = 0
	cz = 0

	for v in obj:
		cx += v[0]
		cy += v[1]
		cz += v[2]

	cx = cx / len(obj)
	cy = cy / len(obj)
	cz = cz / len(obj)

	return (cx, cy, cz)


def move_x(dist_x, obj):
	obj["position"][0] += dist_x


def move_y(dist_y, obj):
	obj["position"][1] += dist_y


def move_z(dist_z, obj):
	obj["position"][2] += dist_z


def rotate_x(angle, obj):
	obj["rotation"][0] += angle


def rotate_y(angle, obj):
	obj["rotation"][1] += angle


def rotate_z(angle, obj):
	obj["rotation"][2] += angle


def render(obj, color):

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

		x, y, z = v[0], v[1], v[2]

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

		if z <= 1:
			projected.append(None)
			continue

		Px = (f * x) / z
		Py = (f * y) / z

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


def clear_object(obj):
	render(obj, BLACK)
