'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

oracion_ingresada = str(input('Escriba una oración con las palabras que desee: '))

palabras = oracion_ingresada.split()
contador = 0

for palabra in palabras:
  contador += 1
print('la oración ingresada contiene', contador, 'palabras')

