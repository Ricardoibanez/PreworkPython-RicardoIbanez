'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''

longitud = float(input('Escriba la longitud deseada del rectangulo: '))
ancho = float(input('Escriba el ancho deseado del rectangulo: '))

def area_rectangulo():
  print('El area del rectangulo es: ', longitud * ancho)

area_rectangulo()
