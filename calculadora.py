
def menu():
    print("--SELECCIONE UNA OPCIÓN---")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Exponerciar")
    leer_opcion()

def leer_opcion():
    try:        
        opcion = int(input(">>>"))
        if (opcion<1 or opcion>5):
            print("Seleccionaste una opción fuera del rango (1-5)")
            leer_opcion()
        else:
            if(opcion == 1):
                sumar()
            elif (opcion == 2):
                restar()
            elif(opcion == 3):
                multiplicar()
            elif(opcion == 4):
                dividir()
            
    except:
        print("Seleccione una opción valida")
        leer_opcion()
        return

def leer_numero1():
    try:
        numero1 = float(input("Ingrese el primero número : "))
        return numero1
    except:
        print("Error no ingresaste un número !")
        n1=leer_numero1()
        
def leer_numero2():
    try:
        numero2 = float(input("Ingrese el segundo número : "))
        return numero2
    except:
        print("Error no ingresaste un número !")
        n2=leer_numero2()
        

def sumar():
    try:
        n1 = float(input("Ingrese el primer número : "))
        n2 = float(input("Ingrese el segundo número : "))
        print("La suma de los números es",n1+n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        sumar()

def restar():
    try:
        n1 = float(input("Ingrese el primer número : "))
        n2 = float(input("Ingrese el segundo número : "))
        print("La resta de los números es",n1-n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        restar()

def multiplicar():
    try:
        n1 = float(input("Ingrese el primer número : "))
        n2 = float(input("Ingrese el segundo número : "))
        print("La multiplicación de los números es",n1*n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        multiplicar()

def dividir():
    try:
        n1 = float(input("Ingrese el primer número : "))
        n2 = float(input("Ingrese el segundo número : "))
        #controlar división por cero
        try:
            print("La división de los números es",n1/n2)
            menu()
        except:
            print("La división por cero es imposible !")
            dividir()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        dividir()

menu()

