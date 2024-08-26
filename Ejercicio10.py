'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

usuario = float(input('Escriba un número del 1 - 7 para determinar el día de la semana: '))
if usuario == 1:
  dia = 'Lunes'
elif usuario == 2:
  dia = 'Martes'
elif usuario == 3:
  dia = 'Miércoles'
elif usuario == 4:
  dia = 'jueves'
elif usuario == 5:
  dia = 'Viernes'
elif usuario == 6:
  dia = 'Sábado'
else:
  dia = 'Domingo'

print(dia)
