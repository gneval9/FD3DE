import FD_FontLoader as FL
import framedirect as FD

FL.load_font("./VeFont.txt")

def write(sentence, x, y, scale=1, color=FD.RED):
	for n in range(len(sentence)):
		if sentence[n] != " ":
			if n == 0:
				FL.draw_char(sentence[n], x-scale, y, scale, color)
			else:
				FL.draw_char(sentence[n], x+(scale*5*n), y, scale, color)
		else:
			FD.draw_line(x+(scale*5*n), y, x+(scale*5*n)+scale, y, FD.BLACK)



