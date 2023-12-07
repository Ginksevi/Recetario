from pathlib import Path
import os
""" Todas las funciones han sido almacenadas en este archivo """
#--------------------------------------------------------------------------------------

ruta_acceso = Path('Day_6\Projecto_Day6\Recetas')

#***************************************************************************************

def contar_recetas(ruta):
    contador = 0
    for res in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

#****************************************************************************************

def incio():
    os.system("cls")
    print("*" * 50)
    print("*" * 12 + " Bienvenido al recetario " + "*" * 12)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuntran en {ruta_acceso}")
    print(f"Total de recetas es: {contar_recetas(ruta_acceso)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Menu")
        print('''
        [1] - Leer receta
        [2] - Crear nueva receta
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir de la aplicación''')
        eleccion_menu = input("\nElige una opción: ")
    return int(eleccion_menu)

#***********************************************************************************************

def mostrar_categoria(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

#***********************************************************************************************

def elegir_categoria(lista):
    eleccion = 'x'

    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElije una categoria: ")
    return lista[int(eleccion) - 1]

#***********************************************************************************************

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

#************************************************************************************************

def elegir_recetas(lista):
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElige una receta: ")
    return lista[int(eleccion) - 1]

#************************************************************************************************

def leer_receta(receta):
    print(Path.read_text(receta))

#************************************************************************************************

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta '{nombre_receta}' a sido creada")
            existe = True
        else:
            print("La receta ya existe")

#*************************************************************************************************

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"LA nueva categoria '{nombre_categoria}' a sido creada")
            existe = True
        else:
            print("La categoria ya existe")

#**************************************************************************************************

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta '{receta.name}' a sido eliminada")

#**************************************************************************************************

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria '{categoria.name}' a sido eliminada")

#**************************************************************************************************

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'q':
        eleccion_regresar = input("\nPresione 'Q' para volver al menu: ")

#**************************************************************************************************

finalizar_programa = False