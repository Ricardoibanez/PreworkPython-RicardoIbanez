'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

#Formula IMC = PESO /ALTURA *2

peso = float(input('introduzca su peso en kg: '))
altura = int(input('Introduzca su altura en cm: '))

resultado_IMC = peso / (altura/100)**2
print('Su IMC es de:', resultado_IMC)

