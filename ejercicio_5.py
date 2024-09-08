#                FUNCIONES LAMBDA

#Crea una función lambda que multiplique 3 números
print((lambda x, y, z: x * y * z)(10, 2, 4))

#Validar si una lista está vacía
print((lambda x: True if len(x) == 0 else False ) ([]))

#Validar si una lista tiene al menos 'n elementos'
print((lambda x, y: True if len(x) >= y else False ) ([],1))

#Calcular la raíz cuadrada de un número
print((lambda x: x**(1/2))(10))

#Obtener la intersección de dos conjuntos
print((lambda x, y: x.intersection(y))({1,2,3},{2}))


#                MAP AND FILTER

list1 = [1,2,3,4]
list2 = ["Hackers","Fight","club"]
list3 = ["Piccolo","Goku","Videl","Babidi","Broly"]
list4 = ["Python","Rust","Kotlin",""]

# Concatena las listas, filtra los elementos que contenga la letra i y pone en mayúsculas los elementos filtrados

print(list(map(lambda u: u.upper(), filter(lambda nombre: "i" in str(nombre), (lambda w,x,y,z: w+x+y+z) (list1,list2,list3,list4)))))


#              LISTAS POR COMPRENSIÓN

# Lista de números pares del 1 al 50

comp1 = [i for i in range(1,50) if i % 2 == 0]
print(comp1)

# Usa el anterior resultado para crear otra lista que tenga a los impares

print([i for i in comp1 if i % 2 != 0])

# Utilice una lambda para elevar los números del 1 al 10 al cuadrado

print(list(map(lambda square: square**2, [i for i in range(1,10)])))

# Utilice una lista de listas para crear otra lista de listas donde a cada elemento se le sume 1

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(map(lambda sublista: list(map(lambda x: x + 1, sublista)), lista)))