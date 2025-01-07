import requests
import csv
import logging

logging.basicConfig(level=logging.INFO)

url_base = "https://jsonplaceholder.typicode.com"
endpoints_array = [
    "/posts",  # endpoint que contiene los IDs
    "/posts/{}",
    "/posts/{}/comments"
]
token = "tu_token_aquí"  # reemplaza con tu token real

def extraer_datos(url):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error al obtener datos desde {url}: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error al obtener datos desde {url}: {e}")
        return None

def generar_csv(datos, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Obtener las claves de los datos (columnas del CSV)
        claves = list(datos[0].keys())
        
        # Escribir la cabecera del CSV
        writer.writerow(claves)
        
        # Escribir los datos en el CSV
        for dato in datos:
            writer.writerow([dato[clave] for clave in claves])

# Extraer IDs y otros datos del primer endpoint
primero_url = f"{url_base}{endpoints_array[0]}"
primero_data = extraer_datos(primero_url)

if primero_data is not None:
    # Guardar información del primer endpoint en un CSV
    filename_primero = f"{endpoints_array[0][1:]}.csv"
    generar_csv(primero_data, filename_primero)
    logging.info(f"CSV generado: {filename_primero}")
    
    # Extraer IDs de la respuesta JSON del primer endpoint
    ids = [dato["id"] for dato in primero_data]
    ids = [1,2,3] # para probar borrar
    # Utilizar IDs para extraer datos de otros endpoints
    for id in ids:
        for endpoint in endpoints_array[1:]:
            url_completa = f"{url_base}{endpoint.format(id)}"
            logging.info(f"Extrayendo datos desde {url_completa}")
            data = extraer_datos(url_completa)
            
            if data is not None:
                if isinstance(data, dict):  # Nota: se envuelve en una lista porque esperamos un solo registro
                    data = [data]
                '''
                En este código, se agrega una comprobación if isinstance(data, dict): 
                para verificar si la respuesta es un diccionario (es decir, un solo registro). 
                Si es así, se convierte a una lista con data = [data] antes de pasarla a la 
                función generar_csv. Esto permite manejar tanto respuestas con múltiples 
                registros como respuestas con un solo registro.
                '''
                filename_endpoint = f"{endpoint.format(id).replace('/', '')}.csv"
                generar_csv(data, filename_endpoint)
                logging.info(f"CSV generado: {filename_endpoint}")