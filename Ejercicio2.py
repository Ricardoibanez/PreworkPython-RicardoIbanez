'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

cuenta = float(input('Ingrese la totalidad de la cuenta sin propina: '))
total_cuenta = cuenta * 1.15
print(f'El monto total a pagar con un 15 % de propina es: ', total_cuenta, '€')

