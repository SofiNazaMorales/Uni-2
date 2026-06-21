# Calculadora de Ruta más corta entre Ciudades de Japón
Proyecto realizado para la asignatura de Matemática Discreta.

# Repositorio
En los archivos adjuntos se encuentran:

_Codigo fuente_  `mate_discreta_.py ` : programa de python del proyecto

_Requerimientos_  `requirements.txt ` : bibliotecas necesarias para ejecutar

_Fuentes de datos utilizados_  ` datos_grafo.csv ` : archivo que almacena las ciudades y distancias utilizadas

# Descripción
Este programa permite encontrar la ruta más corta entre ciudades de Japón utilizando el algoritmo de Dijkstra.
El usuario puede seleccionar una ciudad de origen y una ciudad de destino mediante una interfaz gráfica. Luego, el programa muestra la ruta encontrada, la distancia total recorrida y la cantidad de ciudades por las que pasa el recorrido.
También es posible visualizar el grafo completo de ciudades y conexiones.

# Librerías utilizadas
* tkinter
* networkx
* matplotlib

## Cómo ejecutar

1. Instalar las librerías necesarias:

```
pip install -r requirements.txt
```

2. Ejecutar el archivo principal:

```
python mate_discreta_.py
```

# Funcionamiento
Cada ciudad está conectada con otras ciudades mediante rutas que tienen una distancia asociada.
El algoritmo de Dijkstra analiza las distintas alternativas posibles y determina cuál es la ruta con menor distancia entre el origen y el destino seleccionados.

# Estructura del codigo
El archivo `mate_discreta_.py` esta organizado en bloques:

- **Bloque 1 - Datos del grafo**
- **Bloque 2 - Funciones del algoritmo**: implementacion manual de Dijkstra.
- **Bloque 3 - Funciones de visualizacion**
- **Bloque 4 - Funciones de interfaz**
- **Bloque 5 - Ventana principal**

# Integrantes
- Vicente Barrientos
- Diego Vasquez
- Macarena Melin
- Sofía Morales
