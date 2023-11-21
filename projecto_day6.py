from pathlib import Path

ruta_acceso = Path('Day_6\Projecto_Day6\Recetas')
print(f"Bienvenido al recetario\nEsta es la ruta de acceso donde se encuentras nuestras recetas '{ruta_acceso}'")

print("Estas son nuestras recetas disponibles")
recetas = Path('Day_6\Projecto_Day6\Recetas').glob("**/*.txt")
for res in recetas:
    print(res)


opciones = list(range(1,7))