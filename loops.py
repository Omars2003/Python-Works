x=0
while x<=10:  # aqui ocupamos el while, mientras se cumpla la condicion se imprime y se va sumando al contador 1
    print(x)
    x+=1
for y in range (29): #aqui ocupamos un for mas feninido con condiciones especificas
    if y==20:
        continue #continue corre a la siguiente indicacion  por lo que cuando sea ==20 no la va a imprimir si que va al if de abajo
    if y==22:
        break # cuando y sea igual a =22 se rompre el codigo
    print(y)