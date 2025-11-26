"""
Módulo barco.py
Clase Barco para el juego Hundir la Flota

Autor: Felipe (DAM-1 - COD)
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
