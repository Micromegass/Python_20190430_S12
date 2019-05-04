#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from os.path import dirname, abspath, basename
import sqlite3

ruta_de_este_script   = dirname(abspath(__file__))
nombre_de_este_script = basename(__file__)

ruta_bd = ruta_de_este_script + "̣/prueba.db"

print(ruta_bd)
conexion = sqlite3.connect(ruta_bd)

texto_crear_tabla='''   CREATE TABLE T2 
                     (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       fecha_creacion TIMESTAMP DEFAULT (datetime('now','localtime')),
                       un_texto TEXT
                     );
                   '''
c = conexion.cursor()

c.execute(texto_crear_tabla)

c.execute("INSERT INTO T2 (un_texto) VALUES('⊙⊙⊙⊙⊙⊙⊙')")
c.execute("INSERT INTO T2 (un_texto) VALUES('ááááááá')")

conexion.commit()

conexion.close()

#Fuentes
#http://www.pythondiario.com/2013/12/python-y-sqlite3-como-base-de-datos.html

