import re

cadena = "Esta es una cadena con saltos de linea."
cadena_modificada = re.sub(r"linea", "línea\n", cadena)
print(cadena_modificada)

cadena = 'Esta cadena contiene comillas simples\' simple \'dentro.'
print(cadena)

nombre = "Juan"
edad = 25
cadena = f"{nombre} tiene {edad} años."
print(cadena)

from pathlib import Path

def buscar_palabras_en_fichero(nombre_fichero, palabras_clave):
    lineas_encontradas = []  # Lista para almacenar las líneas donde se encuentran las palabras clave
    
    try:
        with open(nombre_fichero, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                # Comprobar si alguna palabra clave está en la línea
                if any(palabra in linea for palabra in palabras_clave):
                    lineas_encontradas.append(numero_linea)  # Guardar el número de línea
        return lineas_encontradas
    
    except FileNotFoundError:
        print(f"El archivo '{nombre_fichero}' no se encontró.")
        return []
nombre_fichero = "texto.txt"
palabras_clave = ["palabra1", "palabra2", "palabra3"]

lineas = buscar_palabras_en_fichero(nombre_fichero, palabras_clave)
if lineas:
    print(f"Las palabras clave se encontraron en las líneas: {lineas}")
else:
    print("No se encontraron las palabras clave en el archivo.")

def existe_fichero(nombre_fichero):
    return Path(nombre_fichero).is_file()
nombre_fichero = "texto.txt"
if existe_fichero(nombre_fichero):  print(f"El archivo '{nombre_fichero}' existe.")
else:   print(f"El archivo '{nombre_fichero}' no existe.")