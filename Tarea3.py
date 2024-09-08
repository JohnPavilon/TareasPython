from Tarea1 import generar_contraseña

# Paso 1: Leemos el archivo y obtenemos cada palabra de cada línea
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        palabras = archivo.read().splitlines()
    return palabras

# Paso 2: Hacemos diferentes funciones para hacer "seguras" nuestras contraseñas

# Genera un diccionario con las letras a reemplazar y las reemplaza en la entrada dada
def reemplazar_letras_por_numeros(palabra):
    reemplazos = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    return ''.join(reemplazos.get(c, c) for c in palabra)

# Hace un intercambio de mayúsculas a minúsculas y viceversa
def cambiar_mayusculas_minusculas(palabra):
    return palabra.swapcase() 

# Usamos nuestro generador de contraseñas "seguras" de la tarea 1 y la concatenamos a nuestra palabra
def concatenar_con_numeros_y_simbolos(palabra):
    return palabra + generar_contraseña() 

# Paso 3: Generamos todas las contraseñas posibles por cada función
def generar_contraseñas(palabras):
    posibles_contraseñas = []
    for palabra in palabras:
        posibles_contraseñas.append(reemplazar_letras_por_numeros(palabra))
        posibles_contraseñas.append(cambiar_mayusculas_minusculas(palabra))
        posibles_contraseñas.append(concatenar_con_numeros_y_simbolos(palabra))
        posibles_contraseñas.append(concatenar_con_numeros_y_simbolos(cambiar_mayusculas_minusculas(reemplazar_letras_por_numeros(palabra))))

    return posibles_contraseñas

# Paso 4: Guardamos las contraseñas en un nuevo archivo de salida
def escribir_contraseñas(nombre_archivo_salida, contraseñas):
    with open(nombre_archivo_salida, 'w') as archivo:
        for contraseña in contraseñas:
            archivo.write(contraseña + '\n')

# Paso 5: Creamos una nueva función que ejecute los pasos anteriores
def generador_de_diccionarios(nombre_archivo_entrada, nombre_archivo_salida):
    palabras = leer_archivo(nombre_archivo_entrada)
    contraseñas = generar_contraseñas(palabras)
    escribir_contraseñas(nombre_archivo_salida, contraseñas)

# Ejecuta el programa
generador_de_diccionarios('cosas.txt', 'diccionario.txt')
