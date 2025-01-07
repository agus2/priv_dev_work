import requests
import csv
import logging

logging.basicConfig(level=logging.INFO)

url_base = "https://jsonplaceholder.typicode.com"
endpoints_array = [
    "/posts",  # endpoint que contiene los IDs
    "/posts/{id}",
    "/posts/{id}/comments"
]

def extraer_datos(url):
    try:
        response = requests.get(url)
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

# Extraer IDs del endpoint que los contiene
primero_url = f"{url_base}{endpoints_array[0]}"
primero_data = extraer_datos(primero_url)

if primero_data is not None:
    # Guardar información del primer endpoint en un CSV
    filename_primero = f"{endpoints_array[0][1:]}.csv"
    generar_csv(primero_data, filename_primero)
    logging.info(f"CSV generado: {filename_primero}")
    
    # Extraer IDs de la respuesta JSON del primer endpoint
    ids = [dato["id"] for dato in primero_data]
    
    # Utilizar IDs para extraer datos de otros endpoints
    for id in ids:
        url_post_id = f"{url_base}{endpoints_array[1].format(id=id)}"
        logging.info(f"Extrayendo datos desde {url_post_id}")
        post_id_data = extraer_datos(url_post_id)
        
        if post_id_data is not None:
            filename_post_id = f"post_{id}.csv"
            generar_csv([post_id_data], filename_post_id)  # Nota: se envuelve en una lista porque esperamos un solo registro
            
            url_comments_id = f"{url_base}{endpoints_array[2].format(id=id)}"
            logging.info(f"Extrayendo comentarios desde {url_comments_id}")
            comments_id_data = extraer_datos(url_comments_id)
            
            if comments_id_data is not None:
                filename_comments_id = f"comments_{id}.csv"
                generar_csv(comments_id_data, filename_comments_id)
                logging.info(f"CSV generado: {filename_comments_id}")