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
class Ticket:
    estudiante= " "
    profesor = " "
    hora= " "
    
    def __init__(self, nombre_estudiante:str, nombre_profesor:str, hora:str):
        self.estudiante=nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora

class Agenda:
    def __init__(self):
            self.tickets: list[Ticket] = []

    def disponibilidad(self, profesor:str, hora:str) -> bool:
        for ticket in self.tickets:
            if (ticket.profesor == profesor) and (ticket.hora == hora):
                print("El profesor no está disponible en esta hora")
                return False
        print("El profesor se encuentra disponible en el horario")
        return True

    def agregar_ticket(self, estudiante:str, profesor:str, hora:str) -> bool:
        if (self.disponibilidad(profesor, hora) == True):
            self.tickets.append(Ticket(estudiante, profesor, hora))
            return True
        return False

    def eliminar_ticket(self, profesor:str, hora:str) -> bool:
        for profe, ticket in enumerate(self.tickets):
            if (ticket.profesor == profesor) and (ticket.hora == hora):
                del self.tickets[profe]
                return True
        print("No hay ningun tutoria agendada en esta hora para el profesor")
        return False

    def mostrar_ticket(self):
        if(not self.tickets):
            print("La agenda se encuentra vacía")
            return
        print("------------ Tutorias -----------")
        for ticket in self.tickets:
            print(f"- {ticket.hora}\t | {ticket.profesor}\t -->{ticket.estudiante}")
tutoria = Agenda()
tutoria.mostrar_ticket()
tutoria.agregar_ticket("Felipe", "Jorge", "14:00")
tutoria.agregar_ticket("Nicolas", "Miller","9:00")
tutoria.mostrar_ticket()
tutoria.disponibilidad("Jorge", "8:00")
tutoria.disponibilidad("Jorge", "14:00")
tutoria.mostrar_ticket()
tutoria.eliminar_ticket("Miller", "9:00")
tutoria.eliminar_ticket("Miller", "8:00")
tutoria.mostrar_ticket()
            

# %%

class Solicitud:
    def _init_(self, nombre_estudiante, nombre_profesor, hora):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora

class Agenda:
    def _init_(self):
        self.solicitudes: list[Solicitud] = []
        
    def _len_(self):
        "Devuelve la cantidad de tutorías agendadas"""
        return len(self.solicitudes)

    def disponibilidad(self, profesor: str, hora: str) -> bool:
        for solicitud in self.solicitudes:
            if solicitud.profesor == profesor and solicitud.hora == hora:
                print(" El profesor NO está disponible en esta hora")
                return False
        print(" El profesor está disponible en esta hora")
        return True

    def agregar_turno(self, estudiante: str, profesor: str, hora: str) -> bool:
        if self.disponibilidad(profesor, hora):
            self.solicitudes.append(Solicitud(estudiante, profesor, hora))
            print("Turno agregado con éxito")
            return True
        return False

    def eliminar_turno(self, profesor: str, hora: str):
        for idx, solicitud in enumerate(self.solicitudes):
            if solicitud.profesor == profesor and solicitud.hora == hora:
                del self.solicitudes[idx]
                print(" Turno eliminado correctamente")
                return True
        print(" No hay ninguna tutoría agendada para el profesor en esa hora")
        return False

    def mostrar_turno(self):
        if not self.solicitudes:
            print("La agenda está vacía")
            return
        print("\n----------- Tutorías -----------")
        for solicitud in self.solicitudes:
            print(f"- {solicitud.hora} \t {solicitud.profesor} \t {solicitud.estudiante}")
        print("--------------------------------")


profesores = ["Arley", "Luisa", "Jorge", "Liliana", "Miller", "César"]
agenda = Agenda()


def menu_profesores():
    print("\n--- Seleccione un profesor ---")
    print("1. Arley\n2. Luisa\n3. Jorge\n4. Liliana\n5. Miller\n6. César")

    try:
        opcion = int(input("Ingrese el número del profesor: "))
    except ValueError:
        print(" Ingrese un número válido")
        

    match opcion:
        case 1: return "Arley"
        case 2: return "Luisa"
        case 3: return "Jorge"
        case 4: return "Liliana"
        case 5: return "Miller"
        case 6: return "César"
        case _:
            print(" Profesor no válido")
            return None


# -------- Menú Principal --------
while True:
    print("\n===== MENÚ AGENDA DE TUTORÍAS =====")
    print("1. Ver disponibilidad")
    print("2. Agregar turno")
    print("3. Eliminar turno")
    print("4. Mostrar agenda")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print(" Ingrese un número válido")
        continue

    match opcion:
        case 1:
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora (ej: 10:00): ")
                agenda.disponibilidad(profesor, hora)

        case 2:
            estudiante = input("Ingrese el nombre del estudiante: ")
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora (ej: 11:00): ")
                agenda.agregar_turno(estudiante, profesor, hora)

        case 3:
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora a eliminar: ")
                agenda.eliminar_turno(profesor, hora)

        case 4:
            agenda.mostrar_turno()
            print(f" Total de tutorías agendadas: {len(agenda)}")  

        case 5:
            print(" Saliendo del sistema...")
            break

        case _:
            print(" Opción no válida, intente de nuevo.")