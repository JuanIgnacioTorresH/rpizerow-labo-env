from gpiozero import LED
from time import sleep
#Importo librerias necesarias

button = Button (18)
#Asigno el pin correspondiente al botón a una variable
ledR = LED (19)
ledG = LED (13)
ledB = LED (26)
#Asigno los pines de los led a variables (R para rojo, G para verde, B para azul)

while (True):
    ledR.on
    sleep (0.5)
    ledR.off
    sleep (0.5)
    #Enciendo el LED Rojo por medio segundo y lo apago
    ledG.on
    sleep (0.5)
    ledG.off
    sleep (0.5)
    #Enciendo el LED Verde por medio segundo y lo apago
    ledB.on
    sleep (0.5)
    ledB.off
    #Enciendo el LED Azul por medio segundo y lo apago
