#we use this kind of methods when whe want to transfor a list to another list with certain elements or transforming them or both
numeros_pares=[x for x in range (10)if x %2==0] #aqui de una lista de 10 numeros solo imrpime los que buscamos que son los pares
print(numeros_pares)
cuadrados=[x*x for x in numeros_pares] #en lugar de numeros pares podemos utilizar range
print(cuadrados)
pairs=[(x,y,z)
       for x in range (20)
       for y in range (20)
       for z in range (20)]
print(pairs)




