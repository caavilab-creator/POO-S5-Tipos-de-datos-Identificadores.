# Definición el modelo para un Libro individual
class Libro:
    def __init__(self, titulo, autor, precio, disponible=True):
        # Inicializamos los atributos con tipos de datos específicos
        self.titulo = str(titulo)          # Tipo: String
        self.autor = str(autor)            # Tipo: String
        self.precio = float(precio)        # Tipo: Float (decimal)
        self.esta_disponible = bool(disponible) # Tipo: Boolean (True/False)

    def __str__(self):
        # Método especial para representar el objeto como una cadena de texto
        estado = "Disponible" if self.esta_disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} - ${self.precio} [{estado}]"