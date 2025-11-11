# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 07:33:59 2025

@author: corte
"""

class Financiera:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self, nombre):
        if nombre not in self.datos:
            return None
        valores = self.datos[nombre]
        return sum(valores) / len(valores) if valores else 0

    def riesgo(self, nombre):
        promedio_cliente = self.promedio(nombre)
        if promedio_cliente is None:
            return "Cliente no encontrado"
        if promedio_cliente < 0:
            return "Alto riesgo"
        if promedio_cliente < 10_000_000:
            return "Riesgo medio"
        return "Riesgo bajo"


clientes = {}
cantidad = int(input("¿Cuántos clientes desea registrar? "))

for idx in range(1, cantidad + 1):
    cliente = input(f"\nNombre del cliente {idx}: ")
    clientes[cliente] = []
    
    movs = int(input(f"¿Cuántos movimientos tiene {cliente}? "))
    for k in range(1, movs + 1):
        entrada = float(input(f"   Movimiento {k}: "))
        clientes[cliente].append(entrada)

banco = Financiera(clientes)

print("\n--- Resultados ---")
for nombre_cliente in clientes:
    print(f"\nCliente: {nombre_cliente}")
    print(f"Promedio: {banco.promedio(nombre_cliente)}")
    print(f"Categoría de riesgo: {banco.riesgo(nombre_cliente)}")