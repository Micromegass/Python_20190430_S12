#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3


def consulta_muestre_las_filas(ruta_de_la_bd,sentencia,encabezados_resultado=True):
    with sqlite3.connect(ruta_de_la_bd) as conn:
         c = conn.cursor()
         c.execute(sentencia)
         filas = c.fetchall()
         cuantos = len(filas)
         print("cuantos =",cuantos)
         if encabezados_resultado:
            encabezados = list(map(lambda x: x[0], c.description))
            cuantos_encabezados = len(encabezados)
            es = ""
            for i in range(cuantos_encabezados):
                es = es + encabezados[i]
                if (i < (cuantos_encabezados -1)):
                    es = es + ","                
            print(es)    
         for fila in filas:
             f = ""
             contador = 0
             for e in fila:
                 contador = contador + 1 
                 f = f + str(e)
                 if (contador < cuantos_encabezados):
                     f = f + ","
             print(f)

     
def consultas(ruta_bd):
    consultas = list()
    consultas.append("SELECT * FROM colores;")
    consultas.append("SELECT * FROM colores WHERE idColor > 5;")
    consultas.append("SELECT * FROM colores WHERE idColor > 300;")
    consultas.append("SELECT * FROM colores WHERE Color LIKE '%a%';")
    consultas.append("SELECT * FROM colores WHERE Color LIKE '%e%';")
    consultas.append("SELECT * FROM vFechas;")
    consultas.append("SELECT * FROM Notas;")
    
    
    cuantas = len(consultas)
    largo_cuantas = len(str(cuantas))
    
    for i in range(cuantas):
        sentencia = consultas[i]
        print("i",str(i+1).zfill(largo_cuantas),"+"*54)
        print(sentencia)
        consulta_muestre_las_filas(ruta_bd,sentencia)
        print("f",str(i+1).zfill(largo_cuantas),"+"*54)

def principal():
    carpeta_de_este_script = os.path.dirname(os.path.realpath(__file__))
    ruta_carpeta_bd = carpeta_de_este_script + os.path.sep + "bd"
    ruta_bd = ruta_carpeta_bd + os.path.sep + "bd01.db"
    print(ruta_bd)
    
    consultas(ruta_bd)    
    

if __name__ == "__main__" :
   principal() 
   
   

