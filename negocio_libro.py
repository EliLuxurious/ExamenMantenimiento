import pandas as pd
from Libro import Libro

class NegocioLibro():

    listado_libros = []
    registro_libros = 'C:/Users/Elia/Desktop/PROGRAMACION/Python/CICLO 3/Educativa/listado_autor/listado_libro.xlsx'

    def __init__(self):
        self.listado_libros = []

    def obtener_libros(self):
        df = pd.read_excel(self.registro_libros)
        listado_libros = []
        for index, row in df.iterrows():
            libro = Libro(row['Codigo_Libro'], row['Titulo'], row['Año'], row['Tomo'])
            autor = row['Autor']  
            if autor:
                libro.asignar_autor(autor)
            listado_libros.append(libro)
        return listado_libros

    def registrar_libro(self, codigo_libro, titulo, year, tomo, autor=None):
        self.listado_libros = self.obtener_libros()
        libro = Libro(codigo_libro, titulo, year, tomo)
        if autor:
            libro.asignar_autor(autor)
        self.listado_libros.append(libro)
        print(f'Se agregó un libro: {len(self.listado_libros)}')

    def guardar_libros(self):
        if len(self.listado_libros) > 0:
            data = []
            for libro in self.listado_libros:
                autor = libro.mostrar_autor() if libro.mostrar_autor() else None
                data.append([libro.get_codigo_libro(), libro.get_titulo(), libro.get_year(), libro.get_tomo(), autor])
            columnas = ['Codigo_Libro', 'Titulo', 'Año', 'Tomo', 'Autor']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registro_libros, index=False, engine='openpyxl')
            return f'Se registraron correctamente los datos del libro'
        else:
            return f'Se generó un error al registrar el libro'

    def editar_libro(self, indice, codigo_libro, titulo, year, tomo, autor=None):
        df = pd.read_excel(self.registro_libros)
        df.loc[indice, 'Codigo_Libro'] = codigo_libro
        df.loc[indice, 'Titulo'] = titulo
        df.loc[indice, 'Año'] = year
        df.loc[indice, 'Tomo'] = tomo
        df.loc[indice, 'Autor'] = autor if autor else None
        df.to_excel(self.registro_libros, index=False, engine='openpyxl')
        return f'Actualización correcta'

    def eliminar_libro_por_codigo(self, codigo_libro):
        libro_a_eliminar = None
        for libro in self.listado_libros:
            if libro.get_codigo_libro() == codigo_libro:
                libro_a_eliminar = libro
                break

        if libro_a_eliminar:
            self.listado_libros.remove(libro_a_eliminar)
            print(f'Libro con código {codigo_libro} eliminado correctamente.')
        else:
            print(f'Libro con código {codigo_libro} no encontrado.')

    def buscar_libro_por_codigo(self, codigo_libro):
        for libro in self.listado_libros:
            if libro.get_codigo_libro() == codigo_libro:
                return libro
        return None


    def generar_reporte_libros(listado_libros):
        try:
            with open("reporte_libros.txt", "w") as archivo_reporte:
                archivo_reporte.write("Reporte de Libros\n\n")
                for libro in listado_libros:
                    autor = libro.mostrar_autor()
                    autor_info = f"Autor: {autor.nombre} {autor.ap_paterno} {autor.ap_materno}" if autor else "Autor no asignado"
                    archivo_reporte.write(f"Código del libro: {libro.get_codigo_libro()}\n")
                    archivo_reporte.write(f"Título: {libro.get_titulo()}\n")
                    archivo_reporte.write(f"Año: {libro.get_year()}\n")
                    archivo_reporte.write(f"Tomo: {libro.get_tomo()}\n")
                    archivo_reporte.write(f"{autor_info}\n")
                    archivo_reporte.write("\n")
            print("Reporte de libros generado con éxito en 'reporte_libros.txt'.")
        except Exception as e:
            print(f"Error al generar el reporte: {str(e)}")
