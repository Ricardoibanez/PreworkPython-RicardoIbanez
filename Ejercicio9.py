'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''

cambio = float(input('Introduzca el importe que quiere convertir de dólares a euros:'))

conversor = cambio * 0.85
print('Según la cantidad de dólares escrita: ', cambio, 'obtendría una cantidad de: ', conversor, 'euros')

