import sys
from random import randint as r                            
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def el_boton_01_clicked():
    print("ME HICIERON CLIC BTN01")

def el_boton_02_clicked():
    print("ME HICIERON CLIC BTN02")

def mostrar():
   LA_APLICACION = QApplication(["ESO"]) #Aplicación Qt que se encarga de la ventana
   
   UNA_VENTANA = QWidget() #Una Ventana nueva

   
   el_boton_01 = QPushButton(UNA_VENTANA) #Nuevo Control (QPushButton)
   el_boton_01.setText("El Botón Nro 1")
   el_boton_01.move(64,32)
   el_boton_01.clicked.connect(el_boton_01_clicked) #Asociar Evento a función

   el_boton_02 = QPushButton(UNA_VENTANA) #Nuevo Control (QPushButton)
   el_boton_02.setText("El Botón Nro 2")
   el_boton_02.move(64,64)
   el_boton_02.clicked.connect(el_boton_02_clicked) #Asociar Evento a función
   
   etiqueta_de_texto = QLabel(UNA_VENTANA) #Nuevo Control (QLabel)
   etiqueta_de_texto.setText("Hola Mundo!") #Texto del Control
   etiqueta_de_texto.move(160,85) #Coordenadas del Control

   UNA_VENTANA.setGeometry(180,180,360,180)#Dimension y Tamaño de la Ventana
   UNA_VENTANA.setWindowTitle("PyQt5 Ejemplo") #Titulo de la Ventana
   UNA_VENTANA.show() #Mostrar la Ventana

   sys.exit(LA_APLICACION.exec_()) #Cerrar la Ventana y la Aplicación

def principal():
    mostrar()


if __name__ == '__main__':
    principal()
   
