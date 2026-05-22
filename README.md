## FD3DE (FrameDirect 3D Engine) - V0.10.1

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

## Uso básico

```python
import fd3de

cubo_load = fd3de.load("Modelos/cubo.fd3de")  # Cargar modelo 3D
cubo = fd3de.spawn(cubo) 	# Spawnear modelo 3D

fd3de.move("x", -170, cubo)                 # Mover el modelo -170 unidades en el eje X

while True:
    fd3de.rotate("y", 2, cubo)              # Rotar el modelo 2 grados en el eje Y

    fd3de.render(cubo, fd3de.YELLOW)     # Renderizar el modelo de color amarillo
    fd3de.update()                       # Actualizar el framebuffer

    fd3de.clear_object(cubo)             # Borrar el modelo (redibujando por encima suyo)
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

Carga el modelo 3D desde una variable. Es esta la que se utilizará en funciones como `render()` o `rotate()`.  

`model (list)` → Variable en la que se ha cargado el modelo con `load()`.  

```python
cubo = fd3de.spawn(cubo_load)  
```

---

### render(obj, color, scale=1, perspective=True)

Se encarga de renderizar el objeto guardado en una variable en la pantalla.

`obj (dict)` → Objeto cargado con **load()**.  
`color (int)` → Color en formato **ARGB** hexadecimal (ej.: 0x486F6C61).  
`scale (float)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).  
`perspective (boolean)` → Indica si se aplicará efecto de perspectiva o no al modelo renderizado.

```python
fd3de.render(cubo, fd3de.RED, 2, True)
```

---

### move(axis, dist, obj)

Mueve el objeto un número determinado de píxeles.

`axis (str)` → Eje en el que se moverá (opciones válidas: "x", "y" y "z").  
`dist (int)` → Número de píxeles que el objeto se desplazará.  
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

### clear_object(obj, scale=1, perspective=True)

Redibuja el objeto sobre sí mismo en color negro para borrarlo (es más eficiente que pintar toda la pantalla de negro).
Como utiliza directamente la función `render()` para eso, requiere tener los mismos argumentos que esta para funcionar correctamente.

`obj (dict)` → Objeto a borrar.  
`scale (float)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).  
`perspective (boolean)` → Indica si se aplicará efecto de perspectiva o no al modelo renderizado.  


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
fd3de.utils.relative_dist_3D((2,3), (5,4))
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
