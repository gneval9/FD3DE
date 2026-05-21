import math as m

def relative_deg(p1, p2):

	v2 = (p2[0] - p1[0], p2[1] - p1[1])

	Mv2 = ((v2[0]**2) + (v2[1]**2)) ** 0.5


	cos_ang = v2[0] / Mv2

	angle = m.degrees(m.acos(cos_ang))

	return(round(angle, 2))




def relative_dis(p1, p2):

	x1, y1, z1 = p1
	x2, y2, z2 = p2

	vector = (x2-x1, y2-y1, z2-z1)

	dist = ((vector[0]**2) + (vector[1]**2) + (vector[2]**2)) ** 0.5

	return(dist)



def vector2D(p1, p2):
	
	vect = (p2[0] - p1[0], p2[1] - p1[1])

	return(vect)




def vector3D(p1, p2):
	
	vect = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
	
	return(vect)
