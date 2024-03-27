from gpiozero import LED, Button
from signal import pause
#Importo librerias necesarias

button = Button (18)
#Asigno el pin del botón a una variable
ledR = LED (19)
#Asigno al pin de uno de los led (el rojo) a una variables

button.when_pressed = ledR.on
#Propiedad que cuando el botón esta apretado, se prende el led
button.when_released = ledR.off
#Propiedad que cuando el botón se suelta o no está apretado, se apaga
pause()
