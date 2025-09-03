import math
#solicitar datos 
base= float(input("ingrese la base del tereno en metros:"))
altura=float(input("ingrese la altura de terrenoen metros:"))
#calcular la base del terreno
area_triangulo=base*altura/2
area_cuadrado=base*base
area_total=(area_triangulo+area_cuadrado)
preciodeltereno=4400000
precio_total=area_total*preciodeltereno
print("el area del terreno es :",area_total,"m")
print("el precio total del terreno es:",precio_total,"pesos")
