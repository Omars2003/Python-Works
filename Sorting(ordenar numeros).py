#Sort method sirve para ordenar una lista de numeros en orden
x=[1,2,2,3,4,7,8,3,6,5,4,9,3,2,1,4,5,9,7]
y=sorted(x) #se almancena la cadena ordenada en otra variable
x.sort() #la cadena desordenada se imprime en la misma variable
print(y,x)
#para hacerlo de mayor a menor  ocupamos reverse=T rue
w=sorted([1,2,3,4,5,6,6,7],key=abs,reverse=True) #key=abs en especifico key nos permite moldear los datos de la manera que queramos, abs=absoluto
print(w)
