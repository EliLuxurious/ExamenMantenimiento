# Importa las clases necesarias desde otros archivos
from Categoria import Categoria
from negocio_autor import AutorNegocio
from negocio_libro import NegocioLibro
from negocio_categoria import NegocioCategoria  # Agregar importación para la clase NegocioCategoria
from Autor import Autor

# Crea instancias de las clases de negocio
negocio_autor = AutorNegocio()
negocio_libro = NegocioLibro()
negocio_categoria = NegocioCategoria()

# Define funciones para realizar acciones en el programa

# Función para registrar autores
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

# Función para obtener y listar autores
def obtener_autores():
    listado_autores = negocio_autor.obtener_autores()
    for autor in listado_autores:
        print(autor.imprimir())

# Función para editar autores
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

# Función para eliminar un autor por su código
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

# Función para registrar libros
def registrar_libros():
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor_codigo = input('Ingrese el código del autor del libro: ') 
    negocio_libro.registrar_libro(codigo_libro, titulo, year, tomo, autor_codigo)
    resultado = negocio_libro.guardar_libros()
    print(resultado)

# Función para obtener y listar libros
def obtener_libros():
    listado_libros = negocio_libro.obtener_libros()
    for libro in listado_libros:
        autor = libro.mostrar_autor()
        if autor and isinstance(autor, Autor):  # Asegúrate de que Autor es la clase correcta
            autor_info = f"Autor: {autor.nombre} {autor.ap_paterno} {autor.ap_materno}"
        else:
            autor_info = "Autor no asignado"
        print(f"Código del libro: {libro.get_codigo_libro()}\nTítulo: {libro.get_titulo()}\nAño: {libro.get_year()}\nTomo: {libro.get_tomo()}\n{autor_info}\n")
    
# Función para generar un reporte de libros
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

# Función para editar libros
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

# Función para eliminar un libro por su código
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

# Función para asignar un libro a una categoría
def asignar_libro_a_categoria():
    codigo_libro = input('Ingrese código del libro: ')
    categoria_codigo = input('Ingrese código de la categoría: ')

    # Busca el libro por su código y la categoría por su código
    libro = negocio_libro.buscar_libro_por_codigo(codigo_libro)
    categoria = negocio_categoria.buscar_categoria_por_codigo(categoria_codigo)

    if libro and categoria:
        # Asigna la categoría al libro
        libro.asignar_categoria(categoria)
        print(f'Libro asignado a la categoría "{categoria.get_nombre_categoria()}".')
    else:
        print("El libro o la categoría no existen. Verifica los códigos ingresados.")



# Función para registrar una nueva categoría
def registrar_categoria():
    cod_categoria = input('Ingrese el código de la categoría: ')
    categoria = input('Ingrese el nombre de la categoría: ')
    negocio_categoria.registrar_categoria(cod_categoria, categoria)
    print(f'Categoría "{categoria}" registrada con éxito.')

# Función para editar una categoría existente
def editar_categoria():
    cod_categoria = input('Ingrese el código de la categoría que desea editar: ')
    nueva_categoria = input('Ingrese el nuevo nombre de la categoría: ')
    negocio_categoria.editar_categoria(cod_categoria, nueva_categoria)
    print(f'Categoría con código "{cod_categoria}" editada con éxito.')

# Función para listar todas las categorías
def listar_categorias():
    categorias = negocio_categoria.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        print("Lista de Categorías:")
        for categoria in categorias:
            # Obtener información sobre el libro asociado (si existe)
            libro_asociado = categoria.mostrar_libro()
            if libro_asociado:
                libro_info = f"Libro Asociado: Código - {libro_asociado.get_codigo_libro()}, Título - {libro_asociado.get_titulo()}"
            else:
                libro_info = "Sin libro asociado"

            print(f"Código de Categoría: {categoria.get_cod_categoria()}, Nombre: {categoria.get_nombre_categoria()}, {libro_info}")


# Función para eliminar una categoría por su código
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

# Define un diccionario que mapea opciones a funciones
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

# Bucle principal del programa
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

    # Verifica si la opción seleccionada está en el diccionario de opciones
    if seleccion in opciones:
        # Para las opciones 4, 8 y 13 se solicita el código correspondiente
        if seleccion == "4" or seleccion == "8" or seleccion == "13":
            codigo = input("Ingrese el código: ")
            opciones[seleccion](codigo)
        # La opción 6 muestra los libros y genera el reporte
        elif seleccion == "6":
            obtener_libros()  # Llama a la función para listar libros
            generar_reporte_libros(negocio_libro.obtener_libros())
        else:
            # Ejecuta la función correspondiente a la opción seleccionada
            opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
