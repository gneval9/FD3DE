import fd3de
import time

cubo = fd3de.load("Modelos/cubo.fd3de")
pir = fd3de.load("Modelos/piramide.fd3de")

fd3de.move_x(-170, cubo)
fd3de.move_x(170, pir)
fd3de.move_z(50, pir)

while True:
    fd3de.rotate_y(2, cubo)
    fd3de.rotate_y(-3, pir)
    
    #fd3de.move_z(15, pir)
    

    fd3de.render(cubo, fd3de.YELLOW)
    fd3de.render(pir, fd3de.CYAN)
    fd3de.update()
    fd3de.clear_object(cubo)
    fd3de.clear_object(pir)
