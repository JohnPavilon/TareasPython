# Hacer un diccionario por comprensión

# Las llaves son los números odiosos menores a 50 y el valor es una tupla de
# dos elementos: su representación en binario y su representación en hexadecimal

# Un número odioso (odious number) es todo aquél que su representación en binario tiene un número impar de unos

odious_numbers = [(i,(bin(i)[2:], hex(i)[2:])) for i in range(1, 50) if bin(i)[2:].count('1') % 2 == 1] 
print(dict(odious_numbers))