# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 23:39:29 2025

@author: corte
"""

class Conversor:
    def __init__(self, numero_str: str, base_origen: int):
        self.__numero_str = numero_str
        self.__base_origen = base_origen

        try:
            int(self.__numero_str, self.__base_origen)
        except ValueError:
            raise ValueError("Número inválido para la base de origen")

    def __a_decimal(self) -> int:
        return int(self.__numero_str, self.__base_origen)

    def convertir_a_binario(self) -> str:
        numero = self.__a_decimal()
        if numero == 0: 
            return "0"
        if numero < 0:
            numero = abs(numero)

        resultado = []
        while numero > 0:
            resultado.append(str(numero % 2))
            numero //= 2
        return "".join(reversed(resultado))

    def convertir_a_octal(self) -> str:
        numero = self.__a_decimal()
        if numero == 0:
            return "0"
        if numero < 0:
            numero = abs(numero)

        resultado = []
        while numero > 0:
            resultado.append(str(numero % 8))
            numero //= 8
        return "".join(reversed(resultado))

    def convertir_a_hexadecimal(self) -> str:
        digitos = "0123456789ABCDEF"
        numero = self.__a_decimal()
        if numero == 0:
            return "0"
        if numero < 0:
            numero = abs(numero)

        resultado = []
        while numero > 0:
            residuo = numero % 16
            resultado.append(digitos[residuo])
            numero //= 16

        return "".join(reversed(resultado))

    def convertir_a_decimal(self) -> str:
        return str(self.__a_decimal())



def menu():
    print("\n--- CONVERSOR DE SISTEMAS NUMÉRICOS ---")
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    print("4. Hexadecimal")
    print("5. Salir")

def obtener_base(opcion: int) -> int:
    bases = {1: 10, 2: 2, 3: 8, 4: 16}
    return bases.get(opcion, None)

def main():
    while True:
        try:
            menu()
            op_origen = int(input("Seleccione la base de origen: "))
            if op_origen == 5:
                print("¡Hasta luego!")
                break
            base_origen = obtener_base(op_origen)
            if not base_origen:
                print("Opción inválida.")
                continue

            menu()
            op_destino = int(input("Seleccione la base de destino: "))
            if op_destino == 5:
                print("¡Hasta luego!")
                break
            base_destino = obtener_base(op_destino)
            if not base_destino:
                print("Opción inválida.")
                continue

            numero = input("Ingrese el número a convertir: ")

            conversor = Conversor(numero, base_origen)

            if base_destino == 10:
                resultado = conversor.convertir_a_decimal()
            elif base_destino == 2:
                resultado = conversor.convertir_a_binario()
            elif base_destino == 8:
                resultado = conversor.convertir_a_octal()
            elif base_destino == 16:
                resultado = conversor.convertir_a_hexadecimal()

            print(f"\nResultado de la conversión: {resultado}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
