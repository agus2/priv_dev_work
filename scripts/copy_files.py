import os
import shutil
import argparse

def copiar_fichero_a_ruta(ruta_destino, fichero_origen):
    try:
        # Convertir las rutas a rutas absolutas (para asegurarnos que todo funcione bien internamente)
        ruta_base = os.getcwd()  # Obtiene la ruta actual del script
        ruta_destino_absoluta = os.path.abspath(ruta_destino)
        fichero_origen_absoluto = os.path.abspath(fichero_origen)

        # Verificar si el fichero origen existe
        if not os.path.isfile(fichero_origen_absoluto):
            print(f"El fichero origen '{fichero_origen}' no existe.")
            return
        
        # Verificar si la ruta destino existe, si no, la crea
        if not os.path.exists(ruta_destino_absoluta):
            os.makedirs(ruta_destino_absoluta)
            print(f"La ruta destino '{ruta_destino_absoluta}' no existía y ha sido creada.")

        # Obtener el nombre del fichero origen
        nombre_fichero = os.path.basename(fichero_origen_absoluto)

        # Generar la ruta completa de destino
        ruta_completa_destino = os.path.join(ruta_destino_absoluta, nombre_fichero)

        # Copiar el fichero
        shutil.copy(fichero_origen_absoluto, ruta_completa_destino)

        # Mostrar rutas relativas en el mensaje final
        ruta_relativa_destino = os.path.relpath(ruta_completa_destino, ruta_base)
        print(f"El fichero '{nombre_fichero}' ha sido copiado a '{ruta_relativa_destino}'.")

    except Exception as e:
        print(f"Error al copiar el fichero: {e}")

if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Copiar un fichero a una ruta relativa especificada.")
    parser.add_argument("ruta_destino", help="Ruta relativa donde se copiará el fichero.")
    parser.add_argument("fichero_origen", help="Ruta relativa del fichero origen a copiar.")

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con los parámetros proporcionados
    copiar_fichero_a_ruta(args.ruta_destino, args.fichero_origen)