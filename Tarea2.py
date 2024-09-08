import random

def adivina_el_numero():
    # Seleccionar un número entre 1 y 100
    numero_objetivo = random.randrange(1,100)
    
    print("¡Comencemos el juego! Adivina el número entre 1 y 100.")
    
    while True:
        # Imprimimos en pantalla este mensaje para que el jugador adivine
        intento = input("Adivina el número (o escribe 'salir' para terminar): ")
        
        # Si queremos salir del juego, escribimos salir
        if intento.lower() == 'salir':
            print("¡Gracias por jugar!")
            break
        
        # Intentamos convertir la entrada en un número entero
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, introduce un número entero válido.")
            continue
        
        # Validamos si el número está en el rango correcto
        if intento < 1 or intento > 100:
            print("Por favor, introduce un número entre 1 y 100.")
            continue
        
        # Mandamos mensaje al jugador dependiendo de su respuesta
        else:
            if intento < numero_objetivo:
                print("El número es mayor.")
            elif intento > numero_objetivo:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break

# Ejecutamos el juego
adivina_el_numero()
