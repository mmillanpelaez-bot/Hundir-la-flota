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


# Bloque de pruebas
if __name__ == "__main__":
    print("=== PRUEBAS DE LA CLASE BARCO ===\n")
    
    # Prueba 1: Crear un Submarino de longitud 1
    print("PRUEBA 1: Submarino (longitud 1)")
    submarino = Barco("Submarino", 1)
    submarino.mostrar_estado()
    
    print("\n> Recibiendo primer impacto...")
    submarino.recibir_impacto()
    submarino.mostrar_estado()
    
    print(f"\n¿Está hundido el submarino? {submarino.esta_hundido()}")
    
    # Prueba 2: Crear un Buque de longitud 3
    print("\n\nPRUEBA 2: Buque (longitud 3)")
    buque = Barco("Buque", 3)
    buque.mostrar_estado()
    
    print("\n> Recibiendo primer impacto...")
    buque.recibir_impacto()
    buque.mostrar_estado()
    print(f"¿Está hundido? {buque.esta_hundido()}")
    
    print("\n> Recibiendo segundo impacto...")
    buque.recibir_impacto()
    buque.mostrar_estado()
    print(f"¿Está hundido? {buque.esta_hundido()}")
    
    print("\n> Recibiendo tercer impacto...")
    buque.recibir_impacto()
    buque.mostrar_estado()
    print(f"¿Está hundido? {buque.esta_hundido()}")
    
    # Prueba 3: Crear un Portaaviones de longitud 4
    print("\n\nPRUEBA 3: Portaaviones (longitud 4)")
    portaaviones = Barco("Portaaviones", 4)
    portaaviones.mostrar_estado()
    
    print("\n> Simulando batalla intensa...")
    for i in range(1, 5):
        portaaviones.recibir_impacto()
        print(f"Impacto {i}: Golpes recibidos = {portaaviones.golpes_recibidos}")
    
    portaaviones.mostrar_estado()
    
    print("\n=== FIN DE LAS PRUEBAS ===")
