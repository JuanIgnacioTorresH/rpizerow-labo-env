from gpiozero import LED
from time import sleep
#Importo librerias necesarias

ledR = LED (19)
ledG = LED (13)
ledB = LED (26)
#Asigno los pines de los led a variables (R para rojo, G para verde, B para azul)

def red():
	ledR.on()
	sleep (1)
	ledR.off()
	sleep (1)
#Funcion que prende el led rojo por un segundo y lo apaga por un segundo

def blue():
	ledB.on()
	sleep (0.5)
	ledB.off()
	sleep (0.5)
#Funcion que prende el led azul por medio segundo y lo apaga por medio segundo

def green():
	ledG.on()
	sleep (0.25)
	ledG.off()
	sleep (0.25)
#Funcion que prende el led verde por un cuarto de segundo y lo apaga por otro cuarto de segundo

while (True):
	red()
	blue()
	green()
#Bucle en el que se ejecuta cada función en secuencia
