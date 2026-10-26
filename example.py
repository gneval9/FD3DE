import fd3de
import time

cubo_l = fd3de.load("Modelos/cubo.fd3de")
pir_l = fd3de.load("Modelos/piramide.fd3de")

cubo = fd3de.spawn(cubo_l)
pir = fd3de.spawn(pir_l)

fd3de.move("x", -170, cubo)
fd3de.move("x", 170, pir)

while True:
	fd3de.rotate("y", 2, cubo)
	fd3de.rotate("y", -3, pir)

	fd3de.render(cubo, fd3de.YELLOW)
	fd3de.render(pir, fd3de.CYAN)

	fd3de.update()

	fd3de.clear_object(cubo)
	fd3de.clear_object(pir)
