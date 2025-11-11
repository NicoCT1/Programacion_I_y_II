# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:36:10 2025

@author: corte
"""

import numpy as np
import random

alumnos = int(input("Ingrese la cantidad de estudiantes de la clase: ")) + 1
notas = int(input("Ingrese la cantidad de notas de la materia: ")) + 1

tabla_calif = np.full((alumnos, notas), None, dtype=object)

tabla_calif[0, 0] = "Estudiantes"
for j in range(1, notas):
    tabla_calif[0, j] = f"Nota{j}"
for i in range(1, alumnos):
    tabla_calif[i, 0] = f"Estudiante{i}"

class MatrizCalificaciones:
    
    def __init__(self, tabla):
        self.__tabla = tabla
        print("Notas encontradas")
        
    def valores(self):
        for i in range(1, self.__tabla.shape[0]):
            for j in range(1, self.__tabla.shape[1]):
                self.__tabla[i, j] = random.randint(0, 5)
                
    def mostrar(self):
        for fila in self.__tabla:
            print("\t".join(map(str, fila)))
            
    def promedio(self):
        promedios = []
        for i in range(1, self.__tabla.shape[0]):
            notas = list(map(int, self.__tabla[i, 1:]))
            promedios.append((self.__tabla[i, 0], sum(notas)/len(notas)))
        return promedios
    
    def nota_maxima(self):
        max_nota = -1
        est = None
        for i in range(1, self.__tabla.shape[0]):
            notas = list(map(int, self.__tabla[i, 1:]))
            if max(notas) > max_nota:
                max_nota = max(notas)
                est = self.__tabla[i, 0]
        return est, max_nota
    
# %%

matriz = MatrizCalificaciones(tabla_calif)
matriz.valores()
matriz.mostrar()

print("\nPromedios:")
for est, prom in matriz.promedio():
    print(f"{est}: {prom:.2f}")

print("\nNota máxima:", matriz.nota_maxima())
