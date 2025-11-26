"""
Módulo tablero.py
Clase Tablero para el juego Hundir la Flota

Autor: Estudiante DAM-1
Asignatura: COD
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
    
    def mostrar_tablero(self):
        """
        Muestra el tablero por consola de forma legible.
        Incluye numeración de filas y columnas para facilitar la visualización.
        """
        filas, columnas = self.dimensiones
        
        print("\n" + "="*50)
        print(f"TABLERO DE JUEGO ({filas}x{columnas})")
        print("="*50)
        
        # Encabezado con números de columna
        print("\n   ", end="")
        for col in range(columnas):
            print(f"{col:3}", end="")
        print("\n   " + "---" * columnas)
        
        # Filas del tablero
        for i, fila in enumerate(self.casillas):
            print(f"{i:2}|", end="")
            for casilla in fila:
                # 0 representa agua, se muestra como ~
                simbolo = "~" if casilla == 0 else str(casilla)
                print(f"{simbolo:3}", end="")
            print()
        
        print("="*50 + "\n")
