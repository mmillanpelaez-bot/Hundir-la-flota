"""
Módulo barco.py
Clase Barco para el juego Hundir la Flota

Autor: Estudiante DAM-1
Asignatura: COD
"""


class Barco:
    """
    Clase que representa un barco en el juego Hundir la Flota.
    
    Attributes:
        nombre (str): Nombre del barco (ej: "Submarino", "Portaaviones")
        longitud (int): Cantidad de casillas que ocupa el barco
        golpes_recibidos (int): Contador de impactos recibidos
    """
    
    def __init__(self, nombre, longitud):
        """
        Constructor de la clase Barco.
        
        Args:
            nombre (str): Nombre del barco
            longitud (int): Longitud del barco en casillas
        """
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0
    
    def recibir_impacto(self):
        """
        Incrementa el contador de golpes recibidos en 1.
        Representa el impacto de un disparo en el barco.
        """
        self.golpes_recibidos += 1
    
    def esta_hundido(self):
        """
        Verifica si el barco está hundido.
        Un barco está hundido cuando los golpes recibidos igualan su longitud.
        
        Returns:
            bool: True si el barco está hundido, False en caso contrario
        """
        return self.golpes_recibidos >= self.longitud
    
    def mostrar_estado(self):
        """
        Muestra por consola el estado actual del barco.
        Incluye nombre, longitud, golpes recibidos y si está hundido.
        """
        estado = "HUNDIDO" if self.esta_hundido() else "A FLOTE"
        print(f"\n--- Estado del Barco ---")
        print(f"Nombre: {self.nombre}")
        print(f"Longitud: {self.longitud} casillas")
        print(f"Golpes recibidos: {self.golpes_recibidos}/{self.longitud}")
        print(f"Estado: {estado}")
        print(f"------------------------")
