import fd3de
import curses
import atexit

print("(Para recargar el modelo introducido, pulsa 'l'.)")
modelo = input("Pon el nombre del archivo de la carpeta 'Modelos' sin la extensión: ")
scale = int(input("Introduzca la escala deseada (defecto = 1): "))

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

atexit.register(curses.endwin)

obj = None
ejes3D = fd3de.load("Modelos/ejes3D.fd3de")

fd3de.move("x", -500, ejes3D)
fd3de.move("y", 300, ejes3D)

def load(modelo):
	return fd3de.load(f"Modelos/{modelo}.fd3de")


def reload():
	global obj
	
	rotation = obj["rotation"].copy()
	obj = load(modelo)

	fd3de.rotate("x", rotation[0], obj)
	fd3de.rotate("y", rotation[1], obj)
	fd3de.rotate("z", rotation[2], obj)


obj = load(modelo)

while True:
	
	key = stdscr.getch()

	if key == curses.KEY_RIGHT:
		fd3de.rotate("y", -5, obj)
		fd3de.rotate("y", -5, ejes3D)
		curses.flushinp()

	elif key == curses.KEY_LEFT:
		fd3de.rotate("y", 5, obj)
		fd3de.rotate("y", 5, ejes3D)
		curses.flushinp()

	elif key == curses.KEY_DOWN:
		fd3de.rotate("x", -5, obj)
		fd3de.rotate("x", -5, ejes3D)
		curses.flushinp()

	elif key == curses.KEY_UP:
		fd3de.rotate("x", 5, obj)
		fd3de.rotate("x", 5, ejes3D)
		curses.flushinp()

	elif key == ord("l"):
		reload()

	fd3de.render(obj, fd3de.GREEN, scale)
	fd3de.render(ejes3D, fd3de.WHITE, 2, False)
	fd3de.update()
	fd3de.clear_object(obj, scale)
	fd3de.clear_object(ejes3D, 2, False)

	reload()
