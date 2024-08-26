'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))
c = str(input('Elija la operacion simple que desea realizar ( suma, resta, multiplicacion o division): '))

if c == 'suma':
  print(a + b)
elif c == 'resta':
  print(a - b)
elif c == 'multiplicacion':
  print(a * b)
else:
  print(a / b)

