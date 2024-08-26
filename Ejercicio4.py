'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

contador_vocales = 0

texto = str(input('Escriba la palabra que desee contar sus vocales: '))
for letra in texto:
  if letra in 'aeiouAEIOU':
    contador_vocales += 1
print('La palara ingresada', (texto), 'contiene', (contador_vocales), 'vocales')

