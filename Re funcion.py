import re
class ex():

    txt = input("ingresa un texto para su analisis")
    x = re.split("\s", txt,)
    #x= re.search("om",txt)  #despues del txt, podemos delimitar enl numero de veces de separar las palabras
    print(x)

#string format() hace que el input sea modificado a nuestra preferencia
    def format(self):
        piezas=3
        numeroitem=459
        price=49
        myorder= "yo quiero {} piezas del item numero {} por {:.2f} dollars."
        print(myorder.format(piezas,numeroitem,price))


x=ex()
x.format()


#Split the string at every white-space character:

