# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 08:44:28 2025

@author: cortes
"""
import numpy as np

LigaDeCol = np. full ((3,9),None)

LigaDeCol[0,0]="Club"
LigaDeCol[0,1]="PJ"
LigaDeCol[0,2]="G"
LigaDeCol[0,3]="E"
LigaDeCol[0,4]="P"
LigaDeCol[0,5]="GF"
LigaDeCol[0,6]="GC"
LigaDeCol[0,7]="DG"
LigaDeCol[0,8]="Pts"

LigaDeCol[1,0]= input ("Ingrese cual va a ser el Primer equipo de la tabla de clasificasión: ")
LigaDeCol[2,0]=input ("Ingrese cual va a ser el Segundo equipo de la tabla de clasificasión: ")

decision1=input("¿ Quieres ingresar los datos de los equipos de futbol ?")
if decision1 == "si" or "yes":
    equipos=input("¿Los de datos de que equipo quieres ingresar?")
    if equipos == 1:
        
        for lista in LigaDeCol:
            print(lista)
            for equipos in lista:
                print (equipos) 