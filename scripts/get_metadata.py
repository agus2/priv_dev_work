import os
import eyed3
import csv

def obtener_metadatos(carpeta, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Archivo', 'Título', 'Artista', 'Año', 'Género', 'Comentario']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".mp3"):
                archivo_path = os.path.join(carpeta, archivo)
                audio_file = eyed3.mp3.MP3(archivo_path)

                writer.writerow({
                    'Archivo': archivo,
                    'Título': audio_file.tag.title,
                    'Artista': audio_file.tag.artist,
                    'Año': audio_file.tag.year,
                    'Género': audio_file.tag.genre,
                    'Comentario': audio_file.tag.comments
                })

# Ejemplo de uso:

'''
carpeta = "/ruta/a/la/carpeta/con/canciones/mp3"
output_file = "metadatos.csv"
obtener_metadatos(carpeta, output_file)
'''
import os

# Obtener la ruta absoluta de la carpeta actual
# print(os.path.dirname(os.path.dirname((os.path.abspath(".")))))
ruta_actual = os.path.abspath(".")

# Obtener la ruta absoluta de la carpeta 2 niveles arriba
ruta_2_niveles_arriba = os.path.dirname(os.path.dirname(ruta_actual))

# Obtener la ruta relativa desde la carpeta actual hasta la carpeta 2 niveles arriba
ruta_relativa = os.path.relpath(ruta_2_niveles_arriba, ruta_actual)

print(ruta_relativa)


import os

# Especificar la ruta de la carpeta


# Listar todos los archivos en la carpeta
archivos = os.listdir(ruta_relativa+"\\AGUS_VARIOS_REGGAETON_DEMBOW")
# Imprimir la lista de archivos
print(archivos)