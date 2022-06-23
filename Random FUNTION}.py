import random
cuatro_numerosrandom_uniformes=[random.random()for _ in range(4)]  #imprime cuatro numeros con valores uniformes de 0 a 1
print(cuatro_numerosrandom_uniformes)
y=random.randrange(10) # le estas indicando el rango en este caso eligira un numero de 0,9
print(y)
# PARA ELEGIRR RANDOM DE UNA LISTA HCAEMOS LO SIGUIENTE
my_best_friends=random.choice(["Luis","Axel","Lau","Jafi","Emi","Vic","Mon","Nat","Pabli","Pau","Danita"])
print(my_best_friends)
#para imprimir multiples valores en un rnago sin que se repitan usamos randon.sample creando una nueva sin moveer la del range
BoletosDeLoteria=range(1000)
ganadores=random.sample(BoletosDeLoteria,10)
print(ganadores)
#si queremos que se repitan los numeros usamos random.choice