#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice
from poo1 import Alumno

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
    'Angel Sánchez',
    'Esteban Arellanes',
    'Danna Márquez',
    'Fernando Romero',
    'Alberto Medel',
    'Luis Lira',
    'Obed Torres',
    'Oscar Caballero',
    'Oscar Ríos',
    'Stephany Marín',
    'Jonathan Valencia',
    'Valeria Ramírez',
    'Israel Villanueva',
    'Juan Legorreta']

def crea_alumnos():
    lista_alumnos=[]
    for b in becarios:
        lista_alumnos = lista_alumnos+[Alumno(b,choice(calificaciones))]

    return lista_alumnos

list = crea_alumnos()
for i in list:
    i.ve_calificacion()