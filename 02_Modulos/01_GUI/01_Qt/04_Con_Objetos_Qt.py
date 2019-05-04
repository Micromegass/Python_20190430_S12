import sys
from random import randint as r                            
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton



class Una_Ventana(QWidget): #Hereda de QWidget
    def __init__(self):
        #Usar el Constructor del Padre
        super().__init__()
        #Invocar Metodo(función) Propio (Interno)
        self.Inicio_de_Ventana()
        
    def Inicio_de_Ventana(self):
        self.el_boton_01 = QPushButton(self) #Nuevo Control (QPushButton)
        self.el_boton_01.setText("COLOR al AZAR")
        self.el_boton_01.move(64,32)
        self.el_boton_01.clicked.connect(self.el_boton_01_clicked) #Asociar Evento a función

        self.el_boton_02 = QPushButton(self) #Nuevo Control (QPushButton)
        self.el_boton_02.setText("&Salir")#Tecla Caliente &
        self.el_boton_02.move(270,32)
        self.el_boton_02.clicked.connect(self.el_boton_02_clicked) #Asociar Evento a función


        self.setGeometry(180,180,360,180)#Dimension y Tamaño de la Ventana
        self.setWindowTitle("PyQt5 Ejemplo -- Con Objetos") #Titulo de la Ventana
        self.show() #Mostrar la Ventana
        
    def el_boton_01_clicked(self):
        print("ME HICIERON CLIC BTN01")
        color = (r(0,255),r(0,255),r(0,255))
        print(color)
        color_hex = "#%02x%02x%02x" % color
        print(color_hex)
        self.setStyleSheet("background-color:"+color_hex+";");
        
    def el_boton_02_clicked(self):
        print("ME HICIERON CLIC BTN01")
        self.close()

def prueba_ventana_con_poo():

   LA_APLICACION = QApplication(["ESO"]) #Aplicación Qt que se encarga de la ventana

   #Crear Objeto 
   la_ventana =  Una_Ventana()

   sys.exit(LA_APLICACION.exec_()) #Cerrar la Ventana y la Aplicación

def principal():
    prueba_ventana_con_poo()


if __name__ == '__main__':
    principal()
   
