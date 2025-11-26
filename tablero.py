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


# Bloque de pruebas
if __name__ == "__main__":
    print("=== PRUEBAS DE LA CLASE TABLERO ===\n")
    
    # Prueba 1: Tablero pequeño 5x5
    print("PRUEBA 1: Tablero 5x5")
    tablero_pequeno = Tablero(5)
    tablero_pequeno.mostrar_tablero()
    
    print(f"Dimensiones: {tablero_pequeno.dimensiones}")
    print(f"Cantidad de filas: {len(tablero_pequeno.casillas)}")
    print(f"Cantidad de columnas: {len(tablero_pequeno.casillas[0])}")
    
    # Verificar que todas las casillas están inicializadas con 0
    todas_agua = all(
        casilla == 0 
        for fila in tablero_pequeno.casillas 
        for casilla in fila
    )
    print(f"¿Todas las casillas tienen agua (0)? {todas_agua}")
    
    # Prueba 2: Tablero estándar 10x10
    print("\n\nPRUEBA 2: Tablero 10x10 (Tamaño estándar)")
    tablero_estandar = Tablero(10)
    tablero_estandar.mostrar_tablero()
    
    # Prueba 3: Tablero grande 15x15
    print("\nPRUEBA 3: Tablero 15x15 (Tamaño grande)")
    tablero_grande = Tablero(15)
    tablero_grande.mostrar_tablero()
    
    # Prueba 4: Modificar una casilla (simulación)
    print("\nPRUEBA 4: Modificando casillas manualmente")
    tablero_test = Tablero(8)
    print("Tablero inicial:")
    tablero_test.mostrar_tablero()
    
    # Simular colocar algunos barcos (1 = barco)
    tablero_test.casillas[0][0] = 1
    tablero_test.casillas[0][1] = 1
    tablero_test.casillas[0][2] = 1
    tablero_test.casillas[5][5] = 1
    
    print("Tablero con algunas casillas modificadas (1 = barco):")
    tablero_test.mostrar_tablero()
    
    print("\n=== FIN DE LAS PRUEBAS ===")
