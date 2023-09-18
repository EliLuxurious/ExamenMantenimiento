from Categoria import Categoria  
from negocio_autor import AutorNegocio
from negocio_libro import NegocioLibro
from negocio_categoria import NegocioCategoria  # Agregar importación para la clase NegocioCategoria

negocio_autor = AutorNegocio()
negocio_libro = NegocioLibro()
negocio_categoria = NegocioCategoria()  # Crear una instancia de NegocioCategoria

def registrar_autores():
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    fecha_nacimiento = input('Ingrese fecha_nacimiento: ')
    cod_autor = input('Ingrese cod_autor: ')
    pais = input('Ingrese pais: ')
    editorial = input('Ingrese editorial: ')
    negocio_autor.registrar_autores(nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial)
    negocio_autor.guardar_autores()
    print(f'Registro exitoso del autor')

def obtener_autores():
    listado_autores = negocio_autor.obtener_autores()
    for autor in listado_autores:
        print(autor.imprimir())

def editar_autores():
    indice = int(input('Ingrese el índice del autor a editar: '))
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    fecha_nacimiento = input('Ingrese fecha_nacimiento: ')
    cod_autor = input('Ingrese cod_autor: ')
    pais = input('Ingrese pais: ')
    editorial = input('Ingrese editorial: ')
    print(negocio_autor.editar_autores(indice, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial))

def eliminar_autor_por_codigo(codigo):
    autor_a_eliminar = None
    for autor in negocio_autor.listado_autores:
        if autor.cod_autor == codigo:
            autor_a_eliminar = autor
            break

    if autor_a_eliminar:
        negocio_autor.listado_autores.remove(autor_a_eliminar)
        print(f'Autor con código {codigo} eliminado correctamente.')
    else:
        print(f'Autor con código {codigo} no encontrado.')


def registrar_libros():
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor_codigo = input('Ingrese el código del autor del libro: ') 
    negocio_libro.registrar_libro(codigo_libro, titulo, year, tomo, autor_codigo)
    resultado = negocio_libro.guardar_libros()
    print(resultado)

def obtener_libros():
    listado_libros = negocio_libro.obtener_libros()
    for libro in listado_libros:
        autor = libro.mostrar_autor()
        autor_info = f"Autor: {autor.nombre} {autor.ap_paterno} {autor.ap_materno}" if autor else "Autor no asignado"
        print(f"Código del libro: {libro.get_codigo_libro()}\nTítulo: {libro.get_titulo()}\nAño: {libro.get_year()}\nTomo: {libro.get_tomo()}\n{autor_info}\n")

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


def editar_libros():
    indice = int(input('Ingrese el índice del libro a editar: '))
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor = input('Ingrese el autor del libro (Código del autor): ')
    
    # Obtener el autor del registro de autores (asumiendo que está implementado)
    autor_encontrado = negocio_autor.buscar_autor_por_codigo(autor)
    if autor_encontrado:
        print(negocio_libro.editar_libro(indice, codigo_libro, titulo, year, tomo, autor_encontrado))
    else:
        print("El autor no existe. Registre al autor antes de editar el libro.")

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

def asignar_libro_a_categoria():
    codigo_libro = input('Ingrese código del libro: ')
    categoria_codigo = input('Ingrese código de la categoría: ')
    
    libro = negocio_libro.buscar_libro_por_codigo(codigo_libro)
    categoria = negocio_categoria.buscar_categoria_por_codigo(categoria_codigo)
    
    if libro and categoria:
        libro.asignar_categoria(categoria)
        resultado = negocio_libro.guardar_libros()
        print(f'Libro asignado a la categoría "{categoria.get_categoria()}".')
    else:
        print("El libro o la categoría no existen.")

def registrar_categoria():
    cod_categoria = input('Ingrese el código de la categoría: ')
    categoria = input('Ingrese el nombre de la categoría: ')
    negocio_categoria.registrar_categoria(cod_categoria, categoria)
    print(f'Categoría "{categoria}" registrada con éxito.')

def editar_categoria():
    cod_categoria = input('Ingrese el código de la categoría que desea editar: ')
    nueva_categoria = input('Ingrese el nuevo nombre de la categoría: ')
    negocio_categoria.editar_categoria(cod_categoria, nueva_categoria)
    print(f'Categoría con código "{cod_categoria}" editada con éxito.')

def listar_categorias():
    categorias = negocio_categoria.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        print("Lista de Categorías:")
        for categoria in categorias:
            print(f"Código de Categoría: {categoria.get_cod_categoria()}, Nombre: {categoria.get_categoria()}")

def eliminar_categoria_por_codigo(self, cod_categoria):
    categoria_a_eliminar = None
    for categoria in self.lista_categorias:
        if categoria.get_cod_categoria() == cod_categoria:
            categoria_a_eliminar = categoria
            break

    if categoria_a_eliminar:
        self.lista_categorias.remove(categoria_a_eliminar)
        print(f'Categoría con código {cod_categoria} eliminada correctamente.')
    else:
        print(f'Categoría con código {cod_categoria} no encontrada.')

opciones = {
    "1": registrar_autores,
    "2": obtener_autores,
    "3": editar_autores,
    "4": eliminar_autor_por_codigo,  
    "5": registrar_libros,
    "6": obtener_libros,
    "7": editar_libros,
    "8": eliminar_libro_por_codigo, 
    "9": asignar_libro_a_categoria,
    "10": registrar_categoria,
    "11": editar_categoria,
    "12": listar_categorias,
    "13": eliminar_categoria_por_codigo, 
    "14": exit
}


while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar autores")
    print("2. Listar autores")
    print("3. Editar autores")
    print("4. Eliminar autor")
    print("5. Registrar libros")
    print("6. Listar libros")
    print("7. Editar libros")
    print("8. Eliminar libro")
    print("9. Asignar libro a categoría")
    print("10. Registrar Categoría")   
    print("11. Editar Categoría")       
    print("12. Listar Categorías")     
    print("13. Eliminar Categoría")
    print("14. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        if seleccion == "4" or seleccion == "8" or seleccion == "13":
            codigo = input("Ingrese el código: ")
            opciones[seleccion](codigo)
        elif seleccion == "6":
            obtener_libros()  # Llama a la función para listar libros
            generar_reporte_libros(negocio_libro.obtener_libros())
        else:
            opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")