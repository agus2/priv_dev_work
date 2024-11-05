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