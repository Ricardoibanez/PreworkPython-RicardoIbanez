'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.'''

millas_ingresadas = float(input('Escriba una distancia en millas para convertirla a km: '))

def km():
  print(millas_ingresadas, 'millas equivale a', millas_ingresadas * 1.60934, 'km')
  
km()
