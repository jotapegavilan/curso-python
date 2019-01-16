try:
    numero1 = float(input("Ingrese el primer número : "))
    numero2 = float(input("Ingrese el segundo número : "))
    suma = numero1+numero2
    resta = numero1-numero2
    multiplicacion = numero1*numero2
    try:
        division = numero1 / numero2
        print("La suma de los números es",suma)
        print("La resta de los números es",resta)
        print("La multiplicación de los números es",multiplicacion)
        print("La división de los números es",division)
    except:
        print("El divisor no puede ser un 0")
        
except:
    print("No ingreses letras ni simbolos")
    


