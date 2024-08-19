from random import uniform

class Pelicula:
    def __init__(self, titulo, director, protagonista, temporadas, episodios_totales, ranking, anio):
        self.titulo = titulo
        self.director = director
        self.protagonista = protagonista
        self.temporadas = temporadas
        self.episodios_totales = episodios_totales
        self.ranking = ranking
        self.anio = anio

    def __repr__(self):
        return f"Pelicula(titulo={self.titulo}, director={self.director}, protagonista={self.protagonista}, " \
               f"temporadas={self.temporadas}, episodios_totales={self.episodios_totales}, ranking={self.ranking}, anio={self.anio})"

class ManejadorPeliculas:
    MAX_PELICULAS = 20
    
    def __init__(self, peliculas=None):
        self.peliculas = peliculas if peliculas is not None else []
        self.validar_array_no_vacio()
        self.validar_max_peliculas()
        
    
    def validar_array_no_vacio(self):
        if len(self.peliculas) == 0:
            print("La lista de películas no puede estar vacía.")
            self.menu()

    def validar_max_peliculas(self):
        if len(self.peliculas) >= ManejadorPeliculas.MAX_PELICULAS:
            print(f"La lista de películas no puede contener más de {ManejadorPeliculas.MAX_PELICULAS} películas.")
            self.menu()

    def verificar_existencia_pelicula(self, titulo):
        return any(pelicula.titulo == titulo for pelicula in self.peliculas)
    
    def agregar_pelicula(self, pelicula):
        if self.verificar_existencia_pelicula(pelicula.titulo):
            print(f"Ya existe una película con el título '{pelicula.titulo}'.")
            self.menu()
        
        if len(self.peliculas) >= ManejadorPeliculas.MAX_PELICULAS:
            print("No se puede agregar más películas. Se ha alcanzado el límite máximo.")
            self.menu()
        
        self.peliculas.append(pelicula)

    def eliminar_pelicula_por_titulo(self, titulo):
        pelicula_a_eliminar = None
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                pelicula_a_eliminar = pelicula
                break
        
        if pelicula_a_eliminar:
            self.peliculas.remove(pelicula_a_eliminar)
            self.validar_array_no_vacio()
            print(f"Pelicula '{titulo}' eliminada exitosamente.")
        else:
            print(f"Pelicula con título '{titulo}' no encontrada.")
    
    def ingresar_nueva_pelicula(self):
        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el director de la película: ")
        protagonista = input("Ingrese el protagonista de la película: ")
        temporadas = int(input("Ingrese el número de temporadas: "))
        episodios_totales = int(input("Ingrese el número total de episodios: "))
        anio = int(input("Ingrese el año de la película: "))
        ranking = round(uniform(0, 10), 1)  # Asigna un ranking aleatorio entre 0 y 10 con un decimal

        nueva_pelicula = Pelicula(titulo, director, protagonista, temporadas, episodios_totales, ranking, anio)
        self.agregar_pelicula(nueva_pelicula)
        print(f"Película '{titulo}' agregada exitosamente con un ranking de {ranking}.")
    
    def mostrar_series(self):
        print("\nSeleccione una opción:")
        print("1. Filtrar por año")
        print("2. Filtrar alfabéticamente por título")
        print("3. Filtrar por cantidad de episodios")
        print("4. Filtrar por ranking")
            
        opcion = input("Ingrese el número de la opción deseada: ")
            
        if opcion == '1':
            self.filtrar_por_anio()
        elif opcion == '2':
            self.filtrar_por_titulo()
        elif opcion == '3':
            self.filtrar_por_episodios()
        elif opcion == '4':
            self.filtrar_por_ranking()
        else:
            print("Opción no válida. Inténtelo de nuevo.")
    
    def filtrar_por_anio(self):
        peliculas_ordenadas = sorted(self.peliculas, key=lambda x: x.anio)
        self.mostrar_peliculas(peliculas_ordenadas)
    
    def filtrar_por_titulo(self):
        peliculas_ordenadas = sorted(self.peliculas, key=lambda x: x.titulo)
        self.mostrar_peliculas(peliculas_ordenadas)
    
    def filtrar_por_episodios(self):
        peliculas_ordenadas = sorted(self.peliculas, key=lambda x: x.episodios_totales, reverse=True)
        self.mostrar_peliculas(peliculas_ordenadas)
    
    def filtrar_por_ranking(self):
        peliculas_ordenadas = sorted(self.peliculas, key=lambda x: (x.ranking, x.episodios_totales), reverse=True)
        self.mostrar_peliculas(peliculas_ordenadas)
    
    def mostrar_peliculas(self, peliculas):
        if peliculas:
            for pelicula in peliculas:
                print(pelicula)
        else:
            print("No hay películas para mostrar.")
    
    def menu(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Mostrar series")
            print("2. Agregar película")
            print("3. Borrar película")
            print("4. Salir")
            
            opcion = input("Ingrese el número de la opción deseada: ")
            
            if opcion == '1':
                self.mostrar_series()
            elif opcion == '2':
                self.ingresar_nueva_pelicula()
            elif opcion == '3':
                titulo = input("Ingrese el título de la película que desea borrar: ")
                self.eliminar_pelicula_por_titulo(titulo)
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
