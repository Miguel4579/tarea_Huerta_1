import numpy as np
a = float(input("Ingrese la cantidad de kilos que va a comprar: "))

if a < 3:
    precio = a*2.4

elif 3 <= a <6:
    precio = a*2.3

elif 6<= a < 10:
    precio = a*2.1

elif 10 <= a:
    precio = a*1.85

print("Debe pagar "+str(precio))
jaaaaaah