import Usuario as U
import re
import hashlib

# Excepciones personalizadas
class PasswordInvalido(Exception):
    pass

class MuchosIntentos(Exception):
    pass

# Función para crear usuarios
def crear_usuarios():
    users = {
        'Angel': ("example@gmail.com", "48d2a5bbcf422ccd1b69e2a82fb90bafb52384953e77e304bef856084be052b6"),
        'Esteban': ("example@gmail.com", "c9c835ab63d384722377be29d1eebd8bbd6f92258f93116321bb5b64144d88e3"),
        'Danna': ("example@gmail.com", "da2ae54a481d947ffdda658ae84ea1be7b5543b75d571d1d22f55a3aff78977f"),
        'Fernando': ("example@gmail.com", "ff6d804ba949e91b79e9596a5e0604eb464d248c0d42659157c5733b556d1405"),
        'Alberto': ("example@gmail.com", "870a81eb53d9b9f11ab598945c0af7fa6b6391420e583fddb1ed863c78fa2292"),
        'Luis': ("example@gmail.com", "6da2b52ff51eb8497d787552e66f4ab673aee0e05aea3d31bd818cf0c88a6f9e"),
        'Obed': ("example@gmail.com", "c1769d75226ae34079f9d48736fc0068ce8931794138c2538dde961a321f5a9b"),
        'Oscar': ("example@gmail.com", "759441099cd1429e46b05ae5db916b3fc5cc90094b055dee6204bebf7f63d69b"),
        'Stephany': ("example@gmail.com", "a4ea55c9f015603bd027142ce317d00926536fc86772c3437843ca86482797d1"),
        'Jonathan': ("example@gmail.com", "a0c33b9a5e6b8c7cfc2bcaa4f43fffea77100227b63cd049587c574efce90110"),
        'Valeria': ("example@gmail.com", "40f20ca783ebf8c081ca9552f0a17c8098b36c3313637fe01ba099105a020e10")
    }

    diccionario_usuarios = {}
    for nombre, (email, password_hash) in users.items():
        usuario = U.Usuario(nombre, email, password_hash)
        diccionario_usuarios[nombre] = usuario

    return diccionario_usuarios

# Función para generar el hash de una contraseña
def generar_hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

# Función para incrementar intentos y verificar límite
def incrementar_intentos(intentos):
    intentos += 1
    if intentos >= 5:
        print('Ha superado el límite de 5 intentos.')
        raise MuchosIntentos
    return intentos

# Crear los usuarios y almacenarlos en un diccionario
usuarios = crear_usuarios()
anycase = r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$'
intentos = 0

while True:
    option = input('Bienvenido, Seleccione una opción:\n 1: Iniciar sesión\n 2: Salir\n')
    try:
        option = int(option)
        if option not in [1, 2]:  # Validamos que solo sea 1 o 2
            raise ValueError('Opción no válida')
    except ValueError:
        print("Por favor, introduce una opción válida.")
        continue

    if option == 2:
        print("Gracias por su visita.")
        break

    user = input("Ingresa tu usuario: ")
    pwd = input("Ingresa tu contraseña: ")

    try:
        # Validar la contraseña
        if len(pwd) <= 5 or not re.match(anycase, pwd):
            raise PasswordInvalido('La contraseña debe tener al menos 5 caracteres y contener tanto letras como números.')
        
        # Verificar si el usuario existe en el diccionario
        if user not in usuarios:
            print("Usuario no encontrado.")
            intentos = incrementar_intentos(intentos)
            continue

        # Verificar si la contraseña hash coincide para el usuario
        if usuarios[user].is_password(pwd):
            print(f"Hola {user}, bienvenido.")
            break
        else:
            print("Contraseña incorrecta.")
            intentos = incrementar_intentos(intentos)

    except PasswordInvalido as e:
        print(e)
        intentos = incrementar_intentos(intentos)
    except MuchosIntentos:
        break
