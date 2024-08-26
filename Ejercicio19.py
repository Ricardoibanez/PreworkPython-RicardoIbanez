'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

años_bisiestos = range(2024,999999999999999,4)
año_ingresado = int(input('Escriba un año para saber si es bisiesto o no: '))

if año_ingresado in años_bisiestos:
  print('El año ingresado: ', año_ingresado, 'es bisiesto')
else:
  print('el año ingresado: ', año_ingresado, 'no es bisiesto')
  
