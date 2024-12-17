import re

def generar_lineas_con_cadenas(nombre_fichero):

    nuevas_lineas = []

    with open(nombre_fichero, 'r') as archivo:
        for linea in archivo:
            match = re.search(r'(.*?)\[(.*?)\](.*)', linea)
            
            if match:
                antes = match.group(1).strip()
                dentro = match.group(2)
                despues = match.group(3).strip()

                elementos = dentro.split(',')
                if len(elementos) > 1:
                    for elemento in elementos:
                        nueva_linea = f"{antes} [{elemento.strip()}] {despues}".strip()
                        nuevas_lineas.append(nueva_linea)
                else:
                    nuevas_lineas.append(linea.strip())
            else:
                nuevas_lineas.append(linea.strip())
    
    return nuevas_lineas

nombre_fichero = "texto.txt"
cadenas = generar_lineas_con_cadenas(nombre_fichero)
for cadena in cadenas:
    print(cadena)