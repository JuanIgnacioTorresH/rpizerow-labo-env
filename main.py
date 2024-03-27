from gpiozero import LED
from time import sleep
#Importo librerias necesarias

ledR = LED (19)
ledG = LED (13)
ledB = LED (26)
#Asigno los pines de los led a variables (R para rojo, G para verde, B para azul)

x = 0
y = 0
z = 0

def red():
	ledR.on()
	sleep (1)
	ledR.off()
	sleep (1)

def blue():
	ledB.on()
	sleep (0.5)
	ledB.off()
	sleep (0.5)

def green():
	ledG.on()
	sleep (0.25)
	ledG.off()
	sleep (0.25)

while (True):
	red()
	blue()
	green()
