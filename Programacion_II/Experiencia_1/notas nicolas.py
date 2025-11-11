# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 21:20:57 2025

@author: cortes
"""

##  PROGRAMACIÓN ORIENTADA A OBJETOS  ##

class Automovil:
    # Atributos - Inicializarlos - Metodo Constructor
    # Encapsular -> atributos, metodos __variables, __metodos()
    def __init__(self):
        self.__largoChasis = 2.50
        self.__anchoChasis = 1.20
        self.__ruedas = 4
        self.__enMarcha = False
        print("Inicializada las variables")
   
    # Metodos
    def arrancar(self, arranca):
        self.__enMarcha = arranca
       
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()
       
        if(self.__enMarcha)and(chequeo):
            return "El automóvil se encuentra en movimiento"
        elif (self.__enMarcha) and (chequeo == False):
            return "Algo salio mal. EL VEHICULO NO PUEDE ARRANCAR"    
        else:
            return "El automovil esta detenido"
       
    def estado(self):
        print(f"El automovil tiene un largo de chasis {self.__largoChasis} m, con un ancho de chasis {self.__anchoChasis} m, y tiene {self.__ruedas} ruedas.")
   
    # chequear los testigos
    def __chequeoInterno(self):
        print("Realizando chequeo")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.temperatura = "ok"
        self.puertas = "abiertas"
        if (self.gasolina == "ok") and (self.aceite == "ok") and (self.temperatura == "ok") and (self.puertas == "cerradas"):
            return True
        else:
            return False

# %% - Instanciando Objetos
# Automovil 1
print("Creacion de objeto 1")
automovil1 = Automovil()
print(automovil1.arrancar(False))
automovil1.estado()

print("--------------- Objeto 2 ----------")
# Automovil 1
mustang = Automovil()
print(mustang.arrancar(True))
mustang.estado()



# %% TRABAJO EN CLASE 




class Estudiante:
    def __init__(self):
        self.__Nombre = None
        self.__Edad = None
        self.__Identificacion = None
        self.__Calificacion = None
        print("Estudiante registrado")

    def datos(self, nombre, edad, identificacion):
        self.__Nombre = nombre
        self.__Edad = edad
        self.__Identificacion = identificacion

    def promedio(self, a, b, c):
        return (a + b + c) / 3

    def notas(self):
        nota1 = float(input("Ingrese la nota número 1: "))
        while nota1 < 0 or nota1 > 5:
            nota1 = float(input("Lo siento, la nota debe estar entre 0 y 5: "))

        nota2 = float(input("Ingrese la nota número 2: "))
        while nota2 < 0 or nota2 > 5:
            nota2 = float(input("Lo siento, la nota debe estar entre 0 y 5: "))

        nota3 = float(input("Ingrese la nota número 3: "))
        while nota3 < 0 or nota3 > 5:
            nota3 = float(input("Lo siento, la nota debe estar entre 0 y 5: "))

        self.__Calificacion = self.promedio(nota1, nota2, nota3)

        if self.__Calificacion >= 3.0:
            print(f"El estudiante {self.__Nombre} aprobó la materia con una calificación de {self.__Calificacion:.2f}")
        else:
            print(f"El estudiante {self.__Nombre} no aprobó la materia con una calificación de {self.__Calificacion:.2f}")


est1 = Estudiante()
est1.datos("Nicolás", 18, 3333)
est1.notas()








