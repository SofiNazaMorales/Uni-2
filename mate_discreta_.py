# Integrantes:
#  - Vicente Barrientos
#  - Diego Vasquez
#  - Macarena Melin
#  - Sofía Morales

import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# BLOQUE 1: DATOS DEL GRAFO

grafo = {
    "Tokio": {}, "Yokohama": {}, "Osaka": {}, "Kioto": {}, "Nagoya": {},
    "Sapporo": {}, "Fukuoka": {}, "Kobe": {}, "Hiroshima": {}, "Sendai": {},
    "Nagasaki": {}, "Nara": {}, "Kanazawa": {}, "Nikko": {}, "Okinawa": {}
}

# Funcion para agregar la conexion en ambos sentidos (grafo no dirigido).
def agregar_conexion(ciudad_a, ciudad_b, distancia_km):
    grafo[ciudad_a][ciudad_b] = distancia_km
    grafo[ciudad_b][ciudad_a] = distancia_km


# Lista de conexiones del grafo
agregar_conexion("Tokio", "Yokohama", 30)  #distancia en km desde ayuntamientos como punto de referencia central jeje
agregar_conexion("Tokio", "Nikko", 110)
agregar_conexion("Tokio", "Sendai", 310)
agregar_conexion("Tokio", "Nagoya", 260)
agregar_conexion("Tokio", "Osaka", 400)
agregar_conexion("Yokohama", "Nagoya", 250)
agregar_conexion("Sendai", "Sapporo", 530)
agregar_conexion("Nagoya", "Kioto", 110)
agregar_conexion("Nagoya", "Kanazawa", 160)
agregar_conexion("Kioto", "Osaka", 40)
agregar_conexion("Kioto", "Nara", 40)
agregar_conexion("Kioto", "Kanazawa", 190)
agregar_conexion("Osaka", "Kobe", 30)
agregar_conexion("Osaka", "Nara", 30)
agregar_conexion("Osaka", "Hiroshima", 280)
agregar_conexion("Kobe", "Hiroshima", 250)
agregar_conexion("Hiroshima", "Fukuoka", 210)
agregar_conexion("Fukuoka", "Nagasaki", 110)
agregar_conexion("Fukuoka", "Okinawa", 860)
agregar_conexion("Nagasaki", "Okinawa", 760)
agregar_conexion("Kanazawa", "Nikko", 270)
agregar_conexion("Nara", "Nagoya", 110)
agregar_conexion("Sapporo", "Tokio", 830)
agregar_conexion("Nikko", "Sendai", 200)
agregar_conexion("Hiroshima", "Nagasaki", 300)
agregar_conexion("Okinawa", "Tokio", 1550)

# BLOQUE 2: FUNCIONES DEL ALGORITMO (DIJKSTRA)
# Funcion 1: inicializa el diccionario de distancias.
def inicializar_distancias(grafo, origen):
    distancias = {}
    for ciudad in grafo:
        distancias[ciudad] = float("inf")
    distancias[origen] = 0
    return distancias
# Funcion 2: busca, entre las ciudades no visitadas, la que
# tiene la menor distancia acumulada hasta el momento.
def buscar_nodo_minimo(distancias, visitados):
    ciudad_minima = None
    menor_distancia = float("inf")
    for ciudad in distancias:
        if ciudad not in visitados:
            if distancias[ciudad] < menor_distancia:
                menor_distancia = distancias[ciudad]
                ciudad_minima = ciudad
    return ciudad_minima
# Funcion 3: reconstruye el camino recorrido 
def reconstruir_ruta(padres, origen, destino):
    ruta = [destino]
    ciudad_actual = destino
    while ciudad_actual != origen:
        ciudad_actual = padres[ciudad_actual]
        ruta.append(ciudad_actual)
    ruta.reverse()  # porque la armamos al reves (de destino a origen)
    return ruta
# Funcion 4: ejecuta el algoritmo de Dijkstra completo.
def ejecutar_dijkstra(grafo, origen, destino):
    distancias = inicializar_distancias(grafo, origen)
    visitados = []          # lista de ciudades ya confirmadas
    padres = {}              # guarda desde que ciudad llegamos a cada una
    while len(visitados) < len(grafo):
        ciudad_actual = buscar_nodo_minimo(distancias, visitados)
        # Si no encontramos ninguna ciudad (grafo desconectado), salimos
        if ciudad_actual is None:
            break
        visitados.append(ciudad_actual)
        # Revisamos cada vecino de la ciudad actual
        for vecino in grafo[ciudad_actual]:
            peso = grafo[ciudad_actual][vecino]
            nueva_distancia = distancias[ciudad_actual] + peso
            # Si encontramos un camino mas corto hacia el vecino, actualizamos su distancia y guardamos quien es su padre
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = ciudad_actual
    # Si la distancia al destino sigue siendo infinita, no hay camino
    if distancias[destino] == float("inf"):
        return None, None

    ruta_optima = reconstruir_ruta(padres, origen, destino)
    distancia_total = distancias[destino]
    return ruta_optima, distancia_total


# BLOQUE 3: FUNCIONES DE VISUALIZACION (networkx + matplotlib)

def mostrar_grafo(ruta_optima=None):

    grafo_nx = nx.Graph()
    for ciudad in grafo:
        for vecino in grafo[ciudad]:
            grafo_nx.add_edge(ciudad, vecino, weight=grafo[ciudad][vecino])
    # Posiciones automaticas de los nodos
    posiciones = nx.spring_layout(grafo_nx, seed=42, k=0.8)
    plt.figure(figsize=(11, 8))
    # Dibujamos todos los nodos y aristas (moradito y negro)
    nx.draw_networkx_nodes(grafo_nx, posiciones, node_color="palevioletred", node_size=1800)
    nx.draw_networkx_labels(grafo_nx, posiciones, font_size=8)
    nx.draw_networkx_edges(grafo_nx, posiciones, edge_color="black")
    # Mostramos los pesos (distancias) en cada arista
    pesos_aristas = nx.get_edge_attributes(grafo_nx, "weight")
    nx.draw_networkx_edge_labels(grafo_nx, posiciones, edge_labels=pesos_aristas, font_size=7)
    if ruta_optima is not None and len(ruta_optima) > 1:
        aristas_ruta = []
        for i in range(len(ruta_optima) - 1):
            aristas_ruta.append((ruta_optima[i], ruta_optima[i + 1]))
        # Dibuja los nodos de la ruta en rosado fuerte
        nx.draw_networkx_nodes(grafo_nx, posiciones, nodelist=ruta_optima,
                                node_color="deeppink", node_size=1800)
        # Si hay una ruta optima, la resaltamos en color rojizo rosado
        nx.draw_networkx_edges(grafo_nx, posiciones, edgelist=aristas_ruta, 
                                edge_color="crimson", width=3)

    plt.axis("off")  #Esto apaga los ejes negros del fondo
    plt.show()

# BLOQUE 4: FUNCIONES DE INTERFAZ (Tkinter)
ultima_ruta_calculada = None  # Variable global donde vamos a guardar la ultima ruta calculada

def calcular_ruta():
    global ultima_ruta_calculada
    origen = combo_origen.get()
    destino = combo_destino.get()
    # Validamos que el usuario haya elegido ambas ciudades
    if origen == "" or destino == "":
        messagebox.showwarning("Datos incompletos", "Debe seleccionar una ciudad de origen y una de destino")
        return
    if origen == destino:
        messagebox.showwarning("Ciudades iguales", "El origen y el destino no pueden ser la misma ciudad")
        return
    ruta_optima, distancia_total = ejecutar_dijkstra(grafo, origen, destino)

    if ruta_optima is None:
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, "No existe una ruta entre las ciudades seleccionadas.")
        ultima_ruta_calculada = None
        return
    ultima_ruta_calculada = ruta_optima

    #texto con los resultados 
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, "Ruta optima encontrada:\n")
    texto_resultado.insert(tk.END, " -> ".join(ruta_optima) + "\n\n")
    texto_resultado.insert(tk.END, "Distancia total: " + str(distancia_total) + " km\n")
    texto_resultado.insert(tk.END, "Cantidad de ciudades recorridas: " + str(len(ruta_optima)))

def visualizar_grafo():                       # Se ejecuta cuando el usuario presiona el boton para ver el grafo
    mostrar_grafo(ultima_ruta_calculada)

# BLOQUE 5: VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Calculadora de Rutas Mas Cortas - Dijkstra")
ventana.geometry("520x430")
ventana.resizable(False, False)
#Titulo del proyecto
titulo = tk.Label(ventana, text="Calculadora de Rutas entre Ciudades de Japon",
                   font=("Arial", 15, "bold"))
titulo.pack(pady=12)
#subtitulo
subtitulo = tk.Label(ventana, text="Algoritmo de Dijkstra - Matematica Discreta",
                      font=("Arial", 10))
subtitulo.pack(pady=2)

#Lista de ciudades
lista_ciudades = list(grafo.keys())

frame_origen = tk.Frame(ventana)
frame_origen.pack(pady=8)
label_origen = tk.Label(frame_origen, text="Ciudad de origen:", width=18, anchor="w")
label_origen.pack(side="left")
combo_origen = ttk.Combobox(frame_origen, values=lista_ciudades, width=25, state="readonly")
combo_origen.pack(side="left")


frame_destino = tk.Frame(ventana)
frame_destino.pack(pady=8)
label_destino = tk.Label(frame_destino, text="Ciudad de destino:", width=18, anchor="w")
label_destino.pack(side="left")
combo_destino = ttk.Combobox(frame_destino, values=lista_ciudades, width=25, state="readonly")
combo_destino.pack(side="left")

#Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=12)

boton_calcular = tk.Button(frame_botones, text="Calcular Ruta", command=calcular_ruta,
                            bg="#C74FE2", fg="white", width=15)
boton_calcular.pack(side="left", padx=5)

boton_visualizar = tk.Button(frame_botones, text="Ver Grafo", command=visualizar_grafo,
                              bg="#FA6AA8", fg="white", width=15)
boton_visualizar.pack(side="left", padx=5)

#Area de texto con los resultados
texto_resultado = tk.Text(ventana, height=10, width=58)
texto_resultado.pack(pady=10)

#Inicia el bucle principal de la interfaz grafica
ventana.mainloop()
