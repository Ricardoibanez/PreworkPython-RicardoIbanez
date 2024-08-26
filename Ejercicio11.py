'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''

fecha_de_nacimiento = int(input('Escriba el año en que naciste: '))

import datetime
fecha = datetime.datetime.now()

def edad_actual():
  print('Tu edad actual teniendo en cuenta únicamente los años es de: ', fecha.year - fecha_de_nacimiento)


edad_actual()
