'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

minutos = int(input('Escriba el numero de minutos para su conversion: '))

hora = minutos // 60
minutos_ajustado = minutos % 60

print('la conversion es: ',hora,'horas',minutos_ajustado,'minutos')
