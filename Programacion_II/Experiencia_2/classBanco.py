# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 10:31:48 2025

@author: corte
"""

class Banco:
    nombre = ""
    def __init__(self, nombreBanco):
        self.nombre = nombreBanco
class Empleado:
    nombre = ""
    def __init__(self,nombreEmpleado):
        self.nombre = nombreEmpleado
        
Bancolombia = Banco("Bancolombia")
Nicolas = Empleado("Nicolas Cortes")

print(f"El sr {Nicolas.nombre}, tiene cuenta en el banco {Bancolombia.nombre}")   