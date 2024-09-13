import requests

# Ejercicio 1: Realiza una petición GET a https://jsonplaceholder.typicode.com/ para obtenerel post con el ID 1
# Luego imprime el título y el cuerpo

respuesta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if respuesta.status_code == 200:
    post = respuesta.json()
    print("Título:", post['title'])
    print("Cuerpo:", post['body'])
else:
    print("Error al obtener el post:", respuesta.status_code)


# Ejercicio 2: Realiza una petición POST a https://jsonplaceholder.typicode.com/posts enviando un título, cuerpo
# y un userId. Imprime la respuesta del servidor

response = requests.post('https://jsonplaceholder.typicode.com/posts', data = {'userID': '10', 'title':"qui qui voluptates illo iste minima", 'body': "aspernatur expedita soluta quo ab ut similique\nexpedita dolores amet\nsed temporibus distinctio magnam saepe deleniti\nomnis facilis nam ipsum natus sint similique omnis"})

if respuesta.status_code == 200:
    print(response.text)
else:
    print("Error al obtener el post:", respuesta.status_code)

# Ejercicio 3: Realiza otra petición https://jsonplaceholder.typicode.com/ para registrar un nuevo usuario

# Datos del nuevo usuario
nuevo_usuario = {
    "name": "Juan Pérez",
    "username": "juanperez",
    "email": "juan.perez@example.com",
    "phone": "555-1234",
    "website": "juanperez.com",
}

# Realizar la solicitud POST
respuesta = requests.post('https://jsonplaceholder.typicode.com/users', json=nuevo_usuario)

# Verificar la respuesta
if respuesta.status_code == 201:
    print("Usuario registrado exitosamente:")
    print(respuesta.json())
else:
    print("Error al registrar el usuario:", respuesta.status_code)

# Ejercicio 4: Crea un nuevo usuario, pero ahora en https://reqres.in/ e imprime el token que está en la respuesta.

# Datos del nuevo usuario
nuevo_usuario = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

# Realizar la solicitud POST
respuesta = requests.post('https://reqres.in/api/register', json=nuevo_usuario)

# Verificar la respuesta
if respuesta.status_code == 201:
    user = respuesta.json()
    print("Usuario registrado exitosamente:")
    print(user["token"])
else:
    print("Error al registrar el usuario:", respuesta.status_code)