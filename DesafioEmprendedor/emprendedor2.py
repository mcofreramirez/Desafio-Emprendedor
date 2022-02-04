import math

p = float(input("Ingrese el precio de suscripción:\n>"))
un = float(input("Ingrese el numero de usurios Normales:\n>"))
up = float(input("Ingrese el numero de usurios Premium:\n>"))
gastoTotal= float(input("Ingrese el Gasto Total:\n>"))


utilidades = (p * un *(up*1.5)) - gastoTotal

print(f'Las utilidades son: {math.ceil(utilidades)}')