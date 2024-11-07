import re

def generar_lineas_con_cadenas(nombre_fichero):
    # Lista para almacenar las nuevas líneas generadas
    nuevas_lineas = []
    
    # Leer el archivo línea por línea
    with open(nombre_fichero, 'r') as archivo:
        for linea in archivo:
            # Buscar el contenido dentro de los corchetes y el texto antes y después
            match = re.search(r'(.*?)\[(.*?)\](.*)', linea)
            
            # Verificar si se encontró el patrón con corchetes
            if match:
                antes = match.group(1).strip()  # Texto antes de los corchetes
                dentro = match.group(2)         # Contenido dentro de los corchetes
                despues = match.group(3).strip()  # Texto después de los corchetes
                
                # Dividir el contenido encontrado por comas para obtener cada elemento
                elementos = dentro.split(',')
                
                # Procesar solo si hay más de un elemento entre corchetes
                if len(elementos) > 1:
                    # Crear una nueva línea para cada elemento encontrado dentro de los corchetes
                    for elemento in elementos:
                        # Concatenar el texto antes, el elemento (dentro de corchetes) y el texto después
                        nueva_linea = f"{antes} [{elemento.strip()}] {despues}".strip()
                        nuevas_lineas.append(nueva_linea)
                else:
                    # Ignorar la línea si solo tiene un elemento entre corchetes
                    #print("Línea ignorada (solo un elemento entre corchetes):", linea.strip())
                    nuevas_lineas.append(linea.strip())
            else:
                # Si no se encontraron corchetes, simplemente guardar la línea original
                nuevas_lineas.append(linea.strip())
    
    return nuevas_lineas


# Ejemplo de uso
nombre_fichero = "texto.txt"
cadenas = generar_lineas_con_cadenas(nombre_fichero)

# Mostrar las cadenas encontradas
# print("Cadenas encontradas entre corchetes:")
for cadena in cadenas:
    print(cadena)