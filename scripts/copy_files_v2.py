import os
import shutil
import argparse

def copiar_fichero_a_ruta(ruta_destino, fichero_origen):
    try:
        # Convertir las rutas a absolutas
        ruta_base = os.getcwd()
        ruta_destino_absoluta = os.path.abspath(ruta_destino)
        fichero_origen_absoluto = os.path.abspath(fichero_origen)

        # Verificar si el fichero origen existe
        if not os.path.isfile(fichero_origen_absoluto):
            print(f"El fichero origen '{fichero_origen}' no existe. Saltando...")
            return
        
        # Crear la ruta destino si no existe
        if not os.path.exists(ruta_destino_absoluta):
            os.makedirs(ruta_destino_absoluta)

        # Obtener el nombre del fichero origen
        nombre_fichero = os.path.basename(fichero_origen_absoluto)

        # Generar la ruta completa de destino
        ruta_completa_destino = os.path.join(ruta_destino_absoluta, nombre_fichero)

        # Copiar el fichero
        shutil.copy(fichero_origen_absoluto, ruta_completa_destino)
        ruta_relativa_destino = os.path.relpath(ruta_completa_destino, ruta_base)
        print(f"El fichero '{nombre_fichero}' ha sido copiado a '{ruta_relativa_destino}'.")

    except Exception as e:
        print(f"Error al copiar el fichero: {e}")

def procesar_fichero_listado(ruta_listado):
    try:
        # Verificar si el fichero de listado existe
        if not os.path.isfile(ruta_listado):
            print(f"El fichero de listado '{ruta_listado}' no existe.")
            return

        # Leer el fichero línea a línea
        with open(ruta_listado, "r") as archivo:
            for linea in archivo:
                # Saltar líneas vacías
                if not linea.strip():
                    continue

                # Separar origen y destino por un separador, por ejemplo, una coma
                try:
                    fichero_origen, ruta_destino = linea.strip().split(",")
                    copiar_fichero_a_ruta(ruta_destino.strip(), fichero_origen.strip())
                except ValueError:
                    print(f"La línea '{linea.strip()}' no tiene el formato correcto. Use 'origen,destino'.")

    except Exception as e:
        print(f"Error al procesar el fichero de listado: {e}")

if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Copiar múltiples ficheros según un archivo de listado.")
    parser.add_argument("fichero_listado", help="Ruta del fichero que contiene las rutas de origen y destino.")

    # Parsear argumentos
    args = parser.parse_args()

    # Procesar el fichero de listado
    procesar_fichero_listado(args.fichero_listado)

'''
Formato del Archivo de Listado

./datos/origen/fichero1.txt, ./destino/carpeta1
./datos/origen/fichero2.txt, ./destino/carpeta2
./datos/origen/fichero3.txt, ./destino/carpeta1

$
python copiar_desde_listado.py listado.txt


Salida Esperada:

El fichero 'fichero1.txt' ha sido copiado a 'destino/carpeta1/fichero1.txt'.
El fichero 'fichero2.txt' ha sido copiado a 'destino/carpeta2/fichero2.txt'.
El fichero 'fichero3.txt' ha sido copiado a 'destino/carpeta1/fichero3.txt'.
'''