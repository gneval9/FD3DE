import math as m

def relative_deg(p1, p2):

	v2 = (p2[0] - p1[0], p2[1] - p1[1])

	Mv2 = ((v2[0]**2) + (v2[1]**2)) ** 0.5


	cos_ang = v2[0] / Mv2

	angle = m.degrees(m.acos(cos_ang))

	return(angle)
