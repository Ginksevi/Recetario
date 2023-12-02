# Estructura del recetario
# Mostrar un menu de inicio al usuario

from projecto_day6 import *

menu = 0

if menu == 1:
    mis_categorias = mostrar_categoria(ruta_acceso)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    # Leer receta
    # Volver a inicio
    pass
elif menu == 2:
    mis_categorias = mostrar_categoria(ruta_acceso)
    mi_categoria = elegir_categoria(mis_categorias)
    # Crear nueva receta
    # Volver a inicio
    pass
elif menu == 3:
    # Crear categoria
    # Volver a incio
    pass
elif menu == 4:
    mis_categorias = mostrar_categoria(ruta_acceso)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    # Eliminar receta
    # Volver a inicio
    pass
elif menu == 5:
    mis_categorias = mostrar_categoria(ruta_acceso)
    mi_categoria = elegir_categoria(mis_categorias)
    # Eliminar categoria
    # Volver a inicio
    pass
elif menu == 6:
    # Terminar el programa
    pass