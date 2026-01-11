"""
PROGRAMA: Sistema de Gestión de Biblioteca Pequeña
FUNCIONALIDAD: Este programa permite administrar un inventario de libros, 
gestionar usuarios y procesar préstamos utilizando Programación Orientada a Objetos (POO).
"""

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_service import BibliotecaService

def ejecutar_aplicacion():
    # 1. Instanciamos objetos de la clase Libro (Datos de prueba)
    libro_a = Libro("Don Quijote", "Cervantes", 35.00)
    libro_b = Libro("Ficciones", "Borges", 22.50)
    inventario_total = [libro_a, libro_b]

    # 2. Instanciamos un usuario (Integer para ID, String para nombre)
    usuario_registrado = Usuario("Carlos Avila", 501)

    # 3. Inicializamos el servicio que maneja la lógica
    gestion = BibliotecaService()

    # --- SIMULACIÓN DE OPERACIONES ---
    print("--- INVENTARIO ACTUAL ---")
    print(libro_a)
    print(libro_b)

    print("\n--- PROCESANDO PRÉSTAMO ---")
    # Llamamos al método del servicio pasando los objetos como argumentos
    gestion.realizar_prestamo(libro_a, usuario_registrado)

    print("\n--- RESUMEN ECONÓMICO ---")
    valor_total = gestion.calcular_patrimonio(inventario_total)
    print(f"El valor total de los libros en la biblioteca es: ${valor_total:.2f}")

# Punto de entrada estándar de Python
if __name__ == "__main__":
    ejecutar_aplicacion()