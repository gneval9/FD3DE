## FD3DE (FrameDirect 3D Engine)

**FD3DE** es un motor 3D programado en Python3 que utiliza **FrameDirect** para el renderizado en **framebuffer**.
La librería permite renderizar figuras 3D creadas por el usuario.

Este paquete no incluye modelos 3D predefinidos.
Los modelos de ejemplo pueden encontrarse en el repositorio oficial:

https://github.com/gneval9/FD3DE

## Requisitos
- Linux con framebuffer habilitado y acceso a `/dev/fb0`
- FrameDirect instalado y actualizado

## Instalación
```bash
pip install fd3de
```

## Uso básico
```python
import fd3de

cubo = fd3de.load("Modelos/cubo.fd3de") # Cargar modelo 3D

fd3de.move_x(-170, cubo) 				# Mover el modelo -170 unidades en el eje X


while True:
	fd3de.rotate_y(2, cubo)				# Rotar el modelo 2 grados en el eje Y

	fd3de.render(cubo, fd3de.YELLOW)	# Renderizar el modelo de color amarillo
	fd3de.update()						# Actualizar el framebuffer

	fd3de.clear_object(cubo)			# Borrar el modelo (redibujando por encima suyo)
```



## Funciones
### load(path) 
Sirve para cargar un modelo. Se asigna a una variable como se muestra a continuación.

`path (str)` = Ruta del archivo del modelo.

```python
cubo = fd3de.load("Modelos/cubo.fd3de")
```


### render(obj, color, scale=1)
Se encarga de renderizar el objeto guardado en una variable en la pantalla.

`obj (dict)` = Objeto cargado con **load()**.

`color (str)` = Color en formato **ARGB** (en hexadecimal).

`scale (int)` = Número por el que se multiplicará la escala del objeto. (Por defecto equivale a 1)
```python
fd3de.render(cubo, fd3de.RED, 2)
```


### move(axis, dist, obj)
Mueve el objeto un número determinado de píxeles.

`axis (str)` = El eje en el que se moverá. (Opciones válidas: "x", "y" y "z")

`dist (int)` = Número de píxeles que el objeto se desplazará.

`obj (dict)` = El objecto a mover.

```python
fd3de.move("x", 50, cubo)
```


### rotate(axis, angle, obj)
Rotar el objeto un número determinado de grados.

`axis (str)` = El eje en el que se rotará. (Opciones válidas: "x", "y" y "z")

`angle (int)` = Número de grados que el objeto rotará.

`obj (dict)` = El objecto a rotar.

```python
fd3de.rotate("y", 35, cubo)
```

### clear_object(obj)
Redibuja el objeto sobre sí mismo de color negro para borarlo. (És más eficiente que pintar toda la pantalla de negro)

`obj (dict)` = El objeto a borrar.
```python
fd3de.clear_object(cubo)
```


### update()
Actualiza el framebuffer.
