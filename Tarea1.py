import random
import string

def generar_contraseña(minusculas=4, mayusculas=3, digitos=5):
    # Genera cadenas con el número de mayúsculas, minúsculas y dígitos solicitados
    letras_minusculas = random.choices(string.ascii_lowercase, k=minusculas)
    letras_mayusculas = random.choices(string.ascii_uppercase, k=mayusculas)
    numeros = random.choices(string.digits, k=digitos)
    
    # Ahora concatenamos las cadenas obtenidas
    contraseña = letras_minusculas + letras_mayusculas + numeros
    
    # Revolvemos la cadena contraseña
    random.shuffle(contraseña)
    
    # Unimos la lista en una cadena
    return ''.join(contraseña)

# Asignamos las variables
minusculas = 6
mayusculas = 8
digitos = 9

#print(generar_contraseña(minusculas, mayusculas, digitos))
