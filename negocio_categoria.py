from Categoria import Categoria

# Define la clase NegocioCategoria
class NegocioCategoria():
    
    lista_categorias = []  # Lista para almacenar objetos de la clase Categoria
    registro_categorias = 'C:/Users/Elia/Desktop/PROGRAMACION/Python/CICLO 3/Educativa/listado_autor/listado_categoria.xlsx'


    # Constructor de la clase NegocioCategoria
    def __init__(self):
        self.lista_categorias = []  # Inicializa la lista de categorías

    # Método para obtener la lista de categorías
    def obtener_categorias(self):
        return self.lista_categorias

    # Método para registrar una nueva categoría
    def registrar_categoria(self, cod_categoria, categoria):
        # Busca si la categoría ya existe en la lista
        categoria_existente = self.buscar_categoria_por_codigo(cod_categoria)
        if categoria_existente:
            print("La categoría ya existe.")
        else:
            # Crea una nueva instancia de Categoria y la agrega a la lista
            nueva_categoria = Categoria(cod_categoria, categoria)
            self.lista_categorias.append(nueva_categoria)
            print("Categoría registrada con éxito.")

    # Método para editar el nombre de una categoría
    def editar_categoria(self, cod_categoria, nueva_categoria):
        # Busca si la categoría existe en la lista
        categoria_existente = self.buscar_categoria_por_codigo(cod_categoria)
        if categoria_existente:
            # Actualiza el nombre de la categoría
            categoria_existente.set_categoria(nueva_categoria)
            print("Categoría editada con éxito.")
        else:
            print("La categoría no existe.")

    # Método para eliminar una categoría por su código
    def eliminar_categoria_por_codigo(self, cod_categoria):
        categoria_a_eliminar = None
        # Itera a través de la lista de categorías
        for categoria in self.lista_categorias:
            if categoria.get_cod_categoria() == cod_categoria:
                categoria_a_eliminar = categoria
                break

        if categoria_a_eliminar:
            # Remueve la categoría de la lista
            self.lista_categorias.remove(categoria_a_eliminar)
            print(f'Categoría con código {cod_categoria} eliminada correctamente.')
        else:
            print(f'Categoría con código {cod_categoria} no encontrada.')

    # Método para buscar una categoría por su código
    def buscar_categoria_por_codigo(self, cod_categoria):
        # Itera a través de la lista de categorías
        for categoria in self.lista_categorias:
            if categoria.get_cod_categoria() == cod_categoria:
                return categoria  # Retorna la categoría si se encuentra
        return None  # Retorna None si la categoría no se encuentra en la lista

