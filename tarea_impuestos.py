class Empleado():  # crear una clase
   
    def Nombre(self):
        print('Ingresa tu nombre:')
        x=input()
    def Años(self):
        print('ingresa tu sueldo:')
        y=int(input())
        if y>=3000:
            print('debes pagar impuestos:')
        else:
            print('no pagas impuestos')
Emp=Empleado()
Emp.Nombre()
Emp.Años()