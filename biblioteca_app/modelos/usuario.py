# Definición del modelo para representar a los socios de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = str(nombre)          # Identificador de texto
        self.id_usuario = int(id_usuario)  # Identificador numérico (Integer)
        self.libros_prestados = []         # Lista para almacenar objetos tipo Libro