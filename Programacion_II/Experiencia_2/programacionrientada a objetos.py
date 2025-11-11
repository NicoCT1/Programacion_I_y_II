# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 07:19:51 2025

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
    
#%%
# Relacion de 

class Colegio:
    nombre = ""
    ubicacion = ""
    
    
    def __init__(self,nombreCol,ubicacionCol):
        self.nombre = nombreCol
        self.ubicacion = ubicacionCol
        self.estudiantes = []
    
    
    def adicionar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        
    def eliminar_estudiante(self,estudiante):
        for e in self.estudiantes:
            if (e == estudiante):
                self.estudiantes.remove(estudiante)
    
    def mostrar_estudiantes(self):
       print("Los estudiantes son: ")
       for estudiante in self.estudiantes:
           print(estudiante)
    
    
class Estudiante:
     def __init__(self,nombreEstudiante,edadEstudiante,gradoEstudiante):
         self.nombre: str = nombreEstudiante
         self.edad: int= edadEstudiante
         self.grado: str = gradoEstudiante
         self.promedio: float = 0.0
         
     def __str__(self):
         return  f"{self.nombre}, {self.edad}, {self.grado}, {self.promedio}"
    
     def promedio(self,notas):
         suma = 0 
         for i in notas:
             self.suma += i
         self.promedio = self.suma / len(notas)
     def informacion_estudiante(self):
         print(f"El estudiante es {self.nombre} con edad {self.edad}, del grado {self.grado} tiene es siguiente promedio: {self.promedio}")
        
     
         
        
san_pablo = Colegio("San Pablo", "Victoria-Caldas")
e1 = Estudiante("Roger Villa", 27,"pregrado")
e2 = Estudiante("Wilfredo Calderon", 21,"pregrado")
e3 = Estudiante("Nicolas Cortes", 18,"pregrado") 
e4 = Estudiante("Felipe Choconta", 21,"pregrado")
e5 = Estudiante("Miller Quiroga", 45,"pregrado")
san_pablo.adicionar_estudiante(e1)
san_pablo.adicionar_estudiante(e2)
san_pablo.adicionar_estudiante(e3)
san_pablo.adicionar_estudiante(e4)
san_pablo.adicionar_estudiante(e5)
san_pablo.mostrar_estudiantes()

# %%

class solicitud:
    estudiante = ""
    profesor = ""
    hora = ""
    
    def __init(self, nombre_estudiante, nombre_profesor, hora):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora
        
class Agenda:
    def __init(self):
        self.turno: list[solicitud] = []
        
    def agregar_turno(self, estudiante, profesor, hora)-> bool:
        if(self. disponibilidad(profesor, hora)==True):
            self.turnos.append(estudiante, profesor, hora)
            return True
        return False
    
    def eliminar_turno(self, profesor, hora):
        for profesor, turno in enumerate(self. turnos):
            if (turno. profesor == profesor) and (turno. hora == hora):
                self. turno.remove(turno)
                return True
        print("No hay ninguna tutoria agendada para el profesor a esta hora")
        return False
    
    def disponibilidad(self, profesor, hora) -> bool: 
        for turno in self.turnos:
            if(turno.profesor == profesor):
                print("El profesor no tiene disponibilidad")
                return False
    
    def mostrar_turno(self):
        if (not self. turnos):
            print("La agenda está vacía")
            return
        
        print("-----------Tutorias-----------")
        for turno in self.trunos:
            print(f"-{turno. hora} \t {turno.profesor} \t {turno.estudiante} \t")
            
# %%
            
agenda = Agenda()
agenda.mostrar_turno()