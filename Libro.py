# Importa la clase Autor desde el archivo Autor.py
from Autor import Autor

# Define la clase Libro, que hereda de Autor (herencia)
class Libro():
    # Atributos de la clase Libro
    codigo_libro = ''  # Codigo del libro
    titulo = ''  # Titulo del libro
    year = ''  # Año del libro
    tomo = ''  # Tomo del libro

    # Constructor de la clase Libro
    def __init__(self, codigo_libro, titulo, year, tomo, cod_autor=None):
        # Inicializa los atributos del libro
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.year = year
        self.tomo = tomo
        self.codigo_autor = cod_autor  # Almacena el código del autor en lugar del objeto Autor

    # Métodos para establecer y obtener el código del libro
    def set_codigo_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro

    def get_codigo_libro(self):
        return self.codigo_libro

    # Métodos para establecer y obtener el título del libro
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    # Métodos para establecer y obtener el año del libro
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    # Métodos para establecer y obtener el tomo del libro
    def set_tomo(self, tomo):
        self.tomo = tomo

    def get_tomo(self):
        return self.tomo

    # Método para asignar un autor al libro
    def asignar_autor(self, autor):
        self.autor = autor

    # Método para mostrar el autor del libro
    def mostrar_autor(self):
        return self.autor
    
    #Asignar Categoria
    def asignar_categoria(self, categoria):
        self.categoria = categoria

    # Método para generar un reporte del libro
    def reporte(self):
        return f"Reporte del curso {self.titulo}\nCodigo del libro: {self.get_codigo_libro}\nAño: {self.year}\nTomo: {self.tomo}"
