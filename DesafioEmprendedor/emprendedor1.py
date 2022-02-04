import math

p = float(input("Ingrese el precio de suscripción:\n>"))
u = float(input("Ingrese el numero de usurios:\n>"))
gastoTotal= float(input("Ingrese el Gasto Total:\n>"))


utilidades = p * u - gastoTotal

print(f'Las utilidades son: {math.ceil(utilidades)}')
