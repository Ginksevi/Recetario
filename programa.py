from funciones import *

while not finalizar_programa:    
    menu = incio()

    if menu == 1:
        mis_categorias = mostrar_categoria(ruta_acceso)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas para mostrar")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categoria(ruta_acceso)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(ruta_acceso)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categoria(ruta_acceso)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas para mostrar")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categoria(ruta_acceso)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True