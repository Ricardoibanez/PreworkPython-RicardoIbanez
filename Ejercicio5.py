'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''


i = 0
suma = 0
while i <= 100:
  if i % 2 == 0:
    suma = suma + i
  i += 1
print(suma)