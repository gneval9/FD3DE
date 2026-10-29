## FD3DE (FrameDirect 3D Engine) - V0.21.0

**FD3DE** es un motor 3D programado en Python3 que utiliza **FrameDirect** para el renderizado en **framebuffer**.  
La librería permite renderizar figuras 3D creadas por el usuario.

Este paquete no incluye modelos 3D predefinidos.  
Los modelos de ejemplo pueden encontrarse en el repositorio oficial:

https://github.com/gneval9/FD3DE

---

## Requisitos

- Linux con framebuffer habilitado y acceso a `/dev/fb0`
- FrameDirect instalado y actualizado

---

## Instalación

```bash
pip install fd3de
```

---
## Uso básico (Con scene)
```python
import fd3de

cubo_load = fd3de.load("Modelos/cubo.fd3de")                      # Cargar el modelo 3D
cubo = fd3de.spawn(cubo_load)                                     # Crear una instancia del modelo 3D

fd3de.scene_new("EscenaPrincipal")                                # Crear la escena "EscenaPrincipal"

fd3de.scene_add("EscenaPrincipal", cubo, fd3de.YELLOW)            # Añadir la instancia a la escena

fd3de.move("x", -170, cubo)                                       # Mover el modelo -170 unidades en el eje X

while True:
    fd3de.rotate("y", 2, cubo)                                    # Rotar el modelo 2 grados en el eje Y

    fd3de.render_scene("EscenaPrincipal")                         # Renderizar la escena

```

## Uso básico (Sin scene)

```python
import fd3de

cubo_load = fd3de.load("Modelos/cubo.fd3de")                      # Cargar modelo 3D
cubo = fd3de.spawn(cubo_load) 	                                  # Crear una instancia del modelo 3D

fd3de.move("x", -170, cubo)                                       # Mover el modelo -170 unidades en el eje X

while True:
    fd3de.rotate("y", 2, cubo)                                    # Rotar el modelo 2 grados en el eje Y

    fd3de.render(cubo, fd3de.YELLOW, 2, True)                     # Renderizar el modelo en amarillo
    fd3de.update()                                                # Actualizar el framebuffer

    fd3de.clear_object(cubo, 2, True)                             # Borrar el modelo (redibujando en negro por encima suyo)
```

---

## Funciones

### load(path)

Sirve para cargar un modelo. Se asigna a una variable como se muestra a continuación.

`path (str)` → Ruta del archivo del modelo.

```python
cubo_load = fd3de.load("Modelos/cubo.fd3de")
```
---

### spawn(model)

Crea una instancia del modelo a partir de un modelo previamente cargado con `load()`. La instancia que devuelve es la que se utiliza después en funciones como `render()` o `rotate()`. 

`model (list)` → Variable en la que se ha cargado el modelo con `load()`.  

```python
cubo = fd3de.spawn(cubo_load)  
```
La instancia está formada por un diccionario con tres elementos: `["original"]`, `["position"]` y `["rotation"]`.


`["original"]` contiene la geometría original del modelo cargado. No hay necesidad ninguna de tocar esto.  
`["position"]` contiene una lista con tres elementos, que representan la posición del objeto en los tres ejes.  
`["rotation"]` contiene una lista con tres elementos, que representan la orientación del objeto en los tres ejes. Estos están en grados sexagesimales.

```python
cubo["position"][0] = 200  #Asigna el valor 200 a la posición de cubo en el eje X
```


---
### scene_new(scene)

Crea una escena con el nombre asignado. Una escena alberga una serie de modelos 3D, los cuales pueden ser renderizados de una sola vez. Se pueden
tener varias escenas y renderizarlas por separado. El nombre "ALL" está reservado. En caso de ser utilizado se lanzará un `ValueError`.

`scene (str)` → Nombre de la escena.

```python
fd3de.scene_new("EscenaPrincipal")
```

### scene_rm(scene)

Borra la escena especificada.

`scene (str)` → Nombre de la escena.

```python
fd3de.scene_rm("EscenaPrincipal")
```

---
### scene_add(scene, obj, color, scale=1, perspective_3d=True)

Añade la instancia del modelo dado a la escena indicada. No se puede añadir el mismo objeto a la escena más de una vez.
En ese caso, se lanzará un `ValueError`.

`scene (str)` → Nombre de la escena.
`obj (dict)` → Objeto cargado con `spawn()`.  
`color (int)` → Color en formato **ARGB** hexadecimal (ej.: 0x486F6C61).  
`scale (float)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).  
`perspective_3d (boolean)` → Indica si se aplicará efecto de perspectiva o no al modelo renderizado.

```python
fd3de.scene_add("EscenaPrincipal", cubo, fd3de.RED, 3, True)
```
---
### scene_del(scene, obj)

Borra el objeto dado de la escena. La función comprueba si `obj` es la misma instancia que un objeto registrado en la escena. Si encuentra una coincidencia, elimina el objeto de la pantalla y lo retira de la escena.

`scene (str)` → Nombre de la escena.
`obj (dict)` → Objeto cargado con `spawn()`.

```python
fd3de.scene_del("EscenaPrincipal", cubo)
```
---
### scene_move_all(axis, dist, scene)

Permite mover todos los objetos de una escena concreta. Internamente utiliza `move()`.

`axis (str)` → Eje en el que se moverá (opciones válidas: "x", "y" y "z").  
`dist (int)` → Número de unidades que el objeto se desplazará.  
`scene (str)` → Escena a mover.  

```python
fd3de.scene_move_all("x", -170, "EscenaPrincipal")
```


---

### scene_orbit_all(axis, angle, scene, target)

Esta función hace que `scene` orbite alrededor de `target` en el eje especificado.

`axis (str)` → Eje en el que orbitará (opciones válidas: "x", "y" y "z").  
`dist (int)` → Número de unidades que la escena orbitará.  
`scene (str)` → Escena que orbitará.
`target (dict)` → Objeto a orbitar.

```python
fd3de.scene_orbit_all("y", 40, "EscenaPrincipal", cubo)
```
---
### scene_contains(scene, obj)
Comprueba si el objeto dado existe en la escena en cuestión. Devuelve `True` o `False` en
función de si existe o no.

`scene (str)` → Nombre de la escena.
`obj (dict)` → Objeto cargado con `spawn()`.

```python
fd3de.scene_contains("EscenaPrincipal", cubo)
```


---
### render_scene(scene)

Al llamar a esta función, se renderizan todos los objetos registrados en la escena dada. A continuación, se actualiza el framebuffer mediante `update()` y, finalmente, se borran las representaciones de los objetos dibujando sus aristas en negro con `clear_object()`. Esto simplifica el renderizado de escenas animadas, ya que no es necesario borrar manualmente cada objeto.

`scene (str)` → Nombre de la escena.

```python
fd3de.render_scene("EscenaPrincipal")
```
Si a la función se le pasa como argumento `fd3de.ALL`, se renderizarán todas las escenas existentes.

```python
fd3de.render_scene(fd3de.ALL)
```


---

### render(obj, color, scale=1, perspective_3d=True)

Se encarga de renderizar el objeto guardado en una variable en la pantalla.

`obj (dict)` → Objeto cargado con `spawn()`.  
`color (int)` → Color en formato **ARGB** hexadecimal (ej.: 0x486F6C61).  
`scale (float)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).  
`perspective_3d (boolean)` → Indica si se aplicará efecto de perspectiva o no al modelo renderizado.

```python
fd3de.render(cubo, fd3de.RED, 2, True)
```

---
### key_input(key)

Permite comprobar si la tecla especificada está siendo pulsada o no, devolviendo un booleano. Internamente utiliza `keyboard.is_pressed`.

`key (str)` → Tecla a comprobar

```python
fd3de.key_input("g")
```


---
### move(axis, dist, obj)

Mueve el objeto un número determinado de unidades.

`axis (str)` → Eje en el que se moverá (opciones válidas: "x", "y" y "z").  
`dist (int)` → Número de unidades que el objeto se desplazará.  
`obj (dict)` → Objeto a mover.

```python
fd3de.move("x", 50, cubo)
```

---

### rotate(axis, angle, obj)

Rota el objeto un número determinado de grados.

`axis (str)` → Eje en el que se rotará (opciones válidas: "x", "y" y "z").  
`angle (int)` → Número de grados que el objeto rotará.  
`obj (dict)` → Objeto a rotar.

```python
fd3de.rotate("y", 35, cubo)
```

---
### orbit(axis, angle, obj, target)

Esta función hace que `obj` orbite alrededor de `target` en el eje especificado.

`axis (str)` → Eje en el que orbitará (opciones válidas: "x", "y" y "z").  
`dist (int)` → Número de unidades que el objeto orbitará.  
`obj (dict)` → Objeto que orbitará.
`target (dict)` → Objeto a orbitar.

```python
fd3de.orbit("y", 40, nave, cubo)
```


---
### clear_object(obj, scale=1, perspective_3d=True)

Redibuja el objeto sobre sí mismo en color negro para borrarlo (es más eficiente que pintar toda la pantalla de negro).
Internamente, utiliza la función `render()` con el color negro, por lo que acepta los mismos parámetros que esta, excepto `color`.
En caso de que dos modelos estén superpuestos, cuando se borre uno de los dos objetos, se pintará de negro por encima del otro modelo,
dejando su silueta marcada sobre los píxeles coincidentes. Este efecto solo se ve en el fotograma en el que se ejecuta el borrado
así que será prácticamente imperceptible.

`obj (dict)` → Objeto a borrar.  
`scale (float)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).  
`perspective_3d (boolean)` → Indica si se aplicará efecto de perspectiva o no al modelo renderizado.  


```python
fd3de.clear_object(cubo, 0.3, False)
```

---

### update()

Actualiza el framebuffer, mostrando todo lo que se haya renderizado con la función **render()**.

```python
fd3de.update()
```

---
## Colores

FD3DE viene con varios colores predeterminados para usarlos de forma cómoda en lugar de utilizar los
códigos hexadecimales.

```python
fd3de.RED
fd3de.GREEN
fd3de.BLUE
fd3de.WHITE
fd3de.BLACK
fd3de.YELLOW
fd3de.CYAN
fd3de.MAGENTA
fd3de.GRAY
fd3de.ORANGE
```


---
## Utilidades

FD3DE incluye una serie de funciones pensadas para facilitar tareas comunes durante el desarrollo de videojuegos, especialmente relacionadas con matemáticas, vectores y cálculos espaciales.

Todas las utilidades se encuentran dentro del módulo `utils` y se utilizan mediante:

```python
fd3de.utils.X()
```
---

### relative_deg(p1, p2)

Devuelve el ángulo en grados entre el eje X positivo y el vector que va de `p1` a `p2`, en el plano XY (2D).

`p1 (tuple)` → Punto 2D inicial (x, y)  
`p2 (tuple)` → Punto 2D final (x, y)  

```python
fd3de.utils.relative_deg((2,5), (4,1))
```

---

### relative_dist_3D(p1, p2)

Devuelve la distancia 3D entre los puntos `p1` y `p2` 

`p1 (tuple)` → Punto 3D inicial (x, y, z)  
`p2 (tuple)` → Punto 3D final (x, y, z)

```python
fd3de.utils.relative_dist_3D((1,5,3), (7,3,4))
```

---

### relative_dist_2D(p1, p2)

Devuelve la distancia 2D entre los puntos `p1` y `p2` 

`p1 (tuple)` → Punto 2D inicial (x, y)  
`p2 (tuple)` → Punto 2D final (x, y)
 
```python
fd3de.utils.relative_dist_2D((2,3), (5,4))
```
---
### vector3D(p1, p2)

Devuelve un vector 3D que va desde `p1` hasta `p2`.

`p1 (tuple)` → Punto 3D inicial (x, y, z)  
`p2 (tuple)` → Punto 3D final (x, y, z)

```python
fd3de.utils.vector3D((3,4,8), (1,6,3))
```

---
### vector2D(p1, p2)

Devuelve un vector 2D que va desde `p1` hasta `p2`.

`p1 (tuple)` → Punto 2D inicial (x, y)  
`p2 (tuple)` → Punto 2D final (x, y)

```python
fd3de.utils.vector2D((3,8), (6,9))
```

---
### vect_magnitude_3D(vector)

Devuelve la magnitud del vector en 3D.

`vector (tuple)` → Vector 3D (x, y, z)

```python
fd3de.utils.vect_magnitude_3D((5,1,2))
```

---
### vect_magnitude_2D(vector)

Devuelve la magnitud del vector en 2D.

`vector (tuple)` → Vector 2D (x, y)

```python
fd3de.utils.vect_magnitude_2D((7,5))
```
---
### normalize3D(vector)

Convierte un vector 3D en un vector unitario.

`vector (tuple)` → Vector 3D a normalizar

```python
fd3de.utils.normalize3D((6,4,2))
```
---

### normalize2D(vector)

Convierte un vector 2D en un vector unitario.

`vector (tuple)` → Vector 2D a normalizar

```python
fd3de.utils.normalize2D((1,2))
```

---

### clamp(val, min_val, max_val)

Limita el valor de `val` al rango definido entre `min_val` y `max_val`.

`val (int | float)` → Valor a limitar  
`min_val (int | float)` → Valor mínimo permitido  
`max_val (int | float)` → Valor máximo permitido  

```python
fd3de.utils.clamp(3, 2, 8)
```

---

## ¿Cómo crear modelos para FD3DE?

Un modelo 3D de FD3DE se compone de una lista en la que se especifica la posición de cada punto en sus tres ejes y los vértices a los que se tiene que unir mediante líneas.

```python
[
    [100, -100, -100, 1, 4],  # 0
    [-100, -100, -100, 2, 5], # 1
    [-100, -100, 100, 3, 6],  # 2
    [100, -100, 100, 0, 7],   # 3
    [100, 100, -100, 5],      # 4
    [-100, 100, -100, 6],     # 5
    [-100, 100, 100, 7],      # 6
    [100, 100, 100, 4]        # 7
]
```

Como se puede ver, no es más que una lista con más listas, donde los tres primeros parámetros son las coordenadas 3D y los siguientes son los vértices con los que este punto se tiene que unir.

Formato:

```
[x, y, z, v1, v2...]
```

El archivo se deberá guardar con la extensión `.fd3de` y se cargará utilizando la función **load()**, pasando como parámetro la ruta del archivo.
