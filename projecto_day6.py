from pathlib import Path
import os

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
        eleccion_menu = input("Elige una opción: ")
    return (eleccion_menu)
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