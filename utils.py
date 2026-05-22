# Made and developed by gneval9 Software
# 22-05-2026
# V0.9.0

import math as m


def relative_deg(p1, p2):
	x = p2[0] - p1[0]
	y = p2[1] - p1[1]

	angle = m.degrees(m.atan2(y, x))

	return(round(angle, 2))


def relative_dist_3D(p1, p2):
	vector = vector3D(p1, p2)

	dist = vect_magnitude_3D(vector)

	return(dist)


def relative_dist_2D(p1, p2):
	vector = vector_2D(p1, p2)

	dist = vect_magnitude_2D(vector)

	return(dist)



def vector3D(p1, p2):	
	vect = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
	
	return(vect)



def vector2D(p1, p2):	
	vect = (p2[0] - p1[0], p2[1] - p1[1])

	return(vect)



def vect_magnitude_3D(vector):
	mag = ((vector[0]**2) + (vector[1]**2) + (vector[2]**2)) ** 0.5

	return(mag)


def vect_magnitude_2D(vector):
	mag = ((vector[0]**2) + (vector[1]**2)) ** 0.5

	return(mag)


def normalize3D(vector):
	mag = vect_magnitude_3D(vector)
	
	if mag == 0:
		return((0,0,0))
	else:
		norm_vect = (
			vector[0] / mag, 
			vector[1] / mag, 
			vector[2] / mag
			)

		return(norm_vect)


def normalize2D(vector):
	mag = vect_magnitude_2D(vector)
	
	if mag == 0:
		return((0,0))
	else:
		norm_vect = (
			vector[0] / mag,
			vector[1] / mag
			)

		return(norm_vect)



def clamp(val, min_val, max_val):
	if min_val <= val <= max_val:
		return(val)

	elif val < min_val:
		return(min_val)
	
	elif val > max_val:
		return(max_val)


