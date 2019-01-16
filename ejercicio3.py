#creación de una función
def saludo():
    nombre = input("Ingresa tu nombre ->") 
    apellido = input("Ingresa tu apellido ->")
    sexo = input("Ingresa tu sexo (masculino o femenino) ->")
    
    if (sexo == "masculino"):
        print("Hola Sr.",nombre,apellido)
    elif (sexo =="femenino"):
        print("Hola Sra.",nombre,apellido)
    else:
        print("Error el sexo debe ser masculino o femenino !")
        saludo()

saludo()

