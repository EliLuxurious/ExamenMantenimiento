class Categoria():
    # Atributos de la clase Categoria
    cod_categoria = ''  # Código de la categoría
    categoria = ''      # Nombre de la categoría

    # Constructor de la clase Categoria
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria  # Inicializa el código de la categoría
        self.categoria = categoria        # Inicializa el nombre de la categoría

    # Método para establecer el código de la categoría
    def set_cod_categoria(self, cod_categoria):
        self.cod_categoria = cod_categoria

    # Método para obtener el código de la categoría
    def get_cod_categoria(self):
        return self.cod_categoria
    
    # Método para establecer el nombre de la categoría
    def set_nombre_categoria(self, categoria):
        self.categoria = categoria

    # Método para obtener el nombre de la categoría
    def get_nombre_categoria(self):
        return self.categoria
    
    # Método para asignar un libro a la categoría
    def asignar_libro(self, libro):
        self.libro = libro
    
    # Método para mostrar el libro asignado a la categoría
    def mostrar_libro(self):
        return self.libro
    
    # Método para generar un reporte de la categoría y el libro asociado
    def reporte(self):
        return f"Reporte del libro: {self.libro}\nCódigo de la categoría: {self.cod_categoria}\nCategoría: {self.categoria}"

    