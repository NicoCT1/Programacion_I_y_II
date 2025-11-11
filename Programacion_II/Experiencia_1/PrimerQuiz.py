# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 23:22:21 2025

@author: corte
"""

import numpy as np

filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

matriz = np.zeros((filas, columnas))

for i in range(filas):
    for j in range(columnas):
       matriz[i, j] = (i + j) % 2

           