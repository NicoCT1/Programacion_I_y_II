# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 07:33:03 2025
                        BASES DE DATODS 
@author: cortes
"""

import sqlite3 as sql

#CREAR BASE DE DATOS
conn =  sql.connect("Estudiantes_De_Programacion_II.db")

#CURSOR PARA BASE DE DATOS
cursor = conn.cursor()

#CREAR TABLA
cursor.execute(
    """CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER,
    proyecto TEXT
    )"""
    )
# %%

cursor.executemany(
    "INSERT INTO estudiantes (nombre, edad, proyecto) VALUES (?,?,?)",
    [
    ("Nicolas", 18, "procesamiento de imagenes"),
    ("Felipe", 21, "IA - BUSSINNESS INTELIGENCE"),
    ("Wilfredo", 21, "CIENCIA DE DATOS EN CIBERSEGURIDAD"),
    ("Roger", 27, "Actuaria - Riesgos financieros")
    ]
    )
# %%

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
proyecto = input("Ingrese el nombre de su proyecto: ")

cursor.execute(
    "INSERT INTO estudiantes (nombre, edad, proyecto) VALUES (?,?,?)",
    (nombre, edad, proyecto)
    )
# %%

cursor.execute("SELECT * FROM estudiantes")
print("Todos los estudiantes: ")
for fila in cursor.fetchall():
    print(fila)
# %%
    
cursor.execute("SELECT nombre, proyecto FROM estudiantes")
print("\nEstudiantes - nombre y su proyecto")
for fila in cursor.fetchall():
    print (fila)
# %%

cursor.execute("SELECT nombre, proyecto FROM estudiantes WHERE edad < 20")
print("\nEstudiantes - nombre y su proyecto")
for fila in cursor.fetchall():
    print (fila)

cursor.execute("SELECT nombre, proyecto FROM estudiantes WHERE edad < 30")
print("\nEstudiantes - nombre y su proyecto")
for fila in cursor.fetchall():
    print (fila)

cursor.execute("SELECT nombre, proyecto FROM estudiantes WHERE edad > 30")
print("\nEstudiantes - nombre y su proyecto")
for fila in cursor.fetchall():
    print (fila)

# %%

#ORDENAR DE FORMA ASCENDENTE#
cursor.execute("SELECT * FROM estudiantes ORDER BY edad ASC")
for fila in cursor.fetchall():
    print (fila)


#ORDENAR DE FORMA DESCENDENTE#
cursor.execute("SELECT * FROM estudiantes ORDER BY edad DESC")
for fila in cursor.fetchall():
    print (fila)

# %%

cursor.execute("SELECT * FROM estudiantes WHERE nombre = ?", ("Felipe",))
for fila in cursor.fetchall():
    print (fila)

# %%

id_estudiante = int(input("Ingrese el ID del estudiante que desea eliminar: "))

cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
for fila in cursor.fetchall():
    print (fila)
    
# %%
    
cursor.execute("SELECT * FROM estudiantes")
print("Todos los estudiantes: ")
for fila in cursor.fetchall():
    print(fila)

# %%

conn.commit()
cursor.execute("SELECT * FROM estudiantes")

print("Todos los estudiantes: ")
for fila in cursor.fetchall():
    print(fila)

# %%

conn.commit()
conn.close()


