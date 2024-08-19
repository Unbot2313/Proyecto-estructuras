import json
from clases import Pelicula, ManejadorPeliculas
peliculas = []

def InitPeliculas():
    with open('datos.json', 'r') as file:
        data = json.load(file)
    
    global peliculas
    peliculas = [Pelicula(**item) for item in data]

# Llamar a InitPeliculas() para cargar los datos
InitPeliculas()
ManejadorPeliculas = ManejadorPeliculas(peliculas)
ManejadorPeliculas.menu()
