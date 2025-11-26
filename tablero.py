"""
Módulo tablero.py
Clase Tablero para el juego Hundir la Flota

Autor: Felipe (DAM-1 - COD)
"""


class Tablero:
    """
    Clase que representa el tablero de juego de Hundir la Flota.
    
    Attributes:
        dimensiones (tuple): Tupla con el formato (filas, columnas)
        casillas (list): Matriz que representa el tablero (lista de listas)
                        El valor 0 representa agua
    """
    
    def __init__(self, tamano):
        """
        Constructor de la clase Tablero.
        Crea un tablero cuadrado de tamaño especificado.
        
        Args:
            tamano (int): Tamaño del tablero (crea un tablero de tamano x tamano)
        """
        self.dimensiones = (tamano, tamano)
        # Inicializar el tablero con agua (0) en todas las casillas
        self.casillas = [[0 for _ in range(tamano)] for _ in range(tamano)]
