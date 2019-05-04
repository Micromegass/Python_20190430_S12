import sys
                            
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def la_ventana():
    #THIS IS MANDATORY
   LA_APLICACION = QApplication(sys.argv) #Aplicación Qt que se encarga de la ventana
   #LA_APLICACION = QApplication(["ESO"]) #Aplicación Qt que se encarga de la ventana
   # LA_APLICACION = QApplication(list()) #ERROR
   # LA_APLICACION = QApplication() #ERROR

   
   UNA_VENTANA = QWidget() #Una Ventana nueva
   
   etiqueta_de_texto = QLabel(UNA_VENTANA) #Nuevo Control (QLabel)
   etiqueta_de_texto.setText("Hola Mundo!") #Texto del Control
   etiqueta_de_texto.move(110,85) #Coordenadas del Control

   UNA_VENTANA.setGeometry(180,180,360,180)#Dimension y Tamaño de la Ventana
   UNA_VENTANA.setWindowTitle("PyQt5 Ejemplo") #Titulo de la Ventana
   UNA_VENTANA.show() #Mostrar la Ventana

    #THIS IS MANDATORY
   sys.exit(LA_APLICACION.exec_()) #Cerrar la Ventana y la Aplicación

if __name__ == '__main__':
   la_ventana()
