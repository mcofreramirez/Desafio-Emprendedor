import math

p = float(input("Ingrese el precio de suscripción:\n>"))
u = float(input("Ingrese el numero de usurios:\n>"))
gastoTotal= float(input("Ingrese el Gasto Total:\n>"))


utilidades = p * u - gastoTotal



utilidadesAnterior = float(input("Ingrese las utilidades del año anterior\n>"))

print(f'Las utilidades actuales son: {math.ceil(utilidades)}')

print(f'Las utilidades año anterior  son: {math.ceil(utilidadesAnterior)}')

razon= utilidades / utilidadesAnterior

print(f'La razon de las utilidades actuales con la anterior  son: {razon:.2f}') 