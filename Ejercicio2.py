'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

camarones = 10
alcachofas = 10
cocacola = 2

cuenta = [camarones, alcachofas, cocacola]
euros = 0
for plato in cuenta:
  euros += plato
total = euros * 1.15
print(total)
