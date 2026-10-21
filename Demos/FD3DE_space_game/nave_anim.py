import fd3de
import threading
import FD_FontLoader as FL
import FDWriter as FDW
import framedirect as FD

FD.init()

screen_x, screen_y = FD.screen_width, FD.screen_height

FL.load_font("VeFont.txt")

nave_load = fd3de.load("Modelos/nave.fd3de")
cubo_load = fd3de.load("Modelos/cubo.fd3de")

nave = fd3de.spawn(nave_load)
cubo = fd3de.spawn(cubo_load)


FDW.write("FD3DE", 150, 100, 10)
FDW.write("SpaceGame", 80, 180, 10)

FDW.write("Made and developed by", screen_x - 610, 50, 3) 
FDW.write("gneval9 Software", screen_x - 600, 120, 7) 
FDW.write("In 03-2026", screen_x - 550, 180, 2) 


fd3de.move("y", -200, cubo)
fd3de.move("y", -50, nave)
fd3de.move("x", 100, cubo)
fd3de.move("x", 100, nave)
fd3de.move("z", -50, nave)

fd3de.rotate("y", 50, nave)
fd3de.rotate("x", -5, nave)

def render_all():
	fd3de.render(cubo, fd3de.WHITE)
	fd3de.render(nave, fd3de.RED, 2)
	fd3de.update()

	fd3de.clear_object(cubo)
	fd3de.clear_object(nave, 2)




def subir():
	for n in range(50):
		fd3de.move("y", 2, nave)
		render_all()

def rotar_y():
	for n in range(50):
		fd3de.rotate("y", 2, nave)
		render_all()


def rotar_x():
	for n in range(15):
		fd3de.rotate("x", 2, nave)
		render_all()


def irse_a_tomar_por_culo():
	for n in range(60):
		fd3de.move("z", 20, nave)
		fd3de.move("x", -10, nave)
		fd3de.move("y", 5, nave)
		
		fd3de.rotate("z", -0.1, nave)
		render_all()

subir()
rotar_y()
rotar_x()
irse_a_tomar_por_culo()
