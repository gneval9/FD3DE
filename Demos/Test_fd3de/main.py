# Made and developed by gneval9 Software
# 22-10-2026

import fd3de
import keyboard
import FDWriter
import framedirect as FD
import random
import os
import time

nave = fd3de.spawn(fd3de.load("Modelos/nave.fd3de"))
plano = fd3de.spawn(fd3de.load("Modelos/plano.fd3de"))
cubo = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
cubo2 = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
cubo3 = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
mini_plano = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
hitbox = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))

fd3de.scene_new("main")

fd3de.scene_add("main", nave, fd3de.RED, 1, True)
fd3de.scene_add("main", plano, fd3de.GREEN, 1)

fd3de.scene_add("main", cubo, fd3de.YELLOW)
fd3de.scene_add("main", cubo2, fd3de.MAGENTA)
fd3de.scene_add("main", cubo3, fd3de.CYAN)





fd3de.rotate("y", 180, nave)

fd3de.move("z", -100, nave)
fd3de.move("y", -100, nave)


fd3de.move("y", -150, plano)



fd3de.move("z", 600, cubo)
fd3de.move("z", 600, cubo2)
fd3de.move("z", 600, cubo3)

cubo["position"][0] = random.randint(-400, 400)
cubo["position"][1] = random.randint(-50, 100)

cubo2["position"][0] = random.randint(-400, 400)
cubo2["position"][1] = random.randint(-50, 100)

cubo3["position"][0] = random.randint(-400, 400)
cubo3["position"][1] = random.randint(-50, 100)






mini_plano["position"][1] = nave["position"][1]
fd3de.move("z", -100, mini_plano)

fd3de.move("z", -100, hitbox)





god_mode = False
debug = False
cubos = [cubo, cubo2, cubo3]

nave_speed_x = 0
nave_speed_y = 0

g = 9.81
top = -100





def render():
    fd3de.render_scene("main")        
       
  



while True:
     
    # Keyboard Inputs
    # ---------------

    if keyboard.is_pressed("right"):
        nave_speed_x += 2
        nave["rotation"][2] = -20
   
    elif keyboard.is_pressed("left"):
        nave_speed_x -= 2
        nave["rotation"][2] = 20

    else:
        nave["rotation"][2] = 0




    if keyboard.is_pressed("down"):
        nave_speed_y += 3
        nave["rotation"][0] = 20

    else:
        nave["rotation"][0] = 0


    if keyboard.is_pressed("g"):
        debug = not debug
        time.sleep(0.05)
    
        if debug == True:
            fd3de.scene_add("main", mini_plano, fd3de.WHITE, 0.2)
            fd3de.scene_add("main", hitbox, fd3de.GREEN, 0.2)
        elif debug == False:
            fd3de.scene_del("main", mini_plano)
            fd3de.scene_del("main", hitbox)

    if keyboard.is_pressed("o"):
        god_mode = not god_mode
        time.sleep(0.05)




    
    # Logic
    # -----

    mini_plano["position"][0] = nave["position"][0]
    
    hitbox["position"][0] = nave["position"][0]
    hitbox["position"][1] = nave["position"][1]


    fd3de.move("z", -5, cubo)
    fd3de.move("z", -4, cubo2)
    fd3de.move("z", -6, cubo3)

    if cubo["position"][2] < -100:
        fd3de.move("z", 600, cubo)
        cubo["position"][0] = random.randint(-400, 400)
        cubo["position"][1] = random.randint(-50, 100)

    if cubo2["position"][2] < -100:
        fd3de.move("z", 600, cubo2)
        cubo2["position"][0] = random.randint(-400, 400)
        cubo2["position"][1] = random.randint(-50, 100)

    if cubo3["position"][2] < -100:
        fd3de.move("z", 600, cubo3)
        cubo3["position"][0] = random.randint(-400, 400)
        cubo3["position"][1] = random.randint(-50, 100)






    # Colisions
    # ---------

    if god_mode == False:

        for n in range(len(cubos)):
            if hitbox["position"][2] >= cubos[n]["position"][2] - 150 and hitbox["position"][2] <= cubos[n]["position"][2] + 100:   #z
                if hitbox["position"][0] >= cubos[n]["position"][0] -100 and hitbox["position"][0] <= cubos[n]["position"][0] + 100: #x
                    if hitbox["position"][1] >= cubos[n]["position"][1] -100 and hitbox["position"][1] <= cubos[n]["position"][1] + 100: #y
                        os.system("clear")
                        print(f"COLISION WITH CUBE AT ({cubos[n]["position"][0]}, {cubos[n]["position"][1]}, {cubos[n]["position"][2]})")
                        exit()


    # Wall colisions
    # --------------

    if nave["position"][0] < -260:
        nave["position"][0] = -260
        nave_speed_x = 0
    

    if nave["position"][0] > 260:
        nave["position"][0] = 260
        nave_speed_x = 0
   

    if nave["position"][1] > 200:
        nave["position"][1] = 200
        nave_speed_y = 0





    # Physics
    # -------

    nave_speed_y += -g / 10
    nave["position"][1] += nave_speed_y
    nave["position"][0] += nave_speed_x
       
    if nave_speed_x > 0:
        nave_speed_x += -0.5
    
    elif nave_speed_x < 0:
        nave_speed_x += 0.5



    if nave["position"][1] < top:
        nave["position"][1] = top
        nave_speed_y = 0
    




    # Debug
    # -----
    
    if debug == True:

        FDWriter.write(f"god_mode: {god_mode}", 60, 60, 2, FD.WHITE, True)

        FDWriter.write(f"nave_speed_x: {round(nave_speed_x)}", 60,100, 2, FD.WHITE, True)
        FDWriter.write(f"nave_speed_y: {round(nave_speed_y)}", 60,120, 2, FD.WHITE, True)

        FDWriter.write(f"nave_coord_x: {round(nave["position"][0])}", 60,140, 2, FD.WHITE, True)
        FDWriter.write(f"nave_coord_y: {round(nave["position"][1])}", 60,160, 2, FD.WHITE, True)


    render()

    if debug == True:

        FDWriter.write(f"god_mode: {god_mode}", 60, 60, 2, FD.BLACK, True)

        FDWriter.write(f"nave_speed_x: {round(nave_speed_x)}", 60,100, 2, FD.BLACK, True)
        FDWriter.write(f"nave_speed_y: {round(nave_speed_y)}", 60,120, 2, FD.BLACK, True)

        FDWriter.write(f"nave_coord_x: {round(nave["position"][0])}", 60,140, 2, FD.BLACK, True)
        FDWriter.write(f"nave_coord_y: {round(nave["position"][1])}", 60,160, 2, FD.BLACK, True)

    
