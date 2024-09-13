import os
import re
import argparse

def fuerza_bruta_xor(archivo, nombre_descifrado):

    # Manejo de excepciones en caso de no encontrar el archivo
    if not os.path.exists(archivo):
        print(f"Error: El archivo {archivo} no existe.")
        return
    
    # Error si el archivo no es binario
    try:
        with open(archivo, 'rb') as archivo_binario:
            contenido = archivo_binario.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Aplicamos fuerza bruta, intenta todos los valores posibles de un byte (0-255)
    for xor_value in range(256): 
        xor_data = bytes(byte ^ xor_value for byte in contenido) # Aplicamos XOR
        
        if b"This program" in xor_data:
            m = re.search(b"MZ", xor_data)
            if m:
                try:
                    # Guardar el archivo descifrado para análisis posterior
                    with open(nombre_descifrado, 'wb') as archivo_descifrado:
                        archivo_descifrado.write(xor_data[m.start():])
                    print(f"Archivo descifrado guardado como: {nombre_descifrado}")
                except Exception as e:
                    print(f"Error al guardar el archivo descifrado: {e}")
                break
    else:
        print("No se encontró una clave XOR válida.")

parser = argparse.ArgumentParser(description="Programa para descifrar un programa ejecutable puesto en cuarentena")
parser.add_argument("--archivo", type=str, default="57FD6325.VBN", help="Nombre del archivo puesto en cuarentena")
parser.add_argument("--d", type=str, default="descifrado_165", help="Nombre del archivo descifrado")
args = parser.parse_args()

fuerza_bruta_xor(args.archivo, args.d)
