# Este servicio contiene la lógica de negocio para gestionar préstamos
class BibliotecaService:
    def realizar_prestamo(self, libro, usuario):
        """
        Lógica para validar si un libro puede ser entregado a un usuario.
        Cambia el estado del libro y lo asigna a la lista del usuario.
        """
        if libro.esta_disponible:
            libro.esta_disponible = False  # Cambiamos el booleano a False
            usuario.libros_prestados.append(libro)
            print(f"CONFIRMACIÓN: {libro.titulo} prestado a {usuario.nombre}.")
            return True
        else:
            print(f"AVISO: El libro '{libro.titulo}' no se encuentra disponible.")
            return False

    def calcular_patrimonio(self, lista_libros):
        # Sumamos el precio (float) de todos los libros para obtener un total
        total = sum(libro.precio for libro in lista_libros)
        return total