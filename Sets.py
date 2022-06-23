#SET IS A DATA STRUCTURE, WHICH REPRESENTS A COLLECTION OF ELEMENTS
from re import S


s=set()
s.add(1)
s.add(3)
x=len(s) #lens return of items on a containter, in this case it will use s set
y=2 in s  #  verifica que el numero este en el set
w=4 in s

words=["hola","anaconda","elton john","cdmx","Isabel"] # una lista con palabras
words_set=set(words) # la lista de arriba la hacemos un set para despes buscar lo que estamos buscando,podemos no hacer la lista si no luego luego hacer un set
"cdmx" in words_set # es mas facil buscar palabras en un set
print(s,x,y,w)