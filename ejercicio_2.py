#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

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

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))


asigna_calificaciones()

def tuplas():
    aprobados =  ()
    reprobados = ()

    for alumno in calificacion_alumno:
        if calificacion_alumno[alumno] >= 7:
            aprobados = aprobados + (alumno,)
        if calificacion_alumno[alumno] < 7:
            reprobados =  reprobados + (alumno,)

    return aprobados,reprobados

def promedio():
    return sum(alumnos for alumnos in calificacion_alumno.values())/len(calificacion_alumno)

def calificaciones():
    return set(calificacion_alumno.values())

alumnos = tuplas()
print(alumnos)

prom = promedio()
print(prom)

calif = calificaciones()
print(calif)
