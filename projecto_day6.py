from pathlib import Path
import os

ruta_acceso = Path('Day_6\Projecto_Day6\Recetas')

def contar_recetas(ruta):
    contador = 0
    for res in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

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

incio()