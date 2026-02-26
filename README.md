## FD3DE (FrameDirect 3D Engine)

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

cubo = fd3de.load("Modelos/cubo.fd3de")  # Cargar modelo 3D

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
cubo = fd3de.load("Modelos/cubo.fd3de")
```

---

### render(obj, color, scale=1)

Se encarga de renderizar el objeto guardado en una variable en la pantalla.

`obj (dict)` → Objeto cargado con **load()**.  
`color (str)` → Color en formato **ARGB** (en hexadecimal).  
`scale (int)` → Número por el que se multiplicará la escala del objeto (por defecto equivale a 1).

```python
fd3de.render(cubo, fd3de.RED, 2)
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

### clear_object(obj)

Redibuja el objeto sobre sí mismo en color negro para borrarlo (es más eficiente que pintar toda la pantalla de negro).

`obj (dict)` → Objeto a borrar.

```python
fd3de.clear_object(cubo)
```

---

### update()

Actualiza el framebuffer, mostrando todo lo que se haya renderizado con la función **render()**.

```python
fd3de.update()
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
