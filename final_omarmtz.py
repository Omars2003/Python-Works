from msilib.schema import Class
import hashlib
import calendar 
print ('HECHO POR OMAR MARTINEZ GARCIA 14/06/22')
print('Ingresa El numero del programa que quieres ejecutar:\n1:Calcula tu peso ideal\n2:Contador de letras\n3:Calendario\n4:Inicio de sesion\n')  #Indicamos que programa quieres correr
num=int(input()) #ingresas el numero 
if num==1: # se pone la condicional de if por si elige el numero 1 corra el programa de peso ideal
    class Pesoideal(): #se crea la clase peso ideal donde se hara el calculo de tu peso ideal

     def Calcular(self): # se crea el objeto que calculara el peso y se ingresaran los datos del genero del usuario y la altura del usuario
        print("Ingresa 'M' para masculino y 'F' para femenino") #se piden las entradas del genero
        sexo = input() #ingresas letra
        print('Altura con punto decimal, ejemplo 1.78') #pide la altura
        altura = input()#ingresa la altura del usuario

        peso_ideal_m = (72.7 * float(altura)) - 58 #hace el calculo del hombre dependiendo los datos ingresados y los guarda en una nueva variable
        peso_ideal_f = (62.1 * float(altura)) - 44.7 #hace el calculo de la mujer dependiendo los datos ingresados y los guarda en una variable

        if sexo == "M":  # se crea la condicional de que si eligio m imprima el resultado  de peso_ideal_m
          print("Tu peso ideal es %.2f: " % peso_ideal_m)
        elif sexo == "F": #y si eligio la f de femenino  imprime el resultado
         print("Tu peso ideal es %.2f: " % peso_ideal_f)#aqui se imprime el resultado
        else: #si no eligio la F ni la M  que imprima que que sexo invalido
         print("Sexo invalido!") #aqui se imprime el mensaje
    Mipeso=Pesoideal() #a la clase le damos el nombre de Mipeso y de igual manera se esta mandando a llamar
    Mipeso.Calcular() #dentro de la clase mi peso mandamos a llamar el objeto Calcular que hace todo el procedimiento
elif num==2: # aqui es la segunda opcion con el programa de contar las letras del texto que ingresas,solo corre si eliges el numero 2 al principio
    class ContadorLetras(): # se crea la clase  ContadorLetras que cuenta las letras del texto
       def co(self):  #objeo que realiza el procedimiento
        titulo= "Contar las letras de cualquier frase".capitalize() #Variable para el titulo
        print (titulo.center(50,"*"))#centro el titulo
        frc=(input("Ingresa una frase: "))#se solicita la frase
        let=len(frc)#saco la logitud original
        cont=0 #contador para los espacios
        contnum=0 #contador para los numeros
        contpuc=0 #contador para los signos
        suma=0 #variable para sumar los contadores
        for i in range(0,let): # se hace un bucle con un limite de 0 al numero de caracteres del texto ingresado
            if (frc[i].isspace()): #si la frase tiene espacios se agregan a un contador
             cont+=1 #aqui se van agragando a una variable que es un contador
            elif(frc[i].isdigit()): # y si no tiene espacios o ya conto todos los espacion se pasa con los digitos, cuenta los numeros o caracteres int 
             contnum+=1 #los acumula en un contador 
            elif(frc[i] in "?¡¿*,.-_'"): #y de igual manera con signos
             contpuc+=1 #los acumula en un contador de igual manera
        suma=cont+contnum+contpuc #sumo los contadores
        rpta=let-suma #al final solo lo resto a la longitud original
        print("La frase tiene :",rpta,"letras") #imprime las letras que tiene 
    pala=ContadorLetras()# le das un nombre a la clase y llamas a la clase
    pala.co()# de la clase llamamos el objeto 
elif num==3: # si elegiste el numero 3 al principio se corre la clase del calendario
   class Calendario(): # se crea la clase calendario
        def cal(self): #se crea el objeto calendario
          print('INGRESA UN MES DE 1 AL 12') #pedimos al usuario ingresar un mes del año,en numeros del 1 al 12
          mm = int(input()) #el usuario ingresa el mes
          print('Ingresa un año') #aqui se imprime que ahora ingrese un año
          yy = int(input()) # el usuario ingresa el año

          month ={1:'Enero', 2:'Febrero', 3:'Marzo', #es una lista con los meses del año cada una con un numero del uno al 12,usando la funcion de diccionario
		         4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio',
		         8:'Agosto', 9:'Septiembre', 10:'Octubre',
		         11:'Noviembre', 12:'Diciembre'}

          dia =(yy-1)% 400 # se crea una variable con el nombre dia que va hacer una operacion aritmetica
          dia = (dia//100)*5 + ((dia % 100) - (dia % 100)//4) + ((dia % 100)//4)*2 #el resultado de la variable interior se le aplicando varias operaciones y se suman y se guardan en esa misma
          dia = dia % 7 # el resultado anterior se divide y se crea la variable fianl con la que se hara el siguiente proceimiento

          nly =[31, 28, 31, 30, 31, 30, # son los dias que tiene cada mes en año bisiesto
	             31, 31, 30, 31, 30, 31]
          ly =[31, 29, 31, 30, 31, 30, # son los dias que tiene cada mes en año no bisiesto
	            31, 31, 30, 31, 30, 31]
          s = 0 #se define una variable con un valor de 0
          if yy % 4 == 0:
           for i in range(mm-1):
               s+= ly[i]
          else:
            for i in range(mm-1):
              s+= nly[i]
          dia += s % 7
          dia = dia % 7
   
# variable used for white space filling 
# where date not present
          space =''
          space = space.rjust(2, ' ')


          print(month[mm], yy)
          print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

          if mm == 9 or mm == 4 or mm == 6 or mm == 11:  #aqui es para ver cuantos dias tiene el mes 
              for i in range(31 + dia): # se crea un bucle en un range hasta 31 +dia
          
                if i<= dia: #si la variable i es menor o igual que la variable dia imprime space
                    print(space, end =' ')
                else: #y si no imprime 
                    print("{:02d}".format(i-dia), end =' ')
                    if (i + 1)% 7 == 0:
                     print()
          elif mm == 2: # si el mm es 2 o febrero  y se crea un for 
                if yy % 4 == 0: #ocupamos la condicional de if con la variable yy en mod y si ==0, p tiene 30 
                    p = 30
                else: # si no p  tiene el valor de 29 y
                  p = 29
          
                for i in range(p + dia): #un bucle en el rango del valor de p+dia
                   if i<= dia:
                    print(space, end =' ')
                   else:
                    print("{:02d}".format(i-dia), end =' ')
                    if (i + 1)% 7 == 0:
                     print() 
          else:
               for i in range(32 + dia):
          
                if i<= dia:
                  print(space, end =' ')
                else:
                  print("{:02d}".format(i-dia), end =' ')
                  if (i + 1)% 7 == 0:
                    print()
   c=Calendario() # a la clase Calendario le damos el nombre de c. y se manda a llamar la clase
   c.cal() # mandamos a llamar dentro de la clase c el objeto cal

elif num==4: # por ultimo si ingresas en numero 4 correo el programa de crear e iniciar sesion
  class Log(): #se crea una clase que tendra las objetos para el programa
   def signup(): # se crea una clase que llamamos signup que es para crear una cuenta
      email = input("Ingresa tu correo electronico : ") # te pide que ingreses tu correo electronico
      pwd = input("Ingresa tu contraseña:") #ingresas tu contraseña
      conf_pwd = input("Confirma tu contraseña:") #te pide ue confirmes tu contraseña
      if conf_pwd == pwd: #si las contraseñas coinciden correo l sig
        enc = conf_pwd.encode() #se codifican las contraseñas
        hash1 = hashlib.md5(enc).hexdigest() #las contraseñas se guardan en un formato diferente y checa que no ambas contraseñas sean las mismas
        with open("credentials.txt", "w") as f: #se abren y usan con funciones de texto especiales para esta funcio
             f.write(email + "\n") 
             f.write(hash1)
        f.close()
        print("Tu registro ha sido exitoso")  #si las contraseñas coinciden y todo funciono bien te da un mensja
      else:
        print("Las contraseñas no coincides! \n") # si las cotraseñas no coinciden te marca un error
   def login(): #ya que tienes una cuenta ahora te pide que inicies sesion,tienes que tener una cuenta ya aqui para que este bojeto funcioe
    email = input("Ingresa tu correo electronico:") # te pide tu correo electronico
    pwd = input("Ingresa tu contraseña: ") # te pide tu contraseña
    auth = pwd.encode() #checa que la contraseña no tenga errores
    auth_hash = hashlib.md5(auth).hexdigest() # le da formato al texto ingresado y lo comprara con el signup
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd: #comprara que los datos del sign up y log in coincidan 
         print("Inicio de sesion exitoso!") #se imprime un texto que te dice si fue exitoso tu programa
    else: # si no coinciden o hubo algun error de manda un mensaje de error
         print("Error al iniciar sesion \n")
  while 1: # se ocupa un while que es un bucle que hace que ingresa un opcion del codigo anterio 
    print("registrate o Inicia sesion")
    print("1.REGISTARTE")
    print("2.INICIA SESION")
    print("3.SALIR")
    ch = int(input("\nElige una opcion ")) # la variable ch guarda la opcion que usuario quiere ocupar
    if ch == 1: # si es 1 corre la la clase Log y el objeto sigup que es de registrarte
        Log.signup()
    elif ch == 2: #si eliges la opcion 2  dentro de la clase log, corre el objeto login
      Log.login()
        
    elif ch == 3: #si elige el 3 que es de salir te saca y corre al siguiente
        pass
    else: # si no eligio un numero del 1 al 3 te manda un menssaje de numero equivocado
        print("Numero equivocado")
  Clave=Log() #le ponemos el nombre de Clave al  objeto Log
  Clave.signup() #llamamos el bojeto sigup que esta en la clase Clave
  Clave.login()# y por ultimo hacemos lo mismo pero con el objeto login






