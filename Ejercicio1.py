'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''

# Fórmula conversion grados centígrados a Farenheit: (X * 9/5 + 32)

Grados_centigrados = float(input("Ingrese el dato numérico para su conversion a farenheit: "))
Grados_Farenheit = (Grados_centigrados * (9/5) + 32)
print('el resultado es:', Grados_Farenheit, 'grados Farenheit')